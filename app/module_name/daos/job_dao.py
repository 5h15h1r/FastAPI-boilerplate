import pandas as pd
from app.db_session import db_connection

class JobDAO:
    def get_all_jobs(
        self, company_uuid, offset, limit, job_type, created_at, search_value
    ):
        db = db_connection()

        get_query = """SELECT j.uuid, j.name, j.created_at, j.job_type, j.job_status 
                    FROM job AS j
                    WHERE company_uuid = %s
                    """
        params = [company_uuid]

        if job_type:
            get_query += " AND j.job_type IN %s"
            params.append(tuple(job_type))

        if created_at:
            get_query += " AND j.created_at >= %s"
            params.append(created_at)

        if search_value:
            get_query += " AND (j.name LIKE %s OR j.job_type LIKE %s)"
            search_term = f"%{search_value}%"
            params.extend([search_term, search_term])

        # For PostgreSQL, use different placeholders
        get_query = get_query.replace("%s", "%s")

        if limit is not None:
            get_query += " LIMIT %s"
            params.append(limit)

        if offset is not None:
            get_query += " OFFSET %s"
            params.append(offset)

        try:
            df = pd.read_sql(get_query, db, params=params)
            return df, len(df)
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame(), 0
        finally:
            db.close()
            
    def get_job_by_uuid(self, job_uuid):
        db = db_connection()
        
        query = """SELECT uuid, name, created_at, job_type, job_status
                FROM job
                WHERE uuid = %s"""
                
        try:
            df = pd.read_sql(query, db, params=[job_uuid])
            return df.iloc[0] if not df.empty else None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            db.close() 