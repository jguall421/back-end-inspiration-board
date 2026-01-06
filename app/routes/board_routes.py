from flask import Blueprint, make_response, abort, request, Response
from app.models.board import Board
from .route_utilities import validate_model
from ..db import db
from ..models.card import Card

bp = Blueprint("board_bp", __name__, url_prefix="/boards")
@bp.post("")
def create_board():
    request_body = request.get_json()

    try:
        new_board = Board.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
    db.session.add(new_board)
    db.session.commit()

    return new_board.to_dict(), 201

@bp.get("")
def get_all_boards():
    # query = db.select(Board).order_by(Board.id)
    query = db.select(Board)
    
    title_param = request.args.get("title")
    if title_param:
    
        query = query.where(Board.title.ilike(f"%{title_param}%"))


    name_param = request.args.get("name")
    if name_param:
        # In case there are books with similar titles, we can also filter by description
        query = query.where(Board.name.ilike(f"%{name_param}%"))

    boards = db.session.scalars(query.order_by(Board.id))
    # We could also write the line above as:

    boards_response = []
    for board in boards:
        boards_response.append(board.to_dict())
        
    return boards_response


@bp.get("/<board_id>")
def get_one_board(board_id):
    board = validate_model(Board, board_id)

    return board.to_dict()

@bp.put("/<board_id>")
def update_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()

    board.title = request_body["title"]
    board.name = request_body["name"]
    db.session.commit()

    return Response(status=204, mimetype="application/json") # 204 No Content

@bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.post("/<board_id>/cards")
def create_card_for_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    request_body["board_id"] = board.id
    new_card = Card.from_dict(request_body)
    db.session.add(new_card)
    db.session.commit()
    return new_card.to_dict(), 201

@bp.get("/<board_id>/cards")
def get_all_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    response = [card.to_dict() for card in board.cards]
    return response

