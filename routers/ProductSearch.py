from fastapi import APIRouter

router = APIRouter()

@router.get("/getMercariProducts/{keyword}")
async def getMercariProducts():
    pass
