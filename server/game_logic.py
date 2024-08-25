class Game:
    def __init__(self):
        self.board = [["" for _ in range(5)] for _ in range(5)]
        self.players = {}
        self.turn = "A"

    def initialize_game(self, player_id, characters):
        if player_id not in self.players:
            self.players[player_id] = characters
            start_row = 0 if player_id == "A" else 4
            for i, char in enumerate(characters):
                self.board[start_row][i] = f"{player_id}-{char}"

    def validate_move(self, player_id, char_name, move):
        # Check if the player has the turn
        if not self.is_valid_turn(player_id):
            return False

        # Check if the character exists and belongs to the current player
        char_position = self.get_character_position(player_id, char_name)
        if char_position == (None, None):
            return False

        row, col = char_position
        # Validate move based on the character's movement rules
        if move in ["L", "R", "F", "B"]:
            return self.is_valid_pawn_move(row, col, move)
        elif move in ["FL", "FR", "BL", "BR"]:
            return self.is_valid_hero2_move(row, col, move)
        else:
            return False

    def process_move(self, player_id, char_name, move):
        if not self.is_valid_turn(player_id):
            return False

        char_position = self.get_character_position(player_id, char_name)
        if char_position == (None, None):
            return False  # Character not found

        old_row, old_col = char_position
        new_row, new_col = old_row, old_col

        # Determine new position based on the move command
        if move == "L":
            new_col -= 1
        elif move == "R":
            new_col += 1
        elif move == "F":
            new_row -= 1
        elif move == "B":
            new_row += 1
        elif move == "FL":
            new_row -= 1
            new_col -= 1
        elif move == "FR":
            new_row -= 1
            new_col += 1
        elif move == "BL":
            new_row += 1
            new_col -= 1
        elif move == "BR":
            new_row += 1
            new_col += 1
        else:
            return False  # Invalid move command

        # Ensure the new position is within bounds
        if not (0 <= new_row < 5 and 0 <= new_col < 5):
            return False

        # Check if the new position is occupied by an opponent's character
        target = self.board[new_row][new_col]
        if target and target.startswith(player_id):
            return False  # Cannot move to a space occupied by a friendly character

        # Move character
        self.board[new_row][new_col] = self.board[old_row][old_col]
        self.board[old_row][old_col] = ""

        # Switch turn
        self.switch_turn()
        return True

    def is_game_over(self):
        player_a_characters = any("A-" in cell for row in self.board for cell in row)
        player_b_characters = any("B-" in cell for row in self.board for cell in row)
        return not player_a_characters or not player_b_characters

    def get_game_state(self):
        return self.board

    def get_character_position(self, player_id, char_name):
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == f"{player_id}-{char_name}":
                    return (row, col)
        return (None, None)

    def switch_turn(self):
        self.turn = "B" if self.turn == "A" else "A"

    def is_valid_turn(self, player_id):
        return self.turn == player_id

    def is_valid_pawn_move(self, row, col, move):
        # Pawn moves one step in any direction, and cannot move outside the board
        if move == "L":
            return col > 0
        elif move == "R":
            return col < 4
        elif move == "F":
            return row > 0
        elif move == "B":
            return row < 4
        return False

    def is_valid_hero2_move(self, row, col, move):
        # Hero2 moves diagonally, cannot move outside the board
        if move == "FL":
            return row > 0 and col > 0
        elif move == "FR":
            return row > 0 and col < 4
        elif move == "BL":
            return row < 4 and col > 0
        elif move == "BR":
            return row < 4 and col < 4
        return False
