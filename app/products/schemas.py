from pydantic import BaseModel


class SProduct(BaseModel):
    id: int
    title: str
    description: str
    price: int
    amount: int