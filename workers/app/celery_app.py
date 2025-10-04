import os
from celery import Celery


redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "aitube",
    broker=redis_url,
    backend=redis_url,
    include=[
        "app.tasks.transcription",
        "app.tasks.summarization",
        "app.tasks.publishing",
    ],
)


