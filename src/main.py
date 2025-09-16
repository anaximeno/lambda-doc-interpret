from fastapi import FastAPI
from mangum import Mangum

from routes import extract

app = FastAPI()
app.include_router(extract.router)

lambda_handler = Mangum(app)
