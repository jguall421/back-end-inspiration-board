from flask import Blueprint, request, Response, abort, make_response
from ..db import db
import os
import requests
from ..models.card import Card

bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@bp.get("")
def get_all_cards():
    query = db.select(Card).order_by(Card.id)
    cards = db.session.scalars(query)
    card_response = []
    for card in cards:
        card_response.append(
            {
                "id": card.id,
                "card_message": card.card_message,
                "likes": card.likes
            }
        )
    return card_response    


@bp.post("")
def create_cards():
    request_body = request.get_json()
    card_message = request_body["card_message"]
    #likes = request_body["likes"]
    new_card = Card(card_message = card_message)
    db.session.add(new_card)
    db.session.commit()

    response = {
        "id": new_card.id,
        "card_message": new_card.card_message
       # "likes": new_card.likes
    }
    return response, 201

#@bp.get("")
