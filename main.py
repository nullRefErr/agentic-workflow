from fastapi import FastAPI

from routers import router

app = FastAPI()
app.include_router(router.router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}