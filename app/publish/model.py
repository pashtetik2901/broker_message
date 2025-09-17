from pydantic import BaseModel
from datetime import datetime

class RequestModel(BaseModel):
    status: str
    name: str
    surname: str
    create_date: str = datetime.now().strftime("%d.%m.%Y")
    