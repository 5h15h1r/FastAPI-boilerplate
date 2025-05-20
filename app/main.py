from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.app_config import get_config
from app.module_name.routers import job_router

app = FastAPI(title="Dummy API", version="0.1.0")

# Configure CORS
config = get_config()
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=config.ALLOWED_METHODS,
    allow_headers=config.ALLOWED_HEADERS,
)

# Include routers
app.include_router(job_router.router, prefix="/api", tags=["jobs"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
