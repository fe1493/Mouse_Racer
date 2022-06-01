"""Game_info Class"""
'''Class in charge of the information of the game'''


class GameInfo:
    def __init__(self):
        self.started = False
        self.ended = False
        self.score = 0

    '''Function to start the game'''
    def start_game(self):
        self.score = 0
        self.started = True
        self.ended = False

    '''Function to end the game'''
    def end_game(self):
        self.ended = True
        self.started = False

    '''Update the score'''
    def update_score(self):
        self.score += 1

    '''Update the score for the escape element'''
    def special_update_score(self):
        self.score += 5






