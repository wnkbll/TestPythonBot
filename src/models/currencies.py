from pydantic import BaseModel


class Currency(BaseModel):
    NumCode: str
    CharCode: str
    Nominal: str
    Name: str
    Value: float
    VunitRate: float
