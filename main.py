from fastapi import FastAPI
from starlette.responses import FileResponse
from uvicorn import run

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World2"}

@app.get("/dl")
async def dl():
    return FileResponse('./txt_file.txt', filename='my_txt_file.txt')

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)