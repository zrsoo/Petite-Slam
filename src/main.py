"""
    Control module
"""
import traceback

from repo.repository import Repository
from service.game_service import GameService
from service.player_service import PlayerService
from ui.console import Console

if __name__ == "__main__":
    try:
        player_repository = Repository()
        player_service = PlayerService(player_repository)

        player_service.read_players("data_files\players")
        li_players = player_service.get_players_sorted()

        game_service = GameService(li_players)

        console = Console(player_service, game_service)

        # Start
        console.run_console()
    except Exception as ex:
        print(str(ex))
        traceback.print_exc()