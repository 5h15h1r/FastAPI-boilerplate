from datetime import datetime, timedelta
from app.module_name.daos.job_dao import ItemDAO
from app.module_name.schemas.job_schema import Item, ItemResponse



class ItemService:
    def __init__(self):
        self.item_dao = ItemDAO()

    def get_all_items(self):
        df = self.item_dao.get_all_items()
        if df.empty:
            return ItemResponse(status=404, message="No items found", count=0, data=[])
        items = [Item(**row) for row in df.to_dict(orient="records")]
        return ItemResponse(status=200, message="Success", count=len(items), data=items)

    def get_item_by_id(self, item_id):
        df = self.item_dao.get_item_by_id(item_id)
        if df.empty:
            return ItemResponse(status=404, message="Item not found", count=0, data=[])
        item = Item(**df.iloc[0].to_dict())
        return ItemResponse(status=200, message="Success", count=1, data=[item]) 