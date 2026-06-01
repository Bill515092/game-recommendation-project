from app.core.database import Base
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped


class Game(Base):
    __tablename__ = "games"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    genre: Mapped[str] = mapped_column(String(30))
    