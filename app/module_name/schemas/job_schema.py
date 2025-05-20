from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import status
from datetime import datetime
from uuid import UUID


class Job(BaseModel):
    uuid: str
    name: str
    created_at: datetime
    job_status: str
    job_type: Optional[str] = None


class JobResponse(BaseModel):
    status: int = status.HTTP_200_OK
    message: str = "Success"
    count: int = 0
    data: List[Job] = []


class OperationStatusResponse(BaseModel):
    status: int = status.HTTP_200_OK
    message: str = "Success" 