from sqlalchemy import Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Gift(Base):
    __tablename__ = "gift"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    cost: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    link: Mapped[str] = mapped_column(String(500), nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    gender: Mapped[str] = mapped_column(String(50), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=True)

    wishlists: Mapped["Wishlist"] = relationship(
        "Wishlist", back_populates="gift")
    hobbies: Mapped["GiftHobby"] = relationship(
        "GiftHobby", back_populates="gift")
