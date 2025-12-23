from flask import Blueprint, request
from app.models.board import Board
from app.models.card import Card
from .route_utilities import create_model, get_models_with_filters, validate_model

bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@bp.post("")
def create_board():
    request_body = request.get_json()
    return create_model(Card, request_body)

@bp.get("")
def get_all_cards():
    return get_models_with_filters(Card, request.args)

@bp.get("/<card_id>")
def get_one_card(card_id):
    card = validate_model(Card, card_id)
    return card.to_dict()