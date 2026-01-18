from sqlalchemy import Column, String, Float, Integer
from db import Base
import uuid

def uid():
    return str(uuid.uuid4())

class Pick(Base):
    __tablename__ = "picks"

    id = Column(String, primary_key=True, default=uid)
    bet_type = Column(String)  # straight or parlay
    player = Column(String)
    market = Column(String)
    line = Column(Float)
    odds = Column(Integer)
    sportsbook = Column(String)
    stake = Column(Float)
    result = Column(String, default="pending")

class PlayerStat(Base):
    __tablename__ = "player_stats"

    id = Column(String, primary_key=True, default=uid)
    player = Column(String)
    stat = Column(String)
    value = Column(Float)
