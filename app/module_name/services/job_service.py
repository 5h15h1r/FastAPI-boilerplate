from datetime import datetime, timedelta
from fastapi import status
from app.module_name.daos.job_dao import JobDAO
from app.module_name.schemas.job_schema import Job, JobResponse, OperationStatusResponse

class JobService:
    def __init__(self):
        self.job_dao = JobDAO()
        
    def get_all_jobs(
        self, company_uuid, offset, limit, job_type, created_at, search_value
    ):
        date_filter_map = {
            "3_months": datetime.now() - timedelta(days=90),
            "6_months": datetime.now() - timedelta(days=180),
            "9_months": datetime.now() - timedelta(days=270),
            "1_year": datetime.now() - timedelta(days=365),
        }

        # Convert the selected filter to a date string
        created_at_date = date_filter_map.get(created_at, None)
        if created_at is not None and created_at not in list(date_filter_map.keys()):
            return OperationStatusResponse(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                message="Please enter a valid date filter",
            )
        created_at_str = (
            created_at_date.strftime("%Y-%m-%d") if created_at_date else None
        )

        job_df, job_count = self.job_dao.get_all_jobs(
            company_uuid=company_uuid,
            offset=offset,
            limit=limit,
            job_type=job_type,
            created_at=created_at_str,
            search_value=search_value,
        )

        if job_df.empty:
            return JobResponse(
                status=status.HTTP_404_NOT_FOUND,
                message="No jobs found",
                count=0,
                data=[],
            )

        job_obj = [
            Job(
                uuid=row["uuid"],
                name=row["name"],
                created_at=row["created_at"],
                job_status=row["job_status"],
                job_type=row.get("job_type", None)
            )
            for _, row in job_df.iterrows()
        ]

        return JobResponse(status=status.HTTP_200_OK, count=job_count, data=job_obj)
        
    def get_job_by_uuid(self, job_uuid):
        job_data = self.job_dao.get_job_by_uuid(job_uuid)
        
        if job_data is None:
            return JobResponse(
                status=status.HTTP_404_NOT_FOUND,
                message="Job not found",
                count=0,
                data=[]
            )
            
        job = Job(
            uuid=job_data["uuid"],
            name=job_data["name"],
            created_at=job_data["created_at"],
            job_status=job_data["job_status"],
            job_type=job_data.get("job_type", None)
        )
        
        return JobResponse(
            status=status.HTTP_200_OK,
            message="Job retrieved successfully",
            count=1,
            data=[job]
        ) 