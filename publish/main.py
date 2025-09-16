from config import logger
from model import RequestModel
from publisher import _publish_event
import asyncio

async def send_msg():
    data = RequestModel(
        status="old",
        name="Fedor",
        surname="Gurov"
    )
    
    await _publish_event(data)
    
    await logger.info("Message send")
    
if __name__ == "__main__":
    asyncio.run(send_msg())