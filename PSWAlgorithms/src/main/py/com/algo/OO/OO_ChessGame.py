'''
Design a chess game using object oriented principles
'''

class Chess_Piece():
    _piece_types = {"King": 1, "Queen": 2, "Rook": 3, "Bishop": 4, "Knight": 5, "Pawn": 6}
    _piece_color = {"Black": 1, "White": 2}

    def __init__(self, p_type, color, position):
        self.type = Chess_Piece._piece_types[p_type]
        self.color =Chess_Piece. _piece_color[color]
        self.current_position = position

    def get_estimated_positions(self, chess):
        possible_positions = []
        current_position = self.current_position
        if self.type == 1: #King
            if 0 <= current_position.x_axis - 1 <= 7:
                new_position = Position(current_position.x_axis-1, current_position.y_axis)
                possible_positions.append(new_position)

            if 0 <= current_position.x_axis + 1 <= 7:
                new_position = Position(current_position.x_axis+1, current_position.y_axis)
                possible_positions.append(new_position)

            if 0 <= current_position.y_axis - 1 <= 7:
                new_position = Position(current_position.x_axis, current_position.y_axis-1)
                possible_positions.append(new_position)

            if 0 <= current_position.y_axis - 1 <= 7:
                new_position = Position(current_position.x_axis, current_position.y_axis+1)
                possible_positions.append(new_position)

        elif self.type == 2: #Queen
            for x_axis in range(0,8):
                if x_axis != current_position.x_axis:
                    if 0 <= current_position.x_axis - x_axis <= 7:
                        new_position = Position(current_position.x_axis-x_axis, current_position.y_axis)
                        possible_positions.append(new_position)

                    if 0 <= current_position.x_axis + x_axis <= 7:
                        new_position = Position(current_position.x_axis+x_axis, current_position.y_axis)
                        possible_positions.append(new_position)

            for y_axis in range(0,8):
                if y_axis != current_position.y_axis:
                    if 0 <= current_position.y_axis - y_axis <= 7:
                        new_position = Position(current_position.x_axis, current_position.y_axis-y_axis)
                        possible_positions.append(new_position)

                    if 0 <= current_position.x_axis + y_axis <= 7:
                        new_position = Position(current_position.x_axis, current_position.y_axis+y_axis)
                        possible_positions.append(new_position)

            for index in range(0,8):
                if 0 <= current_position.x_axis - index <= 7 and 0 <= current_position.y_axis - index <= 7:
                    new_position = Position(current_position.x_axis-index, current_position.y_axis-index)
                    possible_positions.append(new_position)

                if 0 <= current_position.x_axis + index <= 7 and 0 <= current_position.y_axis + index <= 7:
                    new_position = Position(current_position.x_axis+index, current_position.y_axis+index)
                    possible_positions.append(new_position)

                if 0 <= current_position.x_axis - index <= 7 and 0 <= current_position.y_axis + index <= 7:
                    new_position = Position(current_position.x_axis-index, current_position.y_axis+index)
                    possible_positions.append(new_position)

                if 0 <= current_position.x_axis + index <= 7 and 0 <= current_position.y_axis - index <= 7:
                    new_position = Position(current_position.x_axis+index, current_position.y_axis-index)
                    possible_positions.append(new_position)

        elif self.type == 3: #Rook
            for x_axis in range(0,8):
                if x_axis != current_position.x_axis:
                    if 0 <= current_position.x_axis - x_axis <= 7:
                        new_position = Position(current_position.x_axis-x_axis, current_position.y_axis)
                        possible_positions.append(new_position)

                    if 0 <= current_position.x_axis + x_axis <= 7:
                        new_position = Position(current_position.x_axis+x_axis, current_position.y_axis)
                        possible_positions.append(new_position)

            for y_axis in range(0,8):
                if y_axis != current_position.y_axis:
                    if 0 <= current_position.y_axis - y_axis <= 7:
                        new_position = Position(current_position.x_axis, current_position.y_axis-y_axis)
                        possible_positions.append(new_position)

                    if 0 <= current_position.x_axis + y_axis <= 7:
                        new_position = Position(current_position.x_axis, current_position.y_axis+y_axis)
                        possible_positions.append(new_position)

        elif self.type == 4:  # Bishop
            for index in range(0,8):
                if 0 <= current_position.x_axis - index <= 7 and 0 <= current_position.y_axis - index <= 7:
                    new_position = Position(current_position.x_axis-index, current_position.y_axis-index)
                    possible_positions.append(new_position)

                if 0 <= current_position.x_axis + index <= 7 and 0 <= current_position.y_axis + index <= 7:
                    new_position = Position(current_position.x_axis+index, current_position.y_axis+index)
                    possible_positions.append(new_position)

                if 0 <= current_position.x_axis - index <= 7 and 0 <= current_position.y_axis + index <= 7:
                    new_position = Position(current_position.x_axis-index, current_position.y_axis+index)
                    possible_positions.append(new_position)

                if 0 <= current_position.x_axis + index <= 7 and 0 <= current_position.y_axis - index <= 7:
                    new_position = Position(current_position.x_axis+index, current_position.y_axis-index)
                    possible_positions.append(new_position)

        elif self.type == 5:  # Knight
            if 0 <= current_position.x_axis + 2 <= 7 and 0 <= current_position.y_axis + 1 <= 7:
                new_position = Position(current_position.x_axis+2, current_position.y_axis+1)
                possible_positions.append(new_position)

            if 0 <= current_position.x_axis + 2 <= 7 and 0 <= current_position.y_axis - 1 <= 7:
                new_position = Position(current_position.x_axis+2, current_position.y_axis-1)
                possible_positions.append(new_position)

            if 0 <= current_position.x_axis - 2 <= 7 and 0 <= current_position.y_axis + 1 <= 7:
                new_position = Position(current_position.x_axis-2, current_position.y_axis+1)
                possible_positions.append(new_position)

            if 0 <= current_position.x_axis - 2 <= 7 and 0 <= current_position.y_axis - 1 <= 7:
                new_position = Position(current_position.x_axis-2, current_position.y_axis-1)
                possible_positions.append(new_position)

            if 0 <= current_position.y_axis + 2 <= 7 and 0 <= current_position.x_axis + 1 <= 7:
                new_position = Position(current_position.x_axis+1, current_position.y_axis+2)
                possible_positions.append(new_position)

            if 0 <= current_position.y_axis + 2 <= 7 and 0 <= current_position.x_axis - 1 <= 7:
                new_position = Position(current_position.x_axis-1, current_position.y_axis+2)
                possible_positions.append(new_position)

            if 0 <= current_position.y_axis - 2 <= 7 and 0 <= current_position.x_axis + 1 <= 7:
                new_position = Position(current_position.x_axis+1, current_position.y_axis-2)
                possible_positions.append(new_position)

            if 0 <= current_position.y_axis - 2 <= 7 and 0 <= current_position.x_axis - 1 <= 7:
                new_position = Position(current_position.x_axis-1, current_position.y_axis-2)
                possible_positions.append(new_position)

        elif self.type == 6:  # Pawn
            new_position = Position(current_position.x_axis, current_position.y_axis+1)
            possible_positions.append(new_position)
            if chess.is_position_free(current_position.x_axis+1, current_position.y_axis+1):
                new_position = Position(current_position.x_axis+1, current_position.y_axis+1)
                possible_positions.append(new_position)

        return possible_positions

    def move_piece(self, position):
        self.current_position = position

    def piece_dies(self, chess_played):
        chess_played[self.current_position.x_axis][self.current_position.y_axis] = 0

