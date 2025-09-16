from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
lambda_handler = Mangum(app)

@app.get("/hello")
async def get_root():
    return {"Hello": "World"}


@app.get("/test")
async def get_test():
    return {"hell": "yeah"}
