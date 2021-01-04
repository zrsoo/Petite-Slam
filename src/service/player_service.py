"""
    Player service module
"""


class PlayerService:
    def __init__(self, player_repository):
        self.__player_repository = player_repository

    def get_list_of_players(self):
        dict_values = self.__player_repository.get_all_players()

        li_players = []
        for player in dict_values:
            li_players.append(player)

        return li_players

    def read_players(self, data_file):
        self.__player_repository.read_players_from_file(data_file)

    def get_players_sorted(self):
        li_players = self.get_list_of_players()
        li_players.sort(reverse=True, key=lambda x: x.p_strength)
        return li_players
