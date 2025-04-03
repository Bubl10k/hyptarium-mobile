from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Friendship(Base):
    __tablename__ = "friendship"

    user_id_1: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), primary_key=True
    )
    user_id_2: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), primary_key=True
    )

    user_1: Mapped["User"] = relationship(
        "User", foreign_keys=[user_id_1], back_populates="friendships"
    )
    user_2: Mapped["User"] = relationship(
        "User", foreign_keys=[user_id_2], back_populates="friendships"
    )
