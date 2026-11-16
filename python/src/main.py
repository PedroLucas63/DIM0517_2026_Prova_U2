from fastapi import FastAPI

app = FastAPI()
print("Você é bem vindo a nossa aplicação!")

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/healthy")
def healthy():
    return {"status": "healthy"}

@app.get("/remove")
def remove():
    return {"remove": "system32"}

@app.get("/install")
def remove():
    return {"install": "arch"}
