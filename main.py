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
from vulnerabilities import get_vulnerability
from hardware import get_hardware_interface
from polymorphic_engine import PolymorphicEngine
from firewall import Firewall

def main():
    game_state = GameState()
    file_system = FileSystem(None) # Initialize with None, will set IDS later
    ids = IDS(game_state, file_system)
    file_system.set_ids(ids) # Set IDS after it's initialized
    network = Network(game_state, file_system, ids)
    scripting = Scripting(None) # Placeholder, will pass CLI later
    daemon_manager = DaemonManager(file_system, game_state)
    repair_utilities = RepairUtilities(file_system)
    process_manager = ProcessManager()
    network_recon = NetworkRecon()
    cryptography_manager = CryptographyManager()
    ai_core = AICore()
    polymorphic_engine = PolymorphicEngine()
    firewall = Firewall() # Initialize with default empty rules
    cli = CLI(game_state, file_system, network, scripting, daemon_manager, ids, repair_utilities, process_manager, network_recon, cryptography_manager, ai_core, polymorphic_engine, firewall)
    scripting.cli = cli # Set the CLI instance after it's created

    display_boot_sequence()
    while True:
        daemon_manager.run_daemons()
        cli.start_loop()

if __name__ == "__main__":
    main()
