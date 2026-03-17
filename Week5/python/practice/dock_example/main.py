from fastapi import FastAPI

app = FastAPI(
    title="Docker is all about containerization"
)

@app.get("/")
def greet_user():
    return "Hello"