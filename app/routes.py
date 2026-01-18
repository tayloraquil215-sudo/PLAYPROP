from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Pick, PlayerStat
import pandas as pd
import io
from fastapi.responses import StreamingResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pick")
def add_pick(pick: dict, db: Session = Depends(get_db)):
    p = Pick(**pick)
    db.add(p)
    db.commit()
    return p

@router.get("/history")
def history(db: Session = Depends(get_db)):
    return db.query(Pick).all()

@router.get("/stats")
def stats(db: Session = Depends(get_db)):
    wins = db.query(Pick).filter(Pick.result=="win").count()
    losses = db.query(Pick).filter(Pick.result=="loss").count()
    return {"wins": wins, "losses": losses}

@router.get("/players/{name}")
def player_stats(name: str, db: Session = Depends(get_db)):
    return db.query(PlayerStat).filter(PlayerStat.player == name).all()

@router.get("/export")
def export_csv(db: Session = Depends(get_db)):
    data = db.query(Pick).all()
    df = pd.DataFrame([d.__dict__ for d in data]).drop("_sa_instance_state", axis=1)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)
    return StreamingResponse(stream, media_type="text/csv")
