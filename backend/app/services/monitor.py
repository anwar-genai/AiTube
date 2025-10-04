"""
Automatic channel monitoring service
"""
from typing import List
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models
from .youtube import list_channel_uploads, fetch_captions
# Import tasks from workers (these will be called via Celery)
# from ..tasks.transcription import run_transcription
# from ..tasks.summarization import run_summarization  
# from ..tasks.publishing import run_publishing
import logging

logger = logging.getLogger(__name__)


def monitor_all_channels():
    """Monitor all tracked channels for new videos"""
    db = next(get_db())
    
    try:
        # Get all tracked channels
        channels = db.query(models.Channel).all()
        logger.info(f"Monitoring {len(channels)} channels")
        
        for channel in channels:
            try:
                monitor_channel(channel, db)
            except Exception as e:
                logger.error(f"Error monitoring channel {channel.title}: {e}")
                
    except Exception as e:
        logger.error(f"Error in monitor_all_channels: {e}")
    finally:
        db.close()


def monitor_channel(channel: models.Channel, db: Session):
    """Monitor a specific channel for new videos"""
    logger.info(f"Monitoring channel: {channel.title}")
    
    # Fetch recent videos from YouTube
    videos = list_channel_uploads(channel.external_id, max_results=5)
    logger.info(f"Found {len(videos)} recent videos")
    
    for video_data in videos:
        # Check if video already exists
        existing_video = db.query(models.Video).filter(
            models.Video.external_id == video_data["video_id"]
        ).first()
        
        if existing_video:
            logger.info(f"Video {video_data['video_id']} already exists, skipping")
            continue
        
        # Create new video record
        video = models.Video(
            channel_id=channel.id,
            external_id=video_data["video_id"],
            title=video_data["title"],
            description=video_data["description"],
            thumbnail_url=video_data["thumbnail"]
        )
        
        db.add(video)
        db.commit()
        db.refresh(video)
        
        logger.info(f"Added new video: {video.title}")
        
        # Start processing pipeline
        process_video_async(video.id, video_data["video_id"])


def process_video_async(video_id: int, youtube_video_id: str):
    """Start async processing of a video"""
    logger.info(f"Starting processing for video {youtube_video_id}")
    
    # Try to get captions first
    captions = fetch_captions(youtube_video_id)
    
    if captions:
        # If captions available, use them directly
        logger.info("Using YouTube captions")
        transcript = captions
        # TODO: Start summarization via Celery task
        logger.info(f"Would start summarization for {youtube_video_id}")
    else:
        # If no captions, start transcription
        logger.info("No captions found, starting transcription")
        # TODO: Start transcription via Celery task
        logger.info(f"Would start transcription for {youtube_video_id}")


def get_channel_stats(channel_id: int) -> dict:
    """Get statistics for a channel"""
    db = next(get_db())
    
    try:
        channel = db.query(models.Channel).filter(models.Channel.id == channel_id).first()
        if not channel:
            return {"error": "Channel not found"}
        
        video_count = db.query(models.Video).filter(models.Video.channel_id == channel_id).count()
        summary_count = db.query(models.Summary).join(models.Video).filter(
            models.Video.channel_id == channel_id
        ).count()
        
        return {
            "channel_title": channel.title,
            "total_videos": video_count,
            "summarized_videos": summary_count,
            "processing_rate": f"{(summary_count/video_count*100):.1f}%" if video_count > 0 else "0%"
        }
        
    except Exception as e:
        logger.error(f"Error getting channel stats: {e}")
        return {"error": str(e)}
    finally:
        db.close()
