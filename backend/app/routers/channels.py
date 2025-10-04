from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas


router = APIRouter()


@router.post("/", response_model=schemas.ChannelRead)
def add_channel(payload: schemas.ChannelCreate, db: Session = Depends(get_db)):
    exists = (
        db.query(models.Channel)
        .filter(models.Channel.owner_id == payload.owner_id)
        .filter(models.Channel.external_id == payload.external_id)
        .first()
    )
    if exists:
        raise HTTPException(status_code=400, detail="Channel already tracked")
    channel = models.Channel(
        owner_id=payload.owner_id,
        external_id=payload.external_id,
        platform=payload.platform,
        title=payload.title,
    )
    db.add(channel)
    db.commit()
    db.refresh(channel)
    return channel


@router.delete("/{channel_id}")
def remove_channel(channel_id: int, db: Session = Depends(get_db)):
    channel = db.query(models.Channel).filter(models.Channel.id == channel_id).first()
    if not channel:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(channel)
    db.commit()
    return {"ok": True}


