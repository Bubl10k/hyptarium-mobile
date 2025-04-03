from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.setup import get_session
from app.models.events import Event
from app.models.friendship import Friendship
from app.models.gift import Gift
from app.models.user import User
from app.models.wishlist import Wishlist

router = APIRouter(
    prefix="/test",
    tags=["test creation"],
)


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    birth_date: datetime
    bio: str


class GiftCreate(BaseModel):
    name: str
    cost: float
    description: str
    link: str
    age: int
    gender: str
    price: float


class WishlistCreate(BaseModel):
    user_id_1: int
    gift_id: int
    user_id_2: int = None
    is_taken: bool = False


class FriendshipCreate(BaseModel):
    user_id_1: int
    user_id_2: int


class EventCreate(BaseModel):
    user_id_1: int
    date: datetime
    name: str


@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        birth_date=user.birth_date,
        bio=user.bio
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/gifts/")
def create_gift(gift: GiftCreate, db: Session = Depends(get_session)):
    db_gift = Gift(
        name=gift.name,
        cost=gift.cost,
        description=gift.description,
        link=gift.link,
        age=gift.age,
        gender=gift.gender,
        price=gift.price
    )
    db.add(db_gift)
    db.commit()
    db.refresh(db_gift)
    return db_gift


@router.post("/wishlists/")
def create_wishlist(wishlist: WishlistCreate, db: Session = Depends(get_session)):
    db_wishlist = Wishlist(
        user_id_1=wishlist.user_id_1,
        gift_id=wishlist.gift_id,
        user_id_2=wishlist.user_id_2,
        is_taken=wishlist.is_taken
    )
    db.add(db_wishlist)
    db.commit()
    db.refresh(db_wishlist)
    return db_wishlist


@router.post("/friendships/")
def create_friendship(friendship: FriendshipCreate, db: Session = Depends(get_session)):
    db_friendship = Friendship(
        user_id_1=friendship.user_id_1,
        user_id_2=friendship.user_id_2
    )
    db.add(db_friendship)
    db.commit()
    db.refresh(db_friendship)
    return db_friendship


@router.post("/events/")
def create_event(event: EventCreate, db: Session = Depends(get_session)):
    db_event = Event(
        user_id_1=event.user_id_1,
        date=event.date,
        name=event.name
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
