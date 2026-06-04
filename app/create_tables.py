from app.core.database import Base, engine
from app.models.game import Game

Base.metadata.create_all(engine)