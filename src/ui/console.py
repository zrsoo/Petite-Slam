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
                    nr_of_players_eliminated = number_of_players - number_of_players_in_tournament

                    # If the number of players is a power of 2
                    if math.log2(number_of_players).is_integer():
                        print("There are no qualifications, since the number of players is already a power of 2.")
                    else:
                        for times in range(nr_of_players_eliminated):
                            print("Qualification: ")

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