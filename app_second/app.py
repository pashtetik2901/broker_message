from fastapi import FastAPI
from publish.model import TestModel
from publish.publisher import send_new_msg
import uvicorn

app = FastAPI()

@app.post("/send")
async def send(data: TestModel):
    await send_new_msg(data)
    return {
        "status": "Отправлено"
    }


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)