from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Wishlist(Base):
    __tablename__ = "wishlist"

    user_id_1: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), primary_key=True)
    gift_id: Mapped[int] = mapped_column(Integer, ForeignKey("gift.id"), primary_key=True)
    user_id_2: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=True)
    is_taken: Mapped[bool] = mapped_column(Boolean, default=False)
