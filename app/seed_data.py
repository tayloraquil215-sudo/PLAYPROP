from db import SessionLocal
from models import PlayerStat

db = SessionLocal()

players = [
    {"player": "LeBron James", "stat": "Career PPG", "value": 27.1},
    {"player": "LeBron James", "stat": "Career RPG", "value": 7.5},
    {"player": "Stephen Curry", "stat": "Career 3PT%", "value": 42.8},
]

for p in players:
    db.add(PlayerStat(**p))

db.commit()
db.close()
