from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .card import Card


class Board(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    name: Mapped[str]
    cards: Mapped[list["Card"]] = relationship(back_populates="board", cascade="all, delete-orphan")
 


    def to_dict(self):
        board_as_dict = {
            "id": self.id,
            "title": self.title,
            "name": self.name
        }
     
        return board_as_dict

    @classmethod
    def from_dict(cls, board_data):
        new_board = cls(title=board_data["title"],
                       name=board_data["name"])

        return new_board
