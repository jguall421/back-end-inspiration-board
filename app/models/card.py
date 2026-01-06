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
    board_id: Mapped[Optional[int]] = mapped_column(ForeignKey("board.id"))
    board: Mapped[Optional["Board"]] = relationship(back_populates="cards")
    


    @classmethod
    def from_dict(cls, card_data):
        card_to_dict = Card(
            card_message = card_data["card_message"],
            likes = card_data.get("likes", 0),
            board_id = card_data.get("board_id")
        )
        return card_to_dict
    
    def to_dict(self) :
        card_as_dict= {
            "id": self.id,
            "card_message": self.card_message,
            "likes": self.likes
        }
        if self.board_id:
            card_as_dict["board_id"] = self.board_id
        return card_as_dict
        

