from typing import List
from fastapi import APIRouter
import model.MercariProduct as MercariProduct

router = APIRouter()

@router.get("/getMercariProducts/{keyword}", response_model=List[MercariProduct.MercariProduct])
async def getMercariProducts():
    return [MercariProduct.MercariProduct(title="推しの子有馬かなアクリルスタンド", price="2,000", description="こんにちは")]
