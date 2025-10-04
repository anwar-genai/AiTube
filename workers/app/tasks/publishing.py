from ..celery_app import celery_app
from .utils import get_logger


logger = get_logger(__name__)


@celery_app.task(name="publishing.run")
def run_publishing(video_id: str, summary_text: str, hashtags: str, keywords: str) -> dict:
    logger.info(f"Publishing summary for {video_id}")
    # DB write + notifications stub
    return {"ok": True}


