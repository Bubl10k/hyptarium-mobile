from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Wishlist(Base):
    __tablename__ = "wishlist"

    user_id_1: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), primary_key=True)
    gift_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("gift.id"), primary_key=True)
    user_id_2: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), nullable=True)
    is_taken: Mapped[bool] = mapped_column(Boolean, default=False)

    user_1: Mapped["User"] = relationship("User", foreign_keys=[user_id_1])
    user_2: Mapped["User"] = relationship("User", foreign_keys=[user_id_2])
    gift: Mapped["Gift"] = relationship("Gift", back_populates="wishlists")
