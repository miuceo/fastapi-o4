import uvicorn
from fastapi import FastAPI

from api import student_router, group_router

app = FastAPI()
app.include_router(student_router)
app.include_router(group_router)

@app.get("/")
def main():
    return {
        "message": "Hello from FastAPI!",
    }
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=4506, reload=True)