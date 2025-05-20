from fastapi import APIRouter, Request, Query, Path, Depends
from typing import List, Optional
from app.module_name.services.job_service import JobService
from app.module_name.schemas.job_schema import JobResponse

router = APIRouter()
job_service = JobService()

@router.get("/jobs/{company_uuid}", response_model=JobResponse)
async def get_all_jobs(
    request: Request,
    company_uuid: str = Path(..., description="Company UUID"),
    offset: Optional[int] = Query(None, description="Number of records to skip"),
    limit: Optional[int] = Query(None, description="Number of records to return"),
    job_type: Optional[List[str]] = Query([], description="Filter by job type"),
    created_at: Optional[str] = Query(
        None, description="Filter by: 3_months, 6_months, 9_months, 1_year"
    ),
    search_value: Optional[str] = Query(None, description="Search by name or job type"),
):
    """
    Get all jobs for a company with optional filters
    """
    response = job_service.get_all_jobs(
        company_uuid=company_uuid,
        offset=offset,
        limit=limit,
        job_type=job_type,
        created_at=created_at,
        search_value=search_value,
    )
    return response

@router.get("/job/{job_uuid}", response_model=JobResponse)
async def get_job_by_uuid(
    request: Request,
    job_uuid: str = Path(..., description="Job UUID"),
):
    """
    Get job details by UUID
    """
    return job_service.get_job_by_uuid(job_uuid) 