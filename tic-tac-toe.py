# write your code there
def coordinates(test_input_list, board_state):
    if len(test_input_list) < 2:
        print("You should enter two numbers!")
        return True
    elif test_input_list[0].isalpha() or test_input_list[1].isalpha():
        print("You should enter numbers!")
        return True
    if any([int(cord) > 3 or int(cord) < 1 for cord in test_input_list]):
        print("Coordinates should be from 1 to 3!")
        return True
    elif board_state[int(test_input_list[0]) - 1][int(test_input_list[1]) - 1] != '_':
        print("This cell is occupied! Choose another one!")
        return True
    return False


def Board_display(board_state):
    print('---------')
    for row in board_state:
        print("|", " ".join(row), "|")
    print('---------')


def should_stop():
    stop_game = False
    board_string = ''.join(str(s) for row in board for s in row)
    Win = [board_string[:3], board[3:6], board_string[6:],
                 board_string[0:9:3], board_string[1:9:3], board_string[2:9:3],
                 board_string[0:9:4],
                 board_string[2:7:2]]
    if abs(board_string.count('X') - board_string.count('O')) > 1 \
            or ('XXX' in Win and 'OOO' in Win):
        print("Impossible")
        stop_game = True
    elif 'XXX' in Win:
        print("X wins")
        stop_game = True
    elif 'OOO' in Win:
        print("O wins")
        stop_game = True
    elif board_string.count('_') > 0:
        # print("Game not finished")
        stop_game = False
    elif board_string.count('_') == 0:
        stop_game = True
        print("Draw")
    return stop_game


string: str = "_" * 9
board = [[string[i], string[i + 1], string[i + 2]] for i in range(0, 9, 3)]
Board_display(board)
is_x_turn = True
while not should_stop():
    input_coordinates = [i for i in input("Enter the coordinates: ").split(" ")]
    if not coordinates(input_coordinates, board):
        input_coordinates = [int(i) for i in input_coordinates]
        board[input_coordinates[0] - 1][input_coordinates[1] - 1] = 'X' if is_x_turn else 'O'
        Board_display(board)
        is_x_turn = not is_x_turn