from fastapi import FastAPI
from app.routers import users, tickets

app = FastAPI(title="Ticket Management API", docs_url="/docs")

app.include_router(users.router)
app.include_router(tickets.router)
