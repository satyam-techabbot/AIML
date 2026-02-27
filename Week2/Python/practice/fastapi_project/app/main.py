from fastapi import FastAPI, Request, Depends, HTTPException, status, BackgroundTasks
from pydantic import BaseModel
import time
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from pwdlib import PasswordHash
from config.config import get_settings, Settings

# app setup
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pswd_hash = PasswordHash.recommended()
settings = get_settings()

# fake data
fake_users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": pswd_hash.hash("password123"),
        "role": "admin",
    },
    "bob": {
        "username": "bob",
        "hashed_password": pswd_hash.hash("password123"),
        "role": "user",
    },
}

# Models
class Tokens(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    username: str | None = None
    role: str | None = None

# bg tasks after send route
def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

# Utility functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pswd_hash.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user

def create_access_token(data : dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=15)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)

# defining which cross origin source is allowed
origins = [
    "http://127.0.0.1:8000/",
    "http://localhost:8000/",
    "http://localhost/",
    "http://127.0.0.1/",
]

# adding cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

# login route
@app.post("/login", response_model=Tokens)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends() ]
):
    user = authenticate_user(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(
        data = {
            "sub": user["username"],
            "role": user["role"],
        },
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {
        "access_token" : access_token,
        "token_type" : "Bearer"
    }

# Authentication Dependency
async def get_current_user(
    token : Annotated[str, Depends(oauth2_scheme)]
):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms = [settings.ALGORITHM]
        )
        username : str = payload.get("sub")
        role : str = payload.get("role")

        # print("TOKEN:", token)
        # print("SECRET:", settings.SECRET_KEY)
        # print("PAYLOAD:", payload)

        if username is None:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid Token"
            )
        
        return {
            "username" : username,
            "role" : role
        }
    
    except jwt.ExpiredSignatureError:
        raise HTTPException (
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Token Expired"
        )
    
    except jwt.InvalidTokenError:
        raise HTTPException (
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid Token"
        )

# middleware to calculate time taken by every http request
@app.middleware('http')
async def add_process_time_header(req: Request, call_next):
    start_time = time.time()
    response = await call_next(req)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_items(item_id: int, item: Item):
    return {"item_id ": item_id, "item": item}

# Protected Route
@app.get("/users/me")
async def read_users_me(
    curr_user : Annotated[dict, Depends(get_current_user)]
):
    return curr_user

# Admin Authorization
@app.get("/admin")
async def admin_only(
    curr_user : Annotated[dict, Depends(get_current_user)]
):
    if curr_user["role"] != "admin":
        raise HTTPException (
            status_code = status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    
    return {
        "message" : "Welcome Admin"
    }

@app.post("/send")
async def send_message(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Message sent!")
    return {"message": "Response sent immediately"}