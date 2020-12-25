#board 
board = ["_" , "_" , "_",
        "_" , "_" , "_",
        "_" , "_" , "_"]
check_winner = None
game_still_going = True
current_player = "X"

def display():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display()                      #display board
    while game_still_going :
       # print("hello-2")
        handle_turn(current_player)
        check_if_game_over()                     #check for winner or tie
        flip_player()
    if check_winner == "X" or check_winner == "O":
        print(check_winner + "won")
    elif check_winner == None :
        print("Tie")

def handle_turn(player):
    #print("hello-1")
    print("Player" + player+ "s turn : ")
    position = input("Choose a place(1  to 9) : ")
    while position not in ["1" , "2" , "3" , "4" ,"5" ,"6" ,"7" ,"8" ,"9"] :
        print("Incorrect input!!!  ")
        print("Enter again : ")
        handle_turn(player)
    position = int(position) -1
    if(player == "X"):
        if(board[position] == "X" or board[position] == "O"):
            print("Enter valid position . This position is already filled")
        if(board[position] == "_") :
            #print("hello0x")
            board[position] = "X"
    elif(player == "O"):
        if(board[position] == "X" or board[position] == "O"):
            print("Enter valid position . This position is already filled")
        if(board[position] == "_") :
            #print("hello0O")
            board[position] = "O"
    display()                                               #display board
    

def check_if_game_over():
    #print("hello1")
    check_if_win()                          #check for winner
    #print("hello14")
    check_for_tie()                         #check if tie
    return
    
def check_if_win():
    global check_winner      #to modify  global variables we used this
    #print("hello2")
    row_winner = check_row()
    if row_winner:
        #print("hello5")
        check_winner = row_winner
        
    #print("hello6")
    column_winner = check_column()
    if column_winner:
       # print("hello9")
        check_winner = column_winner
    #print("hello10")
    dai_winner = check_dai()
    if dai_winner:
     #   print("hello13")
        check_winner = dai_winner
    return 

def check_row():                #if any row completely filled with either X or O
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"  
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_" 
    #print("hello3")
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2 :
        return board[3]
    elif row_3:
        return board[6]
    else:
        #print("hello4")
        return "no"

def check_column():              #if any column completely filled with either X or O
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "_"  
    col_2 = board[1] == board[4] == board[7] != "_"
    col_3 = board[2] == board[5] == board[8] != "_" 
    #print("hello7")
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2 :
        return board[1]
    elif col_3:
        return board[2]
    else:
       # print("hello8")
        return "no"
    
def check_dai():                #if the 2 diagonals completely filled with either X or O
    #print("hello11")
    global game_still_going
    dai1 = board[0] == board[4] == board[8] !="_"
    dai2 = board[6] == board[4] == board[2] !="_"
    if dai1 or dai2:
        game_still_going = False
    if dai1 :
        return board[0]
    elif dai2 :
        return board[6]
    else:
        #print("hello12")
        return "no"

def check_for_tie():     # if no winner and all spaces are filled
    #print("hello15")
    global game_still_going
    global check_winner
    if "_" not in board:
        game_still_going = False
        check_winner = None
    return
    
def flip_player():    #change the turns of player
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
    
play_game()   #play game -> starting point
input("Press any key to exit")