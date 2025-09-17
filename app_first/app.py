from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from publish.main import send_msg
from publish.model import RequestModel
import uvicorn

app = FastAPI()


@app.post("/send")
async def send(data: RequestModel):
    try:
        await send_msg(data)
        return {
            "status": True
        }
    except Exception as err:
        print(f'Error - {err}')
        return {
            "status": False
        }

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)