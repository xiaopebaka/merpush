from typing import Optional

from pydantic import BaseModel, Field

class MercariProduct(BaseModel):
    title: Optional[str] = Field(None, examples="有馬かな　アクリルスタンド")
    price: Optional[str] = Field(None, examples="1,500")
    description: Optional[str] = Field(None, examples="よろしくお願いします")