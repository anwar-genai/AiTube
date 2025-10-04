from ..celery_app import celery_app
from .utils import get_logger


logger = get_logger(__name__)


@celery_app.task(name="summarization.run")
def run_summarization(video_id: str, transcript: str) -> dict:
    logger.info(f"Summarizing transcript for {video_id}")
    # LangGraph pipeline stub
    summary = {
        "summary_text": "",
        "hashtags": "",
        "keywords": "",
    }
    return {"video_id": video_id, **summary}


