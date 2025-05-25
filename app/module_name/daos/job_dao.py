import pandas as pd
from app.db_session import db_connection

class ItemDAO:
    def get_all_items(self):
        db = db_connection()
        query = "SELECT id, name, description, created_at FROM items"
        try:
            df = pd.read_sql(query, db)
            return df
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()
        finally:
            db.close()

    def get_item_by_id(self, item_id):
        db = db_connection()
        query = "SELECT id, name, description, created_at FROM items WHERE id = %s"
        try:
            df = pd.read_sql(query, db, params=[item_id])
            return df
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()
        finally:
            db.close() 