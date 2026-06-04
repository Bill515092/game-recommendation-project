from sqlalchemy.orm import Session
from app.core.database import engine
from app.models.game import Game


game = Game(title="Resident Evil", genre="Horror")

with Session(engine) as session:
    try:
        session.add(game)
        session.commit()
        session.refresh(game)
        print(f"Saved game with id: {game.id}")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")