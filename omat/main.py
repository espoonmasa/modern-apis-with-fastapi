from typing import Optional 
import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/hello')
def hello(name: str, age: Optional[int] = None ):
    if name == "":
        return fastapi.responses.JSONResponse(
                content={"error": "ERROR: name cannot be null."},
                status_code=400)
    elif age:
        return fastapi.responses.JSONResponse(
                content={"greeting": f"Hello {name}, you're {age} year!"},
                status_code=200)
    else:
        return fastapi.responses.JSONResponse(
                content={"greeting": f"Hello {name}!"},
                status_code=200)

uvicorn.run(api)