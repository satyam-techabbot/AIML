# FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

We can create a whole backend using it.

## Key features:

- Fast: 
    Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.

- Fast to code: 
    Increase the speed to develop features by about 200% to 300%. *
- Fewer bugs: 
    Reduce about 40% of human (developer) induced errors. *
- Intuitive: 
    Great editor support. Completion everywhere. Less time debugging.

- Easy: 
    Designed to be easy to use and learn. Less time reading docs.
- Short: 
    Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: 
    Get production-ready code. With automatic interactive documentation.
- Standards-based: 
    Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

## Requirements
FastAPI stands on the shoulders of giants:
- Starlette for the web parts.
- Pydantic for the data parts.

## Installation
```bash
python -m venv venv
.\venv\Scripts\activate
pip install "fastapi[standard]"
```

## Get Started
After project installation, create a file main.py.

```python
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

After that, we can run the project ```fastapi dev app/main.py```

## Recommended Folder Structure (Not Official)

While there is no folder structure provided by fastapi and not recommend by them. But, we can structure our project directory in this way.

```
/app
├── main.py
├── core/
│   ├── config.py
│   ├── security.py
│   └── ...
├── api/
│   └── v1/
│       ├── endpoints/ (or routers/)
│       │   ├── users.py
│       │   └── items.py
│       └── ...
├── services/
│   ├── user_service.py
│   └── item_service.py
├── models/
│   ├── user.py
│   └── item.py
├── schemas/
│   ├── user.py
│   └── item.py
├── db/
│   ├── session.py
│   └── base.py
├── tests/
│   ├── test_users.py
│   └── test_items.py
└── utils/
```

## Using Pydantic with fastapi
FastAPI uses Pydantic's BaseModel to provide :

- automatic data validation
- serialization
- ensuring data integrity 
- reducing boilerplate code. 
- Conversion of input data: 
    coming from the network to Python data and types. Reading from: JSON., Path parameters, Query parameters, Cookies, Headers, Forms, Files.

- Conversion of output data: 
    converting from Python data and types to network data (as JSON): Convert Python types (str, int, float, bool, list, etc), datetime objects, UUID objects, Database models
- Automatic interactive API documentation, including 2 alternative user interfaces: Swagger UI, ReDoc.

By defining models with type hints, you create a clear contract for the data your API handles.

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.put("/items/{item_id}")
async def update_items(item_id: int, item: Item):
    return {"item_id ": item_id, "item": item}
```

## Dependencies
FastAPI depends on Pydantic and Starlette.

When you install FastAPI with pip install "fastapi[standard]" it comes with the standard group of optional dependencies:

- Used by Pydantic:
    - email-validator
- Used by Starlette:
    - httpx : Required if you want to use the TestClient.
    - jinja2 : Required if you want to use the default template configuration.
    - python-multipart : Required if you want to support form "parsing", with request.form().

- Used by FastAPI:
    - uvicorn : 
        for the server that loads and serves your application. This includes uvicorn[standard], which includes some dependencies (e.g. uvloop) needed for high performance serving.
    - fastapi-cli[standard] - to provide the fastapi command.
    
        This includes fastapi-cloud-cli, which allows you to deploy your FastAPI application to FastAPI Cloud.

