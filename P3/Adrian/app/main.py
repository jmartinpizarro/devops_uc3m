from fastapi import FastAPI
from app.presentation.api.users import router as user_router
from app.presentation.api.tickets import router as ticket_router

app = FastAPI(
    title="Ticket Management API",
    description="API for managing users and tickets",
    version="1.0.0",
    docs_url="/docs"
)

app.include_router(user_router)
app.include_router(ticket_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Ticket Management API"}