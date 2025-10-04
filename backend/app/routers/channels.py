from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas


router = APIRouter()


@router.get("/", response_model=list[schemas.ChannelRead])
def list_channels(db: Session = Depends(get_db)):
    channels = db.query(models.Channel).order_by(models.Channel.created_at.desc()).all()
    return channels


@router.post("/", response_model=schemas.ChannelRead)
def add_channel(payload: schemas.ChannelCreate, db: Session = Depends(get_db)):
    # Create default user if it doesn't exist
    user = db.query(models.User).filter(models.User.id == payload.owner_id).first()
    if not user:
        user = models.User(
            id=payload.owner_id,
            email=f"user{payload.owner_id}@example.com"
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
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


