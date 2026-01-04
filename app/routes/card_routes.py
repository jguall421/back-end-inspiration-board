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

# @bp.get("/<card_id>")
# def get_one_card(card_id):
#     card = validate_card(card_id)
#     card_response = {
#         "id": card.id,
#         "card_message": card.card_message,
#         "likes": card.likes
#     }
#     return card_response

def validate_card(card_id):
    try:
        card_id = int(card_id)
    except:
        response = {f"message: card id {card_id} not valid"} 
        abort(make_response(response, 400))   
    query = db.select(Card).where(Card.id == card_id)
    card = db.session.scalar(query)  

    if not card:
        response = {f"message: card id {card_id} not found"}
        abort(make_response(response, 404))
    return card    

@bp.delete("/<card_id>")
def delete_card(card_id):
    card = validate_card(card_id)
    db.session.delete(card)
    db.session.commit()
    return Response(status=204, mimetype="application/json")







