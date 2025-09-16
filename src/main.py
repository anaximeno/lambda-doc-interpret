from fastapi import FastAPI
from mangum import Mangum

from routes import test

app = FastAPI()
app.include_router(test.router)

lambda_handler = Mangum(app)