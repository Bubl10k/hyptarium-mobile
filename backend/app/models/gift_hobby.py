from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class GiftHobby(Base):
    __tablename__ = "gift_hobby"

    gift_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("gift.id"), primary_key=True
    )
    hobby: Mapped[str] = mapped_column(String(100), primary_key=True)

    gift: Mapped["Gift"] = relationship("Gift", back_populates="hobbies")
