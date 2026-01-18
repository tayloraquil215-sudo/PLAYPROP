import matplotlib.pyplot as plt
from sqlalchemy.orm import Session
from models import Pick

def win_loss_chart(db: Session):
    wins = db.query(Pick).filter(Pick.result == "win").count()
    losses = db.query(Pick).filter(Pick.result == "loss").count()

    plt.bar(["Wins", "Losses"], [wins, losses])
    plt.title("Win / Loss Chart")
    plt.show()

def odds_line_chart(db: Session):
    picks = db.query(Pick).all()
    odds = [p.odds for p in picks if p.odds]
    plt.plot(odds)
    plt.title("Odds Trend")
    plt.show()

def bet_type_pie(db: Session):
    straight = db.query(Pick).filter(Pick.bet_type == "straight").count()
    parlay = db.query(Pick).filter(Pick.bet_type == "parlay").count()

    plt.pie([straight, parlay], labels=["Straight", "Parlay"], autopct="%1.1f%%")
    plt.title("Bet Types")
    plt.show()
