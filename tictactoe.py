row1 = [" ", " ", " "]
row2 = [" ", "X", " "]
row3 = [" ", " ", " "]

turn = "X"

def display_board(row1, row2, row3):
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

def update_board(choice):
    if choice in [1,2,3]:
        row1[choice-1] = turn
    elif choice in [4,5,6]:
        row2[(choice - 1) % 3] = turn
    else:
        row3[(choice - 1) % 3] = turn

    # Change player's turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"




# display_board(row1,row2,row3)
# get_input()
