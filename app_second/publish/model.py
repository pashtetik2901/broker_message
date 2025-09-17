from pydantic import BaseModel
from datetime import datetime

class TestModel(BaseModel):
    name: str
    cost: float
    count: int
    create_at: str = datetime.now().strftime("%d.%m.%Y")