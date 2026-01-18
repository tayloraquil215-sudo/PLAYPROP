from db import SessionLocal
from models import PlayerStat

db = SessionLocal()

stats = [
    {"player":"LeBron James","stat":"Career PPG","value":27.1},
    {"player":"LeBron James","stat":"Career APG","value":7.4},
    {"player":"LeBron James","stat":"Career RPG","value":7.5},
]

for s in stats:
    db.add(PlayerStat(**s))

db.commit()
db.close()
