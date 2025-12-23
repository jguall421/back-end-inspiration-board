from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .card import Card

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]


    def to_dict(self):
        boardr_as_dict = {
            "id": self.id,
            "name": self.name
        }
        
        return boardr_as_dict
    
    @classmethod
    def from_dict(cls, board_data):
        new_board = cls(name=board_data["name"])
        return new_board
  