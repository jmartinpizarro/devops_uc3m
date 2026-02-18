from fastapi import FastAPI
from ticket_management.api.v1.routers import users, tickets

app = FastAPI(title="Ticket Management API", version="1.0")

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(tickets.router, prefix="/api/v1/tickets", tags=["tickets"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ticket Management API"}