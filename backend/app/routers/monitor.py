from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models
from ..services.monitor import monitor_all_channels, get_channel_stats
from ..services.youtube import list_channel_uploads
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/monitor/start")
def start_monitoring():
    """Start monitoring all channels for new videos"""
    try:
        monitor_all_channels()
        return {"status": "success", "message": "Monitoring started"}
    except Exception as e:
        logger.error(f"Error starting monitoring: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/monitor/channels/{channel_id}/videos")
def get_channel_videos(channel_id: int, db: Session = Depends(get_db)):
    """Get recent videos from a specific channel"""
    channel = db.query(models.Channel).filter(models.Channel.id == channel_id).first()
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    try:
        # Fetch videos from YouTube API
        videos = list_channel_uploads(channel.external_id, max_results=10)
        return {
            "channel_title": channel.title,
            "videos": videos
        }
    except Exception as e:
        logger.error(f"Error fetching channel videos: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/monitor/channels/{channel_id}/stats")
def get_channel_statistics(channel_id: int):
    """Get statistics for a channel"""
    stats = get_channel_stats(channel_id)
    if "error" in stats:
        raise HTTPException(status_code=404, detail=stats["error"])
    return stats


@router.post("/monitor/channels/{channel_id}/process")
def process_channel_videos(channel_id: int, db: Session = Depends(get_db)):
    """Manually trigger processing for a specific channel"""
    channel = db.query(models.Channel).filter(models.Channel.id == channel_id).first()
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    try:
        from ..services.monitor import monitor_channel
        monitor_channel(channel, db)
        return {"status": "success", "message": f"Processing started for {channel.title}"}
    except Exception as e:
        logger.error(f"Error processing channel: {e}")
        raise HTTPException(status_code=500, detail=str(e))
