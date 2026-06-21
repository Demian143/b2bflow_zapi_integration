from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/add_user_number")
def add_user_number():
    ...

@app.post("/send_default_message")
def send_default_message():
    ...