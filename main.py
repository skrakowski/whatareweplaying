import random

def game_statement(games_list):
    num_games = len(games_list)
    if 0 == num_games:
        print("No games")
        return
    answer = random.randint(1, num_games)
    print("We are playing game #"+ str(answer) + " that game is " + str(games_list[answer-1]))
    


games = ["Siege", "GTFO","Apex", "Deep Rock", "Battlebit"]
game_statement(games)