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
from processes import ProcessManager
from network_recon import Network as NetworkRecon
from cryptography import CryptographyManager
from ai_core import AICore

def main():
    game_state = GameState()
    ids = IDS(game_state, file_system)
    file_system = FileSystem(ids)
    network = Network(game_state, file_system)
    scripting = Scripting(None) # Placeholder, will pass CLI later
    daemon_manager = DaemonManager(file_system, game_state)
    repair_utilities = RepairUtilities(file_system)
    process_manager = ProcessManager()
    network_recon = NetworkRecon()
    cryptography_manager = CryptographyManager()
    ai_core = AICore()
    cli = CLI(game_state, file_system, network, scripting, daemon_manager, ids, repair_utilities, process_manager, network_recon, cryptography_manager, ai_core)
    scripting.cli = cli # Set the CLI instance after it's created

    display_boot_sequence()
    while True:
        daemon_manager.run_daemons()
        cli.start_loop()

if __name__ == "__main__":
    main()
