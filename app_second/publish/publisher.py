from aio_pika.abc import AbstractChannel, AbstractQueue
from aio_pika import Message, connect_robust
from publish.config import setting
from publish.model import TestModel
from uuid import uuid4
import logging

def _create_message(data: bytes):
    return Message(
        body=data,
        content_type="application/json",
        content_encoding="utf-8",
        message_id=uuid4().hex,
        app_id=setting.APP_NAME
    )

    
async def _publish_message(data: TestModel):
    connection = await connect_robust(setting.URL_BROKER)
    async with connection:
        channel: AbstractChannel = await connection.channel(publisher_confirms=True)
        queue: AbstractQueue = await channel.declare_queue(setting.QUEUE_NAME, durable=True)
        exchange = await channel.declare_exchange("my_exchange_second")
        routing_key = setting.QUEUE_NAME
        await queue.bind(exchange=exchange, routing_key=routing_key)
        msg = _create_message(data.model_dump_json().encode())
        await exchange.publish(message=msg, routing_key=routing_key)
        
        
async def send_new_msg(data: TestModel):
    logging.info("Start sending")
    await _publish_message(data)
    logging.info("End sending")