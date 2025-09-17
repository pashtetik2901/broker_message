from aio_pika import IncomingMessage
from aiologger import Logger
import asyncio
import json
from config import logger

async def consumer(queue):
    message: IncomingMessage
    async for message in queue:
        async with message.process():
            context = {
                "service_name": message.app_id,
                "task_id": message.message_id
            }
            await logger.info("Message is being processing")
            data = json.loads(message.body.decode())
            
            print(data)
            print(context)
            
            await logger.info("Message was processed")
            