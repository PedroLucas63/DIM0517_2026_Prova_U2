from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/healthy")
def healthy():
    return {"status": "healthy"}

@app.get("/remove")
def remove():
    return {"remove:" "system32"}

@app.get("/install")
def remove():
    return {"install:" "arch"}
