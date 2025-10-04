from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas


router = APIRouter()


@router.get("/", response_model=list[schemas.VideoRead])
def list_videos(db: Session = Depends(get_db)):
    videos = db.query(models.Video).order_by(models.Video.created_at.desc()).limit(100).all()
    return videos


