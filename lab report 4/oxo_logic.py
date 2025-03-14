import os
import sys
import subprocess

def run_in_new_window():
    if sys.platform.startswith('win'):
        subprocess.Popen(['cmd', '/c', f'start cmd /k python "{sys.argv[0]}"'], shell=True)
        sys.exit()
    elif sys.platform.startswith('linux'):
        subprocess.Popen(['gnome-terminal', '--', 'python3', sys.argv[0]])
        sys.exit()
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(['open', '-a', 'Terminal.app', sys.argv[0]])
        sys.exit()

run_in_new_window()

class Game:
    def __init__(self):
        self.board = [None] * 9
        self.current_player = 'X'

    def display_board(self):
        def cell_str(i):
            return self.board[i] if self.board[i] is not None else str(i)
        rows = [
            f"{cell_str(0)} | {cell_str(1)} | {cell_str(2)}",
            f"{cell_str(3)} | {cell_str(4)} | {cell_str(5)}",
            f"{cell_str(6)} | {cell_str(7)} | {cell_str(8)}"
        ]
        return "\n---------\n".join(rows)

    def make_move(self, pos):
        if pos < 0 or pos > 8 or self.board[pos] is not None:
            print("Invalid move.")
            return False
        self.board[pos] = self.current_player
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(self.board[a] == self.board[b] == self.board[c] and self.board[a] is not None for a, b, c in wins)

    def board_full(self):
        return all(cell is not None for cell in self.board)

if __name__ == '__main__':
    game = Game()
    print("Welcome to Tic Tac Toe!")
    while True:
        print("\nCurrent board:")
        print(game.display_board())
        try:
            pos = int(input(f"Player {game.current_player}, enter your move (0-8): "))
        except ValueError:
            print("Invalid input.")
            continue

        if game.make_move(pos):
            if game.check_win():
                print("\nFinal board:")
                print(game.display_board())
                print(f"Player {game.current_player} wins!")
                break
            elif game.board_full():
                print("\nFinal board:")
                print(game.display_board())
                print("It's a tie!")
                break
            game.switch_player()