### Pydantic vs dataclasses
The key difference is that Pydantic provides automatic runtime data validation and parsing, whereas standard dataclasses (from Python's built-in dataclasses module) are purely for reducing boilerplate code in data-holding classes and offer only static type checking.

## Features

- Based on open standards:
    OpenAPI for API creation, including declarations of path operations, parameters, request bodies, security, etc.

- Automatic docs : 
    - Swagger API
    - ReDoc
- Editor support
- Validation : 
    For almost data types and also for exotic types too (URL, Email, UUID)
- Security and authentication : 
    - HTTP Basic
    - OAuth2 (also with JWT tokens)
    - Plus all the security features from Starlette (including session cookies).
- Dependency Injection
- Unlimited "plug-ins"
- Starlette features : 
    FastAPI is actually a sub-class of Starlette.
    - WebSocket support.
    - In-process background tasks.
    - Startup and shutdown events.
    - Test client built on HTTPX.
    - CORS, GZip, Static Files, Streaming responses.
    - Session and Cookie support.
    - 100% test coverage.
    - 100% type annotated codebase.
- Pydantic features
    - Including external libraries also based on Pydantic, as ORMs, ODMs for databases.
    

## Dependency Injection
DI system is a core feature that automatically provides required components, such as database connections, authentication logic, or configuration settings, to your path operation functions.

### Key Benefits
- Improved Testability
- Code Reusability
- Modularity
- Automatic OpenAPI Integration

### How it Works
1. Define a "Dependable": 

    Create a function or a class that performs a specific task or returns a required object. This is your dependency.
    ```
    def get_db_session():
        # logic to create a database session
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    ```

2. Declare the Dependency: 

    In your path operation function, use Depends() with the dependency callable as a parameter's default value.
    ```
    from fastapi import Depends, FastAPI
    app = FastAPI()

    @app.get("/items/")
    def read_items(db_session: Session = Depends(get_db_session)):
        # Use the db_session here
        return {"message": "Using the database session"}
    ```

    FastAPI automatically detects this and injects the dependency's result before the endpoint's logic runs.

    With the Dependency Injection system, you can also tell FastAPI that your path operation function also "depends" on something else that should be executed before your path operation function, and FastAPI will take care of executing it and "injecting" the results.

### Share Annotated dependencies
In FastAPI, the typing.Annotated type is used with Depends() to declare and share dependencies with additional metadata, enabling better code reuse and editor support.

```
from typing import Annotated
from fastapi import Depends

def get_current_user() -> str:
    # logic to get current user
    return "John Doe"

# Define a reusable annotated type alias
CurrentUser = Annotated[str, Depends(get_current_user)]
```

Because we are using Annotated, we can store that Annotated value in a variable and use it in multiple places.

### To async or not to async
And you can declare dependencies with async def inside of normal def path operation functions, or def dependencies inside of async def path operation functions, etc.

It doesn't matter. FastAPI will know what to do.


## Middleware
Middleware in FastAPI is a way to process requests before they reach your route handlers and process responses before they are sent back to the client.

- It takes each request that comes to your application.
- It can then do something to that request or run any needed code.
- Then it passes the request to be processed by the rest of the application (by some path operation).
- It then takes the response generated by the application (by some path operation).
- It can do something to that response or run any needed code.
- Then it returns the response.

```
Client Request
      ↓
Middleware (before)
      ↓
Route Handler
      ↓
Middleware (after)
      ↓
Client Response
```

```python
# This middleware measures how long each request takes to process and attaches that time as a custom HTTP response header

from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### Order of Execution
Middleware executes in the order added

```python
app.add_middleware(MiddlewareA)
app.add_middleware(MiddlewareB)

Request → MiddlewareA → MiddlewareB → Route
Response ← MiddlewareB ← MiddlewareA
```

### Built-in Middlewares in FastAPI
- CORS Middleware
- GZip Middleware
- Trusted Host Middleware
- HTTPS Redirect Middleware


## CORS (Cross-Origin Resource Sharing)

Refers to the situations when a frontend running in a browser has JavaScript code that communicates with a backend, and the backend is in a different "origin" than the frontend.

#### Origin
An origin is the combination of protocol (http, https), domain (myapp.com, localhost, localhost.tiangolo.com), and port (80, 443, 8080).

To avoid CORS problem, backend must have a list of "allowed origins".

#### Wildcards
It's also possible to declare the list as "*" (a "wildcard") to say that all are allowed.

But that will only allow certain types of communication, excluding everything that involves credentials: Cookies, Authorization headers like those used with Bearer Tokens, etc.

### Use CORSMiddleware

- Import CORSMiddleware.
- Create a list of allowed origins (as strings).
- Add it as a "middleware" to your FastAPI application.

```python
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:8000/",
    "http://localhost:8000/"
    "http://localhost/",
    "http://127.0.0.1/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)
```

#### Supported Arguments

- allow_origins : 
    A list of origins that should be permitted to make cross-origin requests.

- allow_origin_regex 

- allow_methods : 
    A list of HTTP methods that should be allowed for cross-origin requests. Defaults to ['GET']. You can use ['*'] to allow all standard methods.

- allow_headers : 
    A list of HTTP request headers that should be supported for cross-origin requests. Defaults to []. You can use ['*'] to allow all headers. The Accept, Accept-Language, Content-Language and Content-Type headers are always allowed for simple CORS requests.

- allow_credentials : 
    Indicate that cookies should be supported for cross-origin requests. Defaults to False.

    None of allow_origins, allow_methods and allow_headers can be set to ['*'] if allow_credentials is set to True. All of them must be explicitly specified.

- expose_headers : 
    Indicate any response headers that should be made accessible to the browser. Defaults to [].

- max_age : 
    Sets a maximum time in seconds for browsers to cache CORS responses. Defaults to 600.


## Security

### OAuth2
OAuth2 is a specification that defines several ways to handle authentication and authorization.

It is quite an extensive specification and covers several complex use cases.

#### FastAPI class & methods:
- OAuth2PasswordBearer : 
    
    Create an instance of OAuth2PasswordBearer and specify the URL for obtaining a token.

- OAuth2PasswordRequestForm : 
    
    Simplifies implementing the OAuth2 password flow by extracting the username and password from form data in a POST request. 
    
    It is designed to work seamlessly with the "Authorize" button in the automatic Swagger UI documentation.


### OAuth1
OAuth 1 is very different from OAuth2, and more complex, as it included direct specifications on how to encrypt the communication. 

Not very popular or used nowadays.

OAuth2 doesn't specify how to encrypt the communication, it expects you to have your application served with HTTPS.

### OpenID Connect
OpenID Connect is another specification, based on OAuth2.

It just extends OAuth2 specifying some things that are relatively ambiguous in OAuth2, to try to make it more interoperable.

For example, Google login uses OpenID Connect (which underneath uses OAuth2).

### OpenAPI
OpenAPI (previously known as Swagger) is the open specification for building APIs (now part of the Linux Foundation).

FastAPI is based on OpenAPI.

That's what makes it possible to have multiple automatic interactive documentation interfaces, code generation, etc.

OpenAPI defines the following security schemes:
- apiKey
- http
- OAuth2
- openIdConnect

#### FastAPI utilities
FastAPI provides several tools for each of these security schemes in the fastapi.security module that simplify using these security mechanisms.

---

### JWT
JWT means "JSON Web Tokens". It's a standard to codify a JSON object in a long dense string without spaces.

It is not encrypted, so, anyone could recover the information from the contents.

A JWT consists of three parts, separated by dots (.)

```Header. Payload. Signature```
- Header: Contains metadata about the token, such as the algorithm used for signing.
- Payload: Stores the claims, i.e., data being transmitted.
- Signature: Ensures the token's integrity and authenticity.

    #### How JWT token Works?

    ![alt text](image.png)

#### Install PyJWT
We need to install PyJWT to generate and verify the JWT tokens in Python. ```pip install pyjwt```

#### Install pwdlib
pwdlib is a great Python package to handle password hashes. It supports many secure hashing algorithms and utilities to work with them.

The recommended algorithm is "Argon2". ```pip install "pwdlib[argon2]"```

---

### Using OAuth2 and JWT
When using OAuth2 + JWT in FastAPI:
- OAuth2 = defines how the client obtains and sends a token
- JWT = the actual token that proves who the user is

1. User Logs In (Authentication Step)

    Client sends:
    ```
    POST /token
    username=alice
    password=secret
    ```

    Server does:
    - Check username/password in database
    - If correct → create a JWT
    - Return the JWT as an OAuth2 access token

    Example response:
    ```
    {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
    }
    ```
    👉 This is authentication (proving identity).

2. Server Creates JWT

    The JWT contains:
    ```
    {
    "sub": "alice",
    "exp": 1712345678
    }
    ```

    Now the server can verify it later without database lookup.

3. Client Sends Token (Authorization Step)

    Client includes token in requests:
    ```
    Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    ```

    FastAPI reads it using:
    ```
    from fastapi.security import OAuth2PasswordBearer
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    ```

4. FastAPI Verifies JWT (Authentication Again)
    ```
    async def get_current_user(token: str = Depends(oauth2_scheme)):
    ```

    Then:
    - Decode JWT
    - Verify signature
    - Check expiration
    - Extract username
    - Load user from DB

    If valid → user is authenticated
    If invalid → 401 Unauthorized

    The JWT token payload may have user role which will tell us to protect routes from unauthorized users. This part is authorization.

##### Note : Generate SECRET_KEY using Bash : ```openssl rand -hex 32```

### Example

```python
# main.py
from fastapi import FastAPI, Request, Depends, HTTPException, status
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

        print("TOKEN:", token)
        print("SECRET:", settings.SECRET_KEY)
        print("PAYLOAD:", payload)

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

```

```
# .env
SECRET_KEY=4fbf4781604906c7698646ff4841974771886f6013de07391a2fddccef52c4ef
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

```python
# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

    model_config = SettingsConfigDict(
        env_file = ".env"
    )

@lru_cache
def get_settings():
    return Settings()
```


## Using env file in FastAPI
1. In the root directory of your project, create a file named .env and add your environment variables as key-value pairs (no spaces around the equals sign)

2. Define Settings in a Python File

    Create a configuration file (e.g., config.py) and use Pydantic's BaseSettings
    ```python
    # config.py
    from pydantic_settings import BaseSettings, SettingsConfigDict
    from functools import lru_cache

    class Settings(BaseSettings):
        database_url: str
        secret_key: str
        debug_mode: bool = False # Pydantic handles type conversion for bool

        model_config = SettingsConfigDict(
            env_file = ".env"
        )

    # Use lru_cache to create a single, cached instance of settings
    @lru_cache()
    def get_settings():
        return Settings()
    ```

3. Use Settings in Your FastAPI App 
    ```python
    # main.py
    from fastapi import FastAPI, Depends
    from .config import get_settings, Settings
    from typing import Annotated

    app = FastAPI()

    # Use dependency injection to access settings within a route (optional but recommended for testing)
    @app.get("/")
    def read_root(settings: Annotated[Settings, Depends(get_settings)]):
        return {
            "App Name": "My FastAPI App",
            "Debug Mode": settings.debug_mode,
            "Secret Key (partial)": settings.secret_key[:5] + "...",
        }

    # Alternatively, access settings directly (less testable)
    settings_direct = get_settings()
    @app.get("/direct")
    def read_direct():
        return {"Database URL": settings_direct.database_url}
    ```
---

## Background Tasks
Simple way to run tasks after returning a response to the client.

### Primary Uses of Background Tasks
- Sending Notifications/Emails: Sending a confirmation email or push notification after a user action (e.g., registration).
- Data Processing: Performing heavy computations, such as parsing large files or analyzing data, after receiving it.
- Logging and Auditing: Writing detailed logs or audit trails to a file or database without slowing down the primary response.
- External API Calls: Triggering third-party webhooks or API calls that might be slow or unstable.
- Cache Management: Updating or warming up cache data after a database update.

### Key Benefits
- Improved UI
- Non-Blocking Operations
- Simplicity

### How it works?
- Inject BackgroundTasks
- Add a task using .add_task()
- Return your response
- Task runs in background

### Example:
```python
from fastapi import FastAPI, BackgroundTasks

# bg tasks after send route
def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/send")
async def send_message(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Message sent!") # we can have multi args like the string sent
    return {"message": "Response sent immediately"}
```

#### Important Limitations

- BackgroundTasks:
    - Not persistent
    - Not distributed
    - Lost if server crashes
    - Runs in same process

- It is NOT for:
    - Heavy computation
    - Long-running tasks
    - Machine learning jobs
    - Video processing 


## Form Models

If not used "fastapi[standard]", then we have to do ```pip install python-multipart``` for using forms.

### Pydantic Models for Forms
```python
from pydantic import BaseModel

class FormData(BaseModel):
    username: str
    password: str

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]): # Accepts form data, validates it using a Pydantic model, and returns it.
    return data
```

### Forbid Extra Form Fields

In some special use cases, you might want to restrict the form fields to only those declared in the Pydantic model. And forbid any extra fields.

```python
class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}
```















