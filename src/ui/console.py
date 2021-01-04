"""
    Console module
"""

import traceback
import math


class Console:
    def __init__(self, player_service, game_service):
        self.__player_service = player_service
        self.__game_service = game_service

    def run_console(self):
        # # Reading players from file
        # self.__player_service.read_players("data_files\players")

        while True:
            try:
                self.print_menu()

                command = input("Command: ")

                if command == "D" or command == "d":
                    self.print_players_sorted()
                elif command == "Pq" or command == "pq":
                    number_of_players = self.__game_service.get_number_of_players()
                    number_of_players_in_tournament = self.__game_service.get_number_of_players_in_tournament()
                    nr_rounds = number_of_players - number_of_players_in_tournament
                    # print(number_of_players)
                    # If the number of players is a power of 2
                    if math.log2(number_of_players).is_integer():
                        print("There are no qualifications, since the number of players is already a power of 2.")
                    else:
                        # Playing qualifications
                        li_lost_players = self.__game_service.play_qualifications(nr_rounds)
                        print(len(li_lost_players))
                        # Removing losing players
                        self.__game_service.remove_losing_players(li_lost_players)
                        # li_players = self.__game_service.get_remaining_players()
                        # for player in li_players:
                        #     self.display_player(player)
                elif command == "Pt" or command == "pt":
                    number_of_players = self.__game_service.get_number_of_players()
                    # print(number_of_players)
                    while number_of_players != 1:
                        number_of_players = self.__game_service.get_number_of_players()
                        nr_rounds = math.floor(math.log2(number_of_players))
                        # print(nr_rounds)
                        li_lost_players = self.__game_service.play_tournament(nr_rounds)
                        self.__game_service.remove_losing_players(li_lost_players)

                    print("The winner is: ")
                    li_player = self.__game_service.get_remaining_players()
                    self.display_player(li_player[0])

                elif command == "X" or command == 'x':
                    return
            except Exception as ex:
                print(str(ex))
                traceback.print_exc()

    @staticmethod
    def print_menu():
        print("1.) D - Display all players.\n"
              "2.) Pq - Play qualifying round.\n"
              "3.) Pt - Play the tournament.\n"
              "4.) X - Exit.")

    def print_players_sorted(self):
        li_players = self.__player_service.get_players_sorted()

        print("\nThe list of all players is:\n")

        for player in li_players:
            print(player.id + ' ' + player.name + ' ' + player.p_strength)

        print("\n")

    @staticmethod
    def display_player(player):
        print(player.id + ' ' + player.name + ' ' + player.p_strength)