from fastapi import FastAPI
from routers import book, user, file, apidb
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book.router)
app.include_router(user.router)
app.include_router(file.router)
app.include_router(apidb.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
