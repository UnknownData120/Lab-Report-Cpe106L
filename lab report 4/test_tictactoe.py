# test_tictactoe.py

import unittest
from oxo_logic import Game

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Initialize a new game before each test."""
        self.game = Game()

    def test_initial_board(self):
        """Test that the board initializes empty."""
        self.assertEqual(self.game.board, [None] * 9)

    def test_make_move_valid(self):
        """Test making a valid move."""
        result = self.game.make_move(0)
        self.assertTrue(result)
        self.assertEqual(self.game.board[0], 'X')

    def test_make_move_invalid_position(self):
        """Test that out-of-range moves are rejected."""
        result = self.game.make_move(9)
        self.assertFalse(result)

    def test_make_move_on_taken_position(self):
        """Test that moves on already occupied cells are rejected."""
        self.game.make_move(0)
        result = self.game.make_move(0)
        self.assertFalse(result)

    def test_switch_player(self):
        """Test switching between players."""
        initial = self.game.current_player
        self.game.switch_player()
        self.assertNotEqual(self.game.current_player, initial)

    def test_win_condition(self):
        """Test win detection for a row win."""
        self.game.board = ['X', 'X', 'X', None, None, None, None, None, None]
        self.assertTrue(self.game.check_win())

    def test_no_win(self):
        """Test that an empty board does not produce a win."""
        self.assertFalse(self.game.check_win())

    def test_board_full(self):
        """Test detecting a full board."""
        self.game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertTrue(self.game.board_full())

if __name__ == '__main__':
    unittest.main()
