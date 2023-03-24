# *** Игра "Крестики-нолики" ***

board = {"11": " ", "12": " ", "13": " ", "21": " ", "22": " ", "23": " ", "31": " ", "32": " ", "33": " "}
print("\033[0;33m" + "Пример ввода: 12, где 1 - это номер строки, а 2 - это номер столбца.\n" + "\033[0m")


def draw_board(board):
    print(" ", "|", "1", "|", "2", "|", "3", "|")
    print("-" * 15)
    for j in range(3):
        j += 1
        print(j, "|", board[str(j) + "1"], "|", board[str(j) + "2"], "|", board[str(j) + "3"], "|")
        print("-" * 15)


def take_input(player_token):
    valid = False
    while not valid:
        player_choice = input("\033[0m" + "Ходит " + player_token + ": ")

        if player_choice not in list(board.keys()):
            print("\033[0;31m" + "Некорректный ввод!")
            continue

        if str(board[player_choice]) not in "X0":
            board[player_choice] = player_token
            valid = True
        else:
            print("\033[0;31m" + "Эта клетка уже занята!")


def check_win(board):
    win_coord = (('11', '12', '13'), ('21', '22', '23'), ('31', '32', '33'),
                 ('11', '21', '31'), ('12', '22', '32'), ('13', '23', '33'),
                 ('13', '22', '31'), ('11', '22', '33'))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]] != " ":
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        counter += 1
        if counter > 4:
            winner = check_win(board)
            if winner:
                print("\033[32m" + "*" * 3, winner, "выиграл!", "*" * 3)
                win = True
                break
        if counter == 9:
            print("\033[0;33m" + "*" * 3, "Ничья!", "*" * 3)
            break
    draw_board(board)


main(board)
