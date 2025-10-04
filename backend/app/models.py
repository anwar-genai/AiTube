from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship, Mapped
from .db import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    email: Mapped[str] = Column(String(255), unique=True, index=True, nullable=False)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow, nullable=False)
    channels = relationship("Channel", back_populates="owner")


class Channel(Base):
    __tablename__ = "channels"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    owner_id: Mapped[int] = Column(Integer, ForeignKey("users.id"), nullable=False)
    platform: Mapped[str] = Column(String(50), default="youtube", nullable=False)
    external_id: Mapped[str] = Column(String(255), index=True, nullable=False)
    title: Mapped[str] = Column(String(255), nullable=True)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow, nullable=False)

    owner = relationship("User", back_populates="channels")
    videos = relationship("Video", back_populates="channel")


class Video(Base):
    __tablename__ = "videos"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    channel_id: Mapped[int] = Column(Integer, ForeignKey("channels.id"), nullable=False)
    external_id: Mapped[str] = Column(String(255), index=True, nullable=False)
    title: Mapped[str] = Column(String(500), nullable=True)
    description: Mapped[str] = Column(Text, nullable=True)
    thumbnail_url: Mapped[str] = Column(String(500), nullable=True)
    has_captions: Mapped[bool] = Column(Boolean, default=False)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow, nullable=False)

    channel = relationship("Channel", back_populates="videos")
    summaries = relationship("Summary", back_populates="video")


class Summary(Base):
    __tablename__ = "summaries"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    video_id: Mapped[int] = Column(Integer, ForeignKey("videos.id"), nullable=False)
    summary_text: Mapped[str] = Column(Text, nullable=False)
    hashtags: Mapped[str] = Column(Text, nullable=True)
    keywords: Mapped[str] = Column(Text, nullable=True)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow, nullable=False)

    video = relationship("Video", back_populates="summaries")


