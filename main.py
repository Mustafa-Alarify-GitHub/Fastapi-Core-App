from fastapi import FastAPI
from contextlib import asynccontextmanager

# from core.apps import create_main_app
from core.db import check_database_connection
from core.env_manager import EnvManager
from apps.book.main import book_app
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting application...")
    await check_database_connection()
    yield
    print("Shutting down application...")


# main_app = create_main_app()
main_app = FastAPI(title="Main app", lifespan=lifespan)


# Optionally add a root route
@main_app.get("/")
def root():
    return {"message": "Main Application is running!"}


main_app.mount("/book", book_app, "Book")

if __name__ == "__main__":
    uvicorn.run(
        app=main_app,
        host=EnvManager.get("HOST", "0.0.0.0"),
        port=int(EnvManager.get("PORT", "8000")),
    )
