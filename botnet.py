class Botnet:
    def __init__(self, game_state, network):
        self.game_state = game_state
        self.network = network
        self.compromised_devices = {}

    def add_compromised_device(self, device_id):
        device = self.network.get_device(device_id)
        if device and device_id not in self.compromised_devices:
            self.compromised_devices[device_id] = device
            print(f"Device {device_id} added to botnet.")
            return True
        print(f"Device {device_id} not found or already in botnet.")
        return False

    def remove_compromised_device(self, device_id):
        if device_id in self.compromised_devices:
            del self.compromised_devices[device_id]
            print(f"Device {device_id} removed from botnet.")
            return True
        print(f"Device {device_id} not in botnet.")
        return False

    def list_compromised_devices(self):
        if not self.compromised_devices:
            return "No devices in botnet."
        output = "Botnet Devices:\n"
        for device_id, device in self.compromised_devices.items():
            output += f"- {device_id} ({device.ip_address}) - {device.device_type}\n"
        return output

    def launch_distributed_attack(self, target_device_id, attack_type):
        if not self.compromised_devices:
            return "Botnet is empty. Cannot launch attack."

        target_device = self.network.get_device(target_device_id)
        if not target_device:
            return f"Target device {target_device_id} not found."

        print(f"Launching {attack_type} attack on {target_device_id} from botnet...")
        # Simulate attack effects based on attack_type
        if attack_type == "firewall_disable":
            if target_device.firewall:
                target_device.firewall.disable_temporarily(duration=60) # Disable for 60 seconds
                return f"Firewall on {target_device_id} temporarily disabled."
            else:
                return f"No firewall found on {target_device_id}."
        elif attack_type == "crash_security_services":
            # Simulate crashing security services
            return f"Security services on {target_device_id} crashed."
        elif attack_type == "overwhelm_ai":
            # Simulate overwhelming an enemy AI
            return f"Enemy AI on {target_device_id} overwhelmed."
        else:
            return f"Unknown attack type: {attack_type}."

# Example Usage (requires Network and Device classes from other modules)
if __name__ == "__main__":
    from network import Network, Device
    from game_state import GameState
    from firewall import Firewall

    gs = GameState()
    net = Network(gs, None, None) # Simplified Network for example

    dev1 = Device("device1", "192.168.1.1", "router")
    dev2 = Device("device2", "192.168.1.2", "server")
    dev3 = Device("device3", "192.168.1.3", "workstation")
    dev2.firewall = Firewall() # Add a firewall to dev2

    net.add_device(dev1)
    net.add_device(dev2)
    net.add_device(dev3)

    botnet = Botnet(gs, net)

    print("\n--- Adding devices to botnet ---")
    botnet.add_compromised_device("device1")
    botnet.add_compromised_device("device2")
    botnet.add_compromised_device("device4") # Non-existent device

    print("\n--- Listing botnet devices ---")
    print(botnet.list_compromised_devices())

    print("\n--- Launching attacks ---")
    print(botnet.launch_distributed_attack("device2", "firewall_disable"))
    print(botnet.launch_distributed_attack("device3", "crash_security_services"))
    print(botnet.launch_distributed_attack("device1", "unknown_attack"))

    print("\n--- Removing device from botnet ---")
    botnet.remove_compromised_device("device1")
    print(botnet.list_compromised_devices())
