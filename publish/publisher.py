from typing import Optional
from aio_pika import Message, connect_robust
from aio_pika.abc import DeliveryMode, AbstractChannel
from uuid import uuid4
from config import setting, logger
from model import RequestModel

def _create_message(data: bytes, message_id: Optional[str] = None):
    return Message(
        body=data,
        content_type="application/json",
        content_encoding="utf-8",
        message_id=message_id or uuid4().hex,
        delivery_mode=DeliveryMode.PERSISTENT,
        app_id=setting.APP_NAME
    )
    
async def _publish_event(data: RequestModel, message_id=None):
    connection = await connect_robust(setting.URL_BROKER)
    async with connection:
        channel = await connection.channel(publisher_confirms=True)
        exchange = await channel.declare_exchange("my_exchange", durable=False)
        message = _create_message(data.model_dump_json().encode(), message_id)
        routing_key = setting.QUEUE_NAME
        queue = await channel.declare_queue(setting.QUEUE_NAME, durable=True)
        await queue.bind(exchange=exchange, routing_key=routing_key)

        await logger.info("Start publishing message")
        await exchange.publish(message, routing_key=routing_key)
        await logger.info("Publish completed")

        