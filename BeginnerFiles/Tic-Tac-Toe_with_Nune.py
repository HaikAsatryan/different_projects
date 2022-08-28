board = {1: '-', 2: '-', 3: '-',
         4: '-', 5: '-', 6: '-',
         7: '-', 8: '-', 9: '-'}


def print_board(dictionary):
    print(f'| {dictionary[1]} | {dictionary[2]} | {dictionary[3]} |')
    print(f'+---+---+---+')
    print(f'| {dictionary[4]} | {dictionary[5]} | {dictionary[6]} |')
    print(f'+---+---+---+')
    print(f'| {dictionary[7]} | {dictionary[8]} | {dictionary[9]} |')
    print('\n')


def space_is_free(position):
    if board[position] == '-':
        return True
    return False


def insert_input(letter, position):
    if space_is_free(position):
        board[position] = letter
        print_board(board)
        if check_win():
            if letter == player:
                print("Its unbelievable you WIN!")
                quit()
            else:
                print("You loose, bot Nune wins! Next time try harder!")
                quit()

        if check_draw():
            print('Congrats it is draw!')
            quit()
        return
    else:
        position = int(input('Invalid position. Please put a valid position: '))
        insert_input(letter, position)
        return


def check_win():
    if board[1] == board[2] and board[1] == board[3] and board[1] != '-':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != '-':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != '-':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != '-':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != '-':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != '-':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != '-':
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] != '-':
        return True
    else:
        return False


def check_which_mark_won(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False


def check_draw():
    temp = 0
    for key in board.keys():
        if board[key] == '-':
            temp += 1
    if temp >= 1:
        return False
    return True


def player_move():
    global position
    while True:
        try:
            position = int(input(f'Enter a position for {player}: '))
        except:
            print('Please input only integer from 1 to 9 (inclusive)')
            player_move()
        if position < 1 or position > 9:
            print('Please input only integer from 1 to 9 (inclusive)')
            player_move()
        insert_input(player, position)
        break
    return


def nune_move():
    bestScore = -1000000
    bestMove = 0
    for key in board.keys():
        if board[key] == '-':
            board[key] = nuneBot
            score = minimax(board, False)
            board[key] = '-'
            if score > bestScore:
                bestScore = score
                bestMove = key
    insert_input(nuneBot, bestMove)
    return


def minimax(board, is_maximizing):
    if check_which_mark_won(nuneBot):
        return 1
    elif check_which_mark_won(player):
        return -1
    elif check_draw():
        return 0

    if is_maximizing:
        bestScore = -1000000
        for key in board.keys():
            if board[key] == '-':
                board[key] = nuneBot
                score = minimax(board, False)
                board[key] = '-'
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000000
        for key in board:
            if board[key] == '-':
                board[key] = player
                score = minimax(board, True)
                board[key] = '-'
                if score < bestScore:
                    bestScore = score
        return bestScore


# Game start's from here

print("Welcome to tic-tac-toe game with Haik's champion!")

while True:
    checking = input('Are you enough brave to start playing? (y/n): ')
    if checking.lower() == 'y':
        break
    elif checking.lower() == 'n':
        print('Bye :(')
        quit()
    else:
        print('Please only try to input "y" or "n"!')
        continue

print(f'I am happy that you have decided to play with me! I am tic-tac-toe champion NUNE! {chr(10)}{chr(10)}'
      f'Here are the rules how to play with me: {chr(10)}'
      f"1. The game is played on a grid that's 3 squares by 3 squares.{chr(10)}"
      f'2. You are X, your friend (or bot Nune in this case) is O. '
      f'Players take turns putting their marks in empty squares.{chr(10)}'
      f'3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.{chr(10)}'
      f'4. Squares are numbered from 1 to 9 (left to right) and you should input numbers in 1-9 range only.'
      f'5. When all 9 squares are full, the game is over. '
      f'If no player has 3 marks in a row, the game ends in a tie.{chr(10)}')

while True:
    choice = input('If everything is clear please select who shall start. ("x" for starting Player, "o" for starting '
                   'Nune "c" to close) ')
    if choice.lower() == "x":
        player = 'X'
        nuneBot = 'O'

        while not check_win():
            player_move()
            nune_move()

    elif choice.lower() == "o":
        player = 'O'
        nuneBot = 'X'
        while not check_win():
            nune_move()
            player_move()
    elif choice.lower() == "c":
        print('Bye :(')
        quit()
    else:
        print('Please only try to input "x", "o" or "c"!')
        continue