from IPython.display import clear_output
import random

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

player1 = {"name": "", "mark": "X", "wins": 0}
player2 = {"name": "", "mark": "O", "wins": 0}

def get_names():
    res = input("Player 1 (X), please enter your name: ")
    player1["name"] = res
    res = input("Player 2 (O), please enter your name: ")
    player2["name"] = res

def up_first():
    coin = random.randint(1,2)
    if coin == 1:
        return player1
    else:
        return player2

def setup():
    print("Welcome to Python TicTacToe!")
    get_names()
    play_game()
    if play_again():
        clear_board()
        play_game()
    else:
        print("Bye, Felicia!")



def display_board(row1, row2, row3):
    clear_output()
    print("\nCurrent board state: \n")
    print(f" {row1[0]} | {row1[1]} | {row1[2]} ")
    print("-----------")
    print(f" {row2[0]} | {row2[1]} | {row2[2]} ")
    print("-----------")
    print(f" {row3[0]} | {row3[1]} | {row3[2]} \n")

def get_input():
    choice = ""
    acceptable_range = range(1,10)
    within_bounds = False
    open = False

    while choice.isdigit() == False or not within_bounds or not open:
        choice = input("Please choose your move[1-9]: ")
        if choice.isdigit() == False:
            print("That's not a digit!!\n")

        elif int(choice) in acceptable_range:
            within_bounds = True
            if position_available(int(choice)):
                open = True
            else:
                within_bounds = False
                print("Spot taken.")

        else:
            print("Must be between 1 and 9!")
    return int(choice)


def position_available(choice):
    if choice in [1,2,3]:
        if row1[choice-1] == " ":
            return True
    elif choice in [4,5,6]:
        if row2[(choice - 1) % 3] == " ":
            return True
    else:
        if row3[(choice - 1) % 3] == " ":
            return True
    return False

def update_board(choice, turn):
    if choice in [1,2,3]:
        row1[choice-1] = turn
    elif choice in [4,5,6]:
        row2[(choice - 1) % 3] = turn
    else:
        row3[(choice - 1) % 3] = turn



def take_turn(player):
    display_board(row1, row2, row3)
    name = player["name"]
    print(f"It is {name}'s turn.")
    move = get_input()
    update_board(move, player["mark"])

def check_win(row1,row2,row3):
    if row1[0] != " " and row1[0] == row1[1] and row1[1] == row1[2]:
        display_board(row1, row2, row3)
        if row1[0] == "X":
            name = player1["name"]
            player1["wins"] += 1
        else:
            name = player2["name"]
            player2["wins"] += 1
        print(f"{name} wins!")
        print(f"{player1['name']} - {player1['wins']}  |  {player2['name']} - {player2['wins']}")
        return True
    elif row2[0] != " " and row2[0] == row2[1] and row2[1] == row2[2]:
        display_board(row1, row2, row3)
        if row2[0] == "X":
            name = player1["name"]
            player1["wins"] += 1
        else:
            name = player2["name"]
            player2["wins"] += 1
        print(f"{name} wins!")
        print(f"{player1['name']} - {player1['wins']}  |  {player2['name']} - {player2['wins']}")
        return True
    elif row3[0] != " " and row3[0] == row3[1] and row3[1] == row3[2]:
        display_board(row1, row2, row3)
        if row3[0] == "X":
            name = player1["name"]
            player1["wins"] += 1
        else:
            name = player2["name"]
            player2["wins"] += 1
        print(f"{name} wins!")
        print(f"{player1['name']} - {player1['wins']}  |  {player2['name']} - {player2['wins']}")
        return True
    elif row1[0] != " " and row1[0] == row2[0] and row2[0] == row3[0]:
        display_board(row1, row2, row3)
        if row1[0] == "X":
            name = player1["name"]
            player1["wins"] += 1
        else:
            name = player2["name"]
            player2["wins"] += 1
        print(f"{name} wins!")
        print(f"{player1['name']} - {player1['wins']}  |  {player2['name']} - {player2['wins']}")
        return True
    elif row1[1] != " " and row1[1] == row2[1] and row2[1] == row3[1]:
        display_board(row1, row2, row3)
        if row1[1] == "X":
            name = player1["name"]
            player1["wins"] += 1
        else:
            name = player2["name"]
            player2["wins"] += 1
        print(f"{name} wins!")
        print(f"{player1['name']} - {player1['wins']}  |  {player2['name']} - {player2['wins']}")
        return True
    elif row1[2] != " " and row1[2] == row2[2] and row2[2] == row3[2]:
        display_board(row1, row2, row3)
        if row1[2] == "X":
            name = player1["name"]
            player1["wins"] += 1
        else:
            name = player2["name"]
            player2["wins"] += 1
        print(f"{name} wins!")
        print(f"{player1['name']} - {player1['wins']}  |  {player2['name']} - {player2['wins']}")
        return True
    elif row1[0] != " " and row1[0] == row2[1] and row2[1] == row3[2]:
        display_board(row1, row2, row3)
        if row1[0] == "X":
            name = player1["name"]
            player1["wins"] += 1
        else:
            name = player2["name"]
            player2["wins"] += 1
        print(f"{name} wins!")
        print(f"{player1['name']} - {player1['wins']}  |  {player2['name']} - {player2['wins']}")
        return True
    elif row1[2] != " " and row1[2] == row2[1] and row2[1] == row3[0]:
        display_board(row1, row2, row3)
        if row3[0] == "X":
            name = player1["name"]
            player1["wins"] += 1
        else:
            name = player2["name"]
            player2["wins"] += 1
        print(f"{name} wins!")
        print(f"{player1['name']} - {player1['wins']}  |  {player2['name']} - {player2['wins']}")

        return True
    else:
        return False

def check_tie(row1,row2,row3):
    for space in row1:
        if space == " ":
            return False
    for space in row2:
        if space == " ":
            return False
    for space in row3:
        if space == " ":
            return False
    display_board(row1,row2,row3)
    print("Tied game!")
    return True

def play_again():
    r = input("\nPlay again? [Y/N]").lower()
    if r == 'y':
        return True
    else:
        return False

def clear_board():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]


def play_game():
    turn = up_first()
    while not (check_win(row1,row2,row3) or check_tie(row1,row2,row3)):
        take_turn(turn)
        if turn == player1:
            turn = player2
        else:
            turn = player1

setup()

# display_board(row1,row2,row3)
# get_input()
