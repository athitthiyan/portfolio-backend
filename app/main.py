from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import project_routes, contact_routes
from app.db.database import engine, Base
from app.models import project, contact  # noqa: F401 — registers models with Base

app = FastAPI()

# CORS — allow_credentials=True is incompatible with allow_origins=["*"]
# Using specific origins instead
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables if they don't exist in Supabase yet
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Warning: Could not create tables on startup: {e}")

# Routes
app.include_router(project_routes.router)
app.include_router(contact_routes.router)
