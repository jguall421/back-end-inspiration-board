from app import create_app, db
from app.models.board import Board
from app.models.card import Card
from dotenv import load_dotenv

my_app = create_app()
with my_app.app_context():
    # Add boards
    db.session.add(Board(title="Dream Vacation Ideas", owner="Alice"))
    db.session.add(Board(title="Quotes That Inspire Me", owner="Bob"))
    db.session.add(Board(title="Recipes to Try", owner="Charlie"))
    db.session.add(Board(title="Coding Challenges", owner="Dana"))
    db.session.add(Board(title="Home Improvement Ideas", owner="Emma"))

    # Add cards for Board 1
    db.session.add(Card(message="Visit Iceland", likes=5, board_id=1))
    db.session.add(Card(message="Road trip across New Zealand", likes=3, board_id=1))
    db.session.add(Card(message="Stay in an overwater bungalow in Maldives", likes=7, board_id=1))

    # Add cards for Board 2
    db.session.add(Card(message="Do one thing every day that scares you.", likes=10, board_id=2))
    db.session.add(Card(message="Success is not final, failure is not fatal.", likes=4, board_id=2))
    db.session.add(Card(message="Be the change you wish to see in the world.", likes=6, board_id=2))

    # Add cards for Board 3
    db.session.add(Card(message="Homemade pasta", likes=2, board_id=3))
    db.session.add(Card(message="Vegan chocolate cake", likes=8, board_id=3))
    db.session.add(Card(message="Spicy Thai curry", likes=6, board_id=3))
    db.session.add(Card(message="Sourdough bread", likes=1, board_id=3))

    # Add cards for Board 4
    db.session.add(Card(message="Implement a binary search tree", likes=7, board_id=4))
    db.session.add(Card(message="Create a REST API with Flask", likes=9, board_id=4))
    db.session.add(Card(message="Build a small React app", likes=5, board_id=4))

    # Add cards for Board 5
    db.session.add(Card(message="Paint the living room blue", likes=4, board_id=5))
    db.session.add(Card(message="Install new kitchen backsplash", likes=6, board_id=5))
    db.session.add(Card(message="Build a backyard garden", likes=3, board_id=5))

    db.session.commit()