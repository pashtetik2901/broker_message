from publish.config import logger
from publish.model import RequestModel
from publish.publisher import _publish_event
import asyncio

async def send_msg(data: RequestModel):

    await _publish_event(data)
    
    await logger.info("Message send")
    
# if __name__ == "__main__":
#     asyncio.run(send_msg())