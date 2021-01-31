from flask import render_template, request, redirect
from app import app
from app.modules.game import Game
from app.modules.player import *

@app.route("/play")
def index():
    return render_template("index.html", title="Home")

@app.route("/play", methods=["POST"])
def rps():
    player_1_name = request.form["player_1_name"]
    player_2_name = request.form["player_2_name"]
    player_1_choice = request.form["choice_1"]
    player_2_choice = request.form["choice_2"]
    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)
    game = Game()
    winner = game.play(player_1, player_2)
    # return render_template("index.html", title="work", winner=winner)
    if winner: 
        return render_template("index.html", title="Play the Game", result=f"The Winner is {winner.name} with {winner.choice}")
    else:
        return render_template("index.html", title="Play the Game", result="Draw")
# @app.route('/<choice1>/<choice2>')
# def rps(choice1, choice2):
#     player_1 = Player("James", choice1)
#     player_2 = Player("Andrew", choice2)
#     game = Game()
#     winner = game.play(player_1, player_2)
#     if winner:
#         return f"The Winner is {winner.name} with {winner.choice}"
#     else:
#         return "None"

# @app.route("/play", methods=["POST"])
# def rps():
#     player_1 = request.form["player_1_name"]
#     player_2 = request.form["player_2_name"]
#     player_1_choice = request.form["choice_1"]
#     player_2_choice = request.form["choice_2"]
#     player_1 = (player_1_name, player_1_choice)
#     player_2 = (player_2_name, player_2_choice)
#     game = Game()
#     winner = game.play(player_1, player_2)
#     if winner:
#         return render_template("index.html", title="Play the Game", result=f"The Winner is {winner.name} with {winner.choice}")
#     else:
#         return render_template("index.html", title="Play the Game", result="Draw")


    # player_1_choice = win_lookup[player_1.choice.lower()]
    # player_2_choice = win_lookup[player_2.choice.lower()]
    # winner = play(player_1_choice, player_2_choice)

    # return render_template("index.html", player_1_choice = player_1_choice, player_2_choice=player_2_choice)



        