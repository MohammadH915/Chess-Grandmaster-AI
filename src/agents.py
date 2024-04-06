import datetime
import random

import chess

import utiles


class Agent:
    """
        Base class for agents.
    """

    def __init__(self, board: chess.Board, next_player) -> None:
        self.board = board
        self.next_player = next_player

    def get_action(self):
        """
            This method receives a GameState object and returns an action based on its strategy.
        """
        pass

    """
            get possible moves : 
                possibleMoves = board.legal_moves

            create a move object from possible move : 
                move = chess.Move.from_uci(str(possible_move))

            push the move : 
                board.push(move)

            pop the last move:
                board.pop(move)
    """


class RandomAgent(Agent):
    def __init__(self, board: chess.Board, next_player):
        super().__init__(board, next_player)

    def get_action(self):
        return self.random()

    def random(self):
        possible_moves_list = list(self.board.legal_moves)

        random_move = random.choice(possible_moves_list)
        return chess.Move.from_uci(str(random_move))


class MinimaxAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        pass

    def minimax(self, depth, turn, is_maximizing):
        pass


class AlphaBetaAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        pass

    def alpha_beta(self, depth, turn, is_maximizing, alpha, beta):
        pass


class ExpectimaxAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        pass
    def expectimax(self, depth, turn, is_maximizing):
        pass


def evaluate_board_state(board, turn):
    node_evaluation = 0
    node_evaluation += utiles.check_status(board, turn)
    node_evaluation += utiles.evaluationBoard(board)
    node_evaluation += utiles.checkmate_status(board, turn)
    node_evaluation += utiles.good_square_moves(board, turn)
    if turn == 'white':
        return node_evaluation
    return -node_evaluation
