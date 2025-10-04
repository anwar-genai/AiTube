from .utils import get_logger
from ..celery_app import celery_app


logger = get_logger(__name__)


@celery_app.task(name="transcription.run")
def run_transcription(video_id: str, audio_url: str) -> dict:
    logger.info(f"Transcribing video {video_id} from {audio_url}")
    # Whisper integration stub
    transcript = ""  # replace with real transcript
    return {"video_id": video_id, "transcript": transcript}


