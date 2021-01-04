"""
    Game service module
"""

import math
import random


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
        """
        Simulates qualifications
        :param nr_rounds:
        :return:
        """
        li_playing_players = self.__li_players[:nr_rounds * 2]
        li_lost_players = []

        # For each round
        for x in range(nr_rounds):
            # Pick 2 random players from the list of playing players
            index_player1 = random.randint(0, len(li_playing_players) - 1)
            index_player2 = random.randint(0, len(li_playing_players) - 1)

            # If accidentally, the same player is picked, make sure it doesn't stay that way
            while index_player2 == index_player1:
                index_player2 = random.randint(0, len(li_playing_players))

            print("\nQualifications: ")
            winner, loser = self.play_game(li_playing_players[index_player1], li_playing_players[index_player2])

            li_lost_players.append(loser)

        return li_lost_players

    def play_game(self, player1, player2):
        """
        Simulates the game played between 2 players
        :param player1:
        :param player2:
        :return: the player that won on the first position of a list, and the one that lost on the second position
        """
        print("The players of the game are:")
        self.display_player(player1)
        self.display_player(player2)

        winner = input("Who won?\n")

        if winner == '1':
            return [player1, player2]
        else:
            return [player2, player1]

    @staticmethod
    def display_player(player):
        print(player.id + ' ' + player.name + ' ' + player.p_strength)

    def remove_player_by_id(self, player_id):
        for player in self.__li_players:
            if player.id == player_id:
                self.__li_players.remove(player)

    def remove_losing_players(self, li_lost_players):
        for player in li_lost_players:
            self.remove_player_by_id(player.id)

    def get_remaining_players(self):
        return self.__li_players

    def play_tournament(self, nr_rounds):
        """
        Simulates tournament
        :param nr_rounds:
        :return:
        """
        li_playing_players = self.__li_players
        li_lost_players = []

        # For each round
        for x in range(nr_rounds):
            # Pick 2 random players from the list of playing players
            index_player1 = random.randint(0, len(li_playing_players) - 1)
            index_player2 = random.randint(0, len(li_playing_players) - 1)

            # If accidentally, the same player is picked, make sure it doesn't stay that way
            while index_player2 == index_player1:
                index_player2 = random.randint(0, len(li_playing_players))

            print("\nLast" + str(len(li_playing_players)) + ": ")
            winner, loser = self.play_game(li_playing_players[index_player1], li_playing_players[index_player2])

            li_lost_players.append(loser)

        return li_lost_players
