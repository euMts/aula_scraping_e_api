from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError
from datetime import datetime as dt
from starlette.responses import JSONResponse
from starlette.requests import Request
from methods import Utils

# run: $ uvicorn main:app --host 0.0.0.0 --port 8080 --reload

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Form(BaseModel):
    name: str
    email: str
    message: str

@app.exception_handler(ValidationError)
async def handler1(request: Request, exc: Exception):
    print("ValidationError")
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=dict(exc))

@app.exception_handler(RequestValidationError)
async def handler2(request: Request, exc: Exception):
    print("RequestValidationError")
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=dict(exc))

@app.exception_handler(Exception)
async def handler3(request: Request, exc: Exception):
    print("Exception")
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=dict(exc))

@app.get("/")
def root():
    return {"status":"Im alive!!! 🚀", "datetime":str(dt.now())}

@app.post("/api/contact/")
async def create_user(item: Form):
    try:
        insertion = Utils(item.name, item.email, item.message).return_content
        if insertion["status"] == "Ok":
            return_item = {
                "status":"200",
                "message":str(insertion["message"])
            }
            print(return_item)
            return JSONResponse(status_code=status.HTTP_200_OK, content=return_item)
        else:
            return_item = {
                "status":"500",
                "message":str(insertion["message"])
            }
            print(return_item)
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=return_item)
    except Exception as e:
        return_item = {
            "status":"500",
            "message":e
        }
        print(return_item)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=return_item)