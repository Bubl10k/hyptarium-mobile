from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Friendship(Base):
    __tablename__ = "friendship"

    user_id_1: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), primary_key=True
    )
    user_id_2: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), primary_key=True
    )
