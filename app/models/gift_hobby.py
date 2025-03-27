from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class GiftHobby(Base):
    __tablename__ = "gift_hobby"

    gift_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("gift.id"), primary_key=True
    )
    hobby: Mapped[str] = mapped_column(String(100), primary_key=True)
