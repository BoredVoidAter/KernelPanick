import sys
import io

# Import your game components
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
from hunter_ai import HunterAI
from clock import SystemClock
from botnet import Botnet
from sensor_simulation import SensorSimulation
from actuator_control import ActuatorControl
from communication_hijacking import CommunicationHijacking

# Global game state (for simplicity in this example, consider a more robust state management for a real game)
game_state_instance = None
cli_instance = None

def initialize_game_components():
    global game_state_instance, cli_instance
    if game_state_instance is None:
        game_state_instance = GameState()
        file_system = FileSystem(None) # Initialize with None, will set IDS later
        ids = IDS(game_state_instance, file_system)
        file_system.set_ids(ids) # Set IDS after it's initialized
        network = Network(game_state_instance, file_system, ids)
        scripting = Scripting(None) # Placeholder, will pass CLI later
        daemon_manager = DaemonManager(file_system, game_state_instance)
        repair_utilities = RepairUtilities(file_system)
        process_manager = ProcessManager()
        network_recon = NetworkRecon()
        cryptography_manager = CryptographyManager()
        ai_core = AICore()
        polymorphic_engine = PolymorphicEngine()
        firewall = Firewall() # Initialize with default empty rules
        hunter_ai = HunterAI("Sentinel", network) # Initialize HunterAI
        system_clock = SystemClock() # Initialize SystemClock
        botnet = Botnet(game_state_instance, network) # Initialize Botnet
        sensor_simulation = SensorSimulation()
        actuator_control = ActuatorControl()
        communication_hijacking = CommunicationHijacking()
        cli_instance = CLI(game_state_instance, file_system, network, scripting, daemon_manager, ids, repair_utilities, process_manager, network_recon, cryptography_manager, ai_core, polymorphic_engine, firewall, system_clock, botnet, sensor_simulation, actuator_control, communication_hijacking)
        scripting.cli = cli_instance # Set the CLI instance after it's created

def get_initial_boot_message():
    # Ensure components are initialized before displaying boot sequence
    initialize_game_components()
    return display_boot_sequence()

def run_game_command(command):
    global game_state_instance, cli_instance
    if game_state_instance is None:
        initialize_game_components()

    # Capture stdout for this command
    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    try:
        # Call the CLI's execute_command method
        output = cli_instance.execute_command(command)
        sys.stdout.write(output)

    except Exception as e:
        sys.stdout.write(f"Error during game command execution: {e}\n")
    finally:
        sys.stdout = old_stdout # Restore stdout

    return redirected_output.getvalue()