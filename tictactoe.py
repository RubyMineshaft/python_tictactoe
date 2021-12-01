row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

def display_board(row1, row2, row3):
    print("\nCurrent board state: \n")
    print(f" {row1[0]} | {row1[1]} | {row1[2]} ")
    print("-----------")
    print(f" {row2[0]} | {row2[1]} | {row2[2]} ")
    print("-----------")
    print(f" {row3[0]} | {row3[1]} | {row3[2]} \n")

display_board(row1,row2,row3)
