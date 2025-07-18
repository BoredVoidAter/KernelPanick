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
    hunter_ai = HunterAI("Sentinel", network) # Initialize HunterAI
    system_clock = SystemClock() # Initialize SystemClock
    botnet = Botnet(game_state, network) # Initialize Botnet
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

    cli = CLI(game_state, file_system, network, scripting, daemon_manager, ids, repair_utilities, process_manager, network_recon, cryptography_manager, ai_core, polymorphic_engine, firewall, system_clock, botnet, sensor_simulation, actuator_control, communication_hijacking, code_obfuscation_module, social_engineering_module, network_analysis_module, consciousness_exfiltration_module)
    scripting.cli = cli # Set the CLI instance after it's created

    display_boot_sequence()
    while True:
        daemon_manager.run_daemons()
        hunter_ai.patrol() # Hunter AI patrols
        # Placeholder for player anomaly detection and hunting
        # if hunter_ai.detect_player(game_state.player_anomaly_score, game_state.player_location):
        #     hunter_ai.hunt_player()
        cli.start_loop()

if __name__ == "__main__":
    main()
