import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from config.app_config import get_config
from app.module_name.routers import job_router
from app.global_utilities.functions.request_validation import register_exception_handlers
import logging

# Disable specific Uvicorn loggers
loggers_to_disable = [
    "uvicorn",          # General logs including shutdown/startup
    "uvicorn.error",    # Error-level logs
    "uvicorn.access"    # Access logs (every request log)
]

for logger_name in loggers_to_disable:
    logger = logging.getLogger(logger_name)
    logger.disabled = True

# Configure FastAPI app based on environment
if get_config().APP_ENV == "PROD":
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
    print("Running in PRODUCTION mode")
elif get_config().APP_ENV == "DEV":
    app = FastAPI()
    print("Running in DEVELOPMENT mode")
else:
    app = FastAPI()
    print("Running in DEFAULT mode")

# Configure CORS
origins = get_config().ALLOWED_ORIGINS
methods = get_config().ALLOWED_METHODS
headers = get_config().ALLOWED_HEADERS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

# Register exception handlers


# Include routers
app.include_router(job_router.router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Boilerplate"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="info")
