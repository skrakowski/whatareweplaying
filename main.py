import random
import csv


#function generates random number tied to one of the games in games_list
def game_statement(games_list):
    num_games = len(games_list)
    if 0 == num_games:
        print("No games")
        return
    answer = random.randint(1, num_games)
    print("We are playing " + str(games_list[answer-1]))

#function opens file with players and games they like, checks what players have been input
#adds those players games to the game list    
def game_reader(game_file):
    with open(game_file, encoding="utf-8", newline="") as f:
        freader = (csv.reader(f))
        games = []
        for row in freader:
            if row[0].lower() in act_players:
                games.extend(row[1:])
                
    return games

def active_players():
    act_players = []
    while True:
        players = input("What players are availible? Enter done when done: ")
        if players.lower() == "done":
            break
        else:
            act_players.append(players.lower())
    return act_players

if __name__ == "__main__":
    act_players = active_players()
    games = game_reader("list.csv")
    game_statement(games)
#TODO
#Allow  for looping input for each name and validation 
#Making the names a set **contains**
#Make A GitHub account
