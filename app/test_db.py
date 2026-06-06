from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import engine
from app.models.game import Game


game = Game(title="Doom Eternal", genre="Action")

# CREATE
with Session(engine) as session:
    try:
        session.add(game)
        session.commit()
        session.refresh(game)
        print(f"Saved game with id: {game.id}")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

#  READ
with Session(engine) as session:
    stmt = select(Game).where(Game.id == 5)
    result = session.execute(stmt)

    for game in result.scalars():
        print (game.title, game.genre)

# UPDATE
with Session(engine) as session:
    stmt = select(Game).where(Game.title == "Resident Evil")
    result = session.execute(stmt)

    for game in result.scalars():
            game.genre = "Survival Horror"
            print (game.title, game.genre)
    
    session.commit()

# DELETE
with Session(engine) as session:
     game = session.query(Game).filter_by(id=2).one_or_none()

     if game: 
        session.delete(game)
        session.commit()
     else:
        print("Game not founf")