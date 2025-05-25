from fastapi import APIRouter, HTTPException
from app.module_name.services.job_service import ItemService

router = APIRouter(prefix="/api/v1.0", tags=["Items"])
item_service = ItemService()

@router.get("/items")
def get_all_items():
    return item_service.get_all_items()

@router.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    item = item_service.get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item 