board=["-","-","-",
       "-","-","-",
       "-","-","-",]

currentpayer="X"
gameisgoing=True
winner=None


def disp_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turns():
    global gameisgoing
    position=int(input("enter position:"))
    board[position]=currentpayer

def swap_payer():
    global currentpayer
    if currentpayer=="X":
        currentpayer="O"
    elif currentpayer=="O":
        currentpayer="X"

def check_who_is_the_winner():
    global winner
    rowwinner = check_row()
    colwinner = check_column()
    diawinner = check_dia()

    if rowwinner:
        winner = rowwinner
    elif colwinner:
        winner = colwinner
    elif diawinner:
        winner = diawinner


def check_row():
    global gameisgoing
    row1=board[0]==board[1]==board[2]!='_'
    row2=board[3]==board[4]==board[5]!='_'
    row3=board[6]==board[7]==board[8]!='_'

    if row1 or row2 or row3:
        gameisgoing=False

    if row1:
        return board[1]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

def check_column():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "-"  # empty
    col2 = board[1] == board[4] == board[7] != "-"  # empty
    col3 = board[2] == board[5] == board[8] != "-"  # X

    if col1 or col2 or col3:
        gameisgoing = False

    if col1:  # inside row1 variable if something is present
        return board[6]
    elif col2:
        return board[1]

    elif col3:
        return board[5]


def check_dia():
    global gameisgoing
    dia1 = board[0] == board[4] == board[8] != "-"  # empty
    dia2 = board[2] == board[4] == board[6] != "-"  # empty


    if dia1 or dia2:
        gameisgoing = False

    if dia1:  # inside row1 variable if something is present
        return board[4]
    elif dia2:
        return board[6]

def check_draw():
    global gameisgoing
    if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] != "-":
        gameisgoing=False
        print("Match is Drawn")

def paly_game():
    global gameisgoing
    while gameisgoing:
        disp_board()
        handle_turns()
        swap_payer()
        check_who_is_the_winner()
        #check_draw()

    if winner == "X":
        print("X is the winner")
    elif winner == "O":
        print("O is the winner")



paly_game()