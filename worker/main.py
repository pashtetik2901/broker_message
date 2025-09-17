from asyncio import exceptions
from consumer import logger, consumer
import asyncio
from aio_pika import connect_robust
from aio_pika.abc import AbstractChannel, AbstractQueue
from config import setting

async def main():
    await logger.info("Start worker")
    try:
        connection = await connect_robust(setting.URL_BROKER)
    except Exception as err:
        await logger.error(f"Error - {err}")
        await asyncio.sleep(2)
        return await main()
    
    async with connection:
        channel: AbstractChannel = await connection.channel()
        queue: AbstractQueue = await channel.declare_queue(
            setting.QUEUE_NAME,
            durable=True
        )
        await logger.info("Started consumer")
        
        while True:
            try:
                await consumer(queue)
            except Exception as err:
                await logger.error(f"Error - {err}")
                
if __name__ == "__main__":
    asyncio.run(main())