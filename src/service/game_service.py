"""
    Game service module
"""

import math

class GameService:
    def __init__(self, li_players):
        self.__li_players = li_players

    def get_number_of_players(self):
        return len(self.__li_players)

    def get_number_of_players_in_tournament(self):
        number = len(self.__li_players)

        while not math.log2(number).is_integer():
            number -= 1

        return number

    def play_qualifications(self, nr_rounds):
        li_playing_players = self.__li_players[:nr_rounds * 2]

    def play_game(self):
        pass
