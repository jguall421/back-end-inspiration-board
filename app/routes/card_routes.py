from flask import Blueprint, request, Response, abort, make_response
from ..db import db
import os
import requests
from ..models.card import Card
from .routes_utilities import validate_model

bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@bp.get("")
def get_all_cards():
    query = db.select(Card).order_by(Card.id)
    cards = db.session.scalars(query)
    card_response = []
    for card in cards:
        card_response.append(
            card.to_dict()
        )
    return card_response    


@bp.post("")
def create_cards():
    request_body = request.get_json()
    try:
        new_card = Card.from_dict(request_body)
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
            
    db.session.add(new_card)
    db.session.commit()
    response = new_card.to_dict()
    return response, 201

# @bp.get("/<card_id>")
# def get_one_card(card_id):
#     card = validate_model(card_id)
#     return card.to_dict()

  

@bp.delete("/<card_id>")
def delete_card(card_id):
    card = validate_model(card_id)
    db.session.delete(card)
    db.session.commit()
    return Response(status=204, mimetype="application/json")



@bp.patch("/<card_id>")
def add_likes(card_id):
    card= validate_model(Card, card_id)
    card.likes += 1
    db.session.commit()
    return Response(status=204, mimetype="application/json")








