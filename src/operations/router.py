import time
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from database import get_async_session

from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operation",
    tags=["Operations"]
)

@router.get("/long_operations")
@cache(expire=30)
def get_long_operation():
    time.sleep(2)
    return "Много данных"

@router.get("/get_operation",response_model=list[OperationCreate])
async def get_specific_operations(operation_type: str,session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return result.mappings().all()
        
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status":"error",
            "data": None,
            "details": "Что-то пошло не так"
        })
        


@router.post("/create_operation")
async def add_specific_operations(new_operation: OperationCreate,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status":"success"}