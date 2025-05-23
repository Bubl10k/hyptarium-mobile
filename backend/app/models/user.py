from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    birth_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=False)

    friendships: Mapped["Friendship"] = relationship(
        "Friendship",
        back_populates="user_1",
        foreign_keys="[Friendship.user_id_1]"
    )
    events: Mapped["Event"] = relationship("Event", back_populates="user")
