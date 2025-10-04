from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class ChannelCreate(BaseModel):
    owner_id: int
    external_id: str
    platform: str = "youtube"
    title: Optional[str] = None


class ChannelRead(BaseModel):
    id: int
    owner_id: int
    platform: str
    external_id: str
    title: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class VideoRead(BaseModel):
    id: int
    channel_id: int
    external_id: str
    title: Optional[str]
    description: Optional[str]
    thumbnail_url: Optional[str]
    has_captions: bool
    created_at: datetime

    class Config:
        from_attributes = True


class SummaryRead(BaseModel):
    id: int
    video_id: int
    summary_text: str
    hashtags: Optional[str]
    keywords: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


