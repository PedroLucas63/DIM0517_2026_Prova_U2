from fastapi import FastAPI

app = FastAPI()
print("Bem vindo ao projeto!")

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/healthy")
def healthy():
    return {"status": "healthy"}
