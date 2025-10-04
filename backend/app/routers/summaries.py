from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas


router = APIRouter()


@router.get("/", response_model=list[schemas.SummaryRead])
def list_summaries(db: Session = Depends(get_db)):
    summaries = (
        db.query(models.Summary)
        .order_by(models.Summary.created_at.desc())
        .limit(100)
        .all()
    )
    return summaries


