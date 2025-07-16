import sys
from game_state import GameState
from filesystem import FileSystem
from network import Network
from cli import CLI
from narrative import display_boot_sequence
from scripting import Scripting
from daemons import DaemonManager
from ids import IDS
from utilities import RepairUtilities

def main():
    game_state = GameState()
    file_system = FileSystem()
    network = Network(game_state, file_system)
    scripting = Scripting(None) # Placeholder, will pass CLI later
    daemon_manager = DaemonManager(file_system, game_state)
    ids = IDS(game_state, file_system)
    repair_utilities = RepairUtilities(file_system)
    cli = CLI(game_state, file_system, network, scripting, daemon_manager, ids, repair_utilities)
    scripting.cli = cli # Set the CLI instance after it's created

    display_boot_sequence()
    while True:
        daemon_manager.run_daemons()
        cli.start_loop()

if __name__ == "__main__":
    main()
