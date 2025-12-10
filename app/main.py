import asyncio

from app.kafka.repositories.kafka_repositories import KafkaRepository
from app.gateway.gRPC.server import serve

async def main():
    kf = KafkaRepository()
    await kf.wait_kafka()
    kafka_task = asyncio.create_task(kf.get_message("delete", "post-service"))
    gateway_task = asyncio.create_task(serve())
    await asyncio.gather(kafka_task,gateway_task)
    

if __name__ == "__main__":
    asyncio.run(main())