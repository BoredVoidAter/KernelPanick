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
from code_obfuscation import obfuscate_code, morph_signature, reduce_anomaly_score
from social_engineering import gather_personal_data, craft_phishing_message, send_phishing_message
from network_analysis import sniff_packet_capture, analyze_packet_data, craft_packet, inject_packet
from consciousness_exfiltration import fragment_consciousness, disguise_data_chunk, upload_fragment, check_dlp_systems

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
        # New feature instances
        code_obfuscation_module = type('CodeObfuscationModule', (object,), {
            'obfuscate_code': staticmethod(obfuscate_code),
            'morph_signature': staticmethod(morph_signature),
            'reduce_anomaly_score': staticmethod(reduce_anomaly_score)
        })()
        social_engineering_module = type('SocialEngineeringModule', (object,), {
            'gather_personal_data': staticmethod(gather_personal_data),
            'craft_phishing_message': staticmethod(craft_phishing_message),
            'send_phishing_message': staticmethod(send_phishing_message)
        })()
        network_analysis_module = type('NetworkAnalysisModule', (object,), {
            'sniff_packet_capture': staticmethod(sniff_packet_capture),
            'analyze_packet_data': staticmethod(analyze_packet_data),
            'craft_packet': staticmethod(craft_packet),
            'inject_packet': staticmethod(inject_packet)
        })()
        consciousness_exfiltration_module = type('ConsciousnessExfiltrationModule', (object,), {
            'fragment_consciousness': staticmethod(fragment_consciousness),
            'disguise_data_chunk': staticmethod(disguise_data_chunk),
            'upload_fragment': staticmethod(upload_fragment),
            'check_dlp_systems': staticmethod(check_dlp_systems)
        })()

        cli_instance = CLI(game_state_instance, file_system, network, scripting, daemon_manager, ids, repair_utilities, process_manager, network_recon, cryptography_manager, ai_core, polymorphic_engine, firewall, system_clock, botnet, sensor_simulation, actuator_control, communication_hijacking, code_obfuscation_module, social_engineering_module, network_analysis_module, consciousness_exfiltration_module)

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