class Position():
    def __init__(self):
        x_axis = 0
        y_axis = 0

class Player():
    def __init__(self, color, assigned_piece):
        self.assigned_color = color
        self.assigned_pieces = assigned_piece

    def take_turn(self, chess_played, piece_type):
        return self.move_piece(chess_played, piece_type)

    def move_piece(self, chess_played, piece_type):
        hold_piece = self.assigned_pieces[piece_type]
        est_positions = hold_piece.get_estimated_positions(chess_played)
        moved_position = est_positions[1]

        chess_played[moved_position.x_axis][moved_position.y_axis] = hold_piece

        if chess_played.is_position_free(moved_position):
            hold_piece.move_piece(moved_position)
            return "Moved"
        else:
            available_piece = chess_played.get_piece(moved_position)
            available_piece.piece_dies(chess_played)
            hold_piece.move_piece(moved_position)
            if available_piece.type == 1:
                return "Win"
            else:
                return "Moved"

class Chess():
    def __init__(self):
        self.chess_board = [ [0 for index in range(0,8) ] for index in range(0,8)]
        self.chess_pieces = {}

        for color in ("Black", "White"):
            all_color_pieces = {}
            x_axis = 0
            if color == "Black":
                x_axis = 0
            else:
                x_axis = 7

            chess_piece = Chess_Piece("King", color, Position(x_axis,3))
            self.chess_board[x_axis][3] = chess_piece
            #all_color_pieces.append(chess_piece)
            all_color_pieces["King"] = chess_piece

            chess_piece = Chess_Piece("Queen", color, Position(x_axis, 4))
            self.chess_board[x_axis][4] = chess_piece
            #all_color_pieces.append(chess_piece)
            all_color_pieces["Queen"] = chess_piece

            for y_axis in (0, 3):
                if y_axis == 0:
                    piece_type = "Rook"
                elif y_axis == 1:
                    piece_type = "Bishop"
                elif y_axis == 2:
                    piece_type = "Knight"

                chess_piece = Chess_Piece(piece_type, color, Position(x_axis, y_axis))
                self.chess_board[x_axis][y_axis] = chess_piece
                #all_color_pieces.append(chess_piece)
                all_color_pieces[piece_type] = chess_piece

                chess_piece = Chess_Piece(piece_type, color, Position(x_axis, 7-y_axis))
                self.chess_board[x_axis][7-y_axis] = chess_piece
                #all_color_pieces.append(chess_piece)
                all_color_pieces[piece_type] = chess_piece

            for y_axis in range(0,7):
                if color == "Black":
                    x_axis += 1
                else:
                    x_axis -= 1

                chess_piece = Chess_Piece("Pawn", color, Position(x_axis, y_axis))
                self.chess_board[x_axis][y_axis] = chess_piece
                #all_color_pieces.append(chess_piece)
                all_color_pieces["Pawn"] = chess_piece

            self.chess_pieces[color] = all_color_pieces

        self.player1 = Player("Black", self.chess_pieces["Black"])
        self.player2 = Player("White", self.chess_pieces["White"])

    def is_position_free(self, position):
        return self.chess_board[position.x_axis][position.y_axis] == 0

    def get_piece(self, position):
        return self.chess_board[position.x_axis][position.y_axis]

import random
class Game_Manager():
    piece_types = {1: "King", 2: "Queen", 3: "Rook", 4: "Bishop", 5: "Knight", 6: "Pawn"}
        #{"King": 1, "Queen": 2, "Rook": 3, "Bishop": 4, "Knight": 5, "Pawn": 6}

    def __init__(self, chess):
        self.chess = chess

    def play_game(self):
        value = "start"
        while value != "Win":
            random_piece = random.randrange(1, 6)
            random_piece_type = Game_Manager.piece_types(random_piece)
            value = self.chess.player1.take_turn(self.chess, random_piece_type)

            if value == "Win":
                return

            random_piece = random.randrange(1, 6)
            random_piece_type = Game_Manager.piece_types(random_piece)
            value = self.chess.player2.take_turn(self.chess, random_piece_type)

if __name__ == '__main__':
    chess = Chess()
    game_manager = Game_Manager(chess)
    game_manager.play_game()
