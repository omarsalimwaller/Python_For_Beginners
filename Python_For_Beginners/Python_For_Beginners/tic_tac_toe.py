

# Tic-Tac-Toe Board Layout
# [1,1] | [1,2] | [1,3]
# ______|_______|______
# [2,1] | [2,2] | [2,3]
# ______|_______|______
# [3,1] | [3,2] | [3,3]
win_array = [[[1,1],[1,2],[1,3]], [[1,1],[2,1],[3,1]], [[1,3],[2,3],[3,3]], [[3,1],[3,2],[3,3]], [[1,2],[2,2],[3,2]],
              [[2,1],[2,2],[2,3]], [[1,1],[2,2],[3,3]], [[3,1],[2,2],[1,3]]]

user_positions = [[],[]]

player_input = ['','']
player_marker = ['X ','O ']

valid = True

board = {"A1": ["1 ",True,[1,1]], "A2":["2 ",True,[1,2]], "A3": ["3 ",True,[1,3]], "B1":["4 ",True,[2,1]], "B2":["5 ",True,[2,2]], "B3":["6 ",True,[2,3]], 
         "C1":["7 ",True,[3,1]], "C2":["8 ",True,[3,2]], "C3":["9 ",True,[3,3]] }

count = 0
turn = 0

def print_board():
    print("%s | %s | %s" % (board["A1"][0], board["A2"][0], board["A3"][0]))
    print("___|____|___")
    print("%s | %s | %s" % (board["B1"][0], board["B2"][0], board["B3"][0]))
    print("___|____|___")
    print("%s | %s | %s" % (board["C1"][0], board["C2"][0], board["C3"][0]))


while valid:

    print_board()

    #Request input
    print("Enter your board position player %s." % (turn + 1))
    player_input[turn] = input("")    

    for i in board:
        if player_input[turn] == board[i][0].replace(" ","") and board[i][1]:
            #Update value if it is available         
            board[i][0] = player_marker[turn]
            board[i][1] = False
            user_positions[turn].append(board[i][2])
            print("Good move")

 
    #Determine winner
    for winning_combination in win_array:
        #Check for player 1 and player 2
        for player in user_positions:
            #Reset counter. Player must have 3 of the winning combinations.
            count = 0            
            for positions_selected in player:
                if positions_selected in winning_combination:
                    count += 1
                if count >= 3:
                    valid = False
                    print("Congrats player %s. You Win!" %(turn+1))
                    print("Final Board")
                    print_board()
    if valid:
        if turn == 0:
            turn =1
        else:
            turn = 0








