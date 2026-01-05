from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .board import Board

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    card_message: Mapped[str]
    likes: Mapped[Optional[int]] = mapped_column(default=0)
    


    @classmethod
    def from_dict(cls, card_data):
        new_card = Card(
            card_message = card_data["card_message"],
            likes = card_data.get("likes", 0) 
            )
        return new_card
    
    def to_dict(self) :
        result = {
            "id": self.id,
            "card_message": self.card_message,
            "likes": self.likes
        }
        return result

