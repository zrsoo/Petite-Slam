"""
    Repository module
"""
from domain.entity import Player


class Repository:
    def __init__(self):
        self.__entities = {}

    def save_player(self, player):
        """
        Store players in a dictionary, where the id of the player
        is the key and the player himself is the value.
        :param player:
        :return:
        """
        self.__entities[player.id] = player

    def get_all_players(self):
        """
        :return: A list of all the players
        """
        return self.__entities.values()

    def read_players_from_file(self, data_file):
        """
        Reads players from a text file
        :param data_file: the file to read from
        :return: a list of all the players in the file
        """
        try:
            # Reading information from the file
            file = open(data_file, 'r')
            line = file.readline().strip()

            while len(line) > 0:
                # Formatting information
                line = line.split(',')

                # Saving players
                self.save_player(Player(line[0], line[1], line[2]))

                # Reading next line
                line = file.readline().strip()

            file.close()
        except Exception as ex:
            print(ex)
            raise ex