
import random

class Firewall:
    def __init__(self, blocked_ports=None):
        self.blocked_ports = blocked_ports if blocked_ports is not None else []

    def is_port_blocked(self, port):
        return port in self.blocked_ports

class NetworkDevice:
    def __init__(self, device_id, open_ports=None, services=None, firewall=None):
        self.device_id = device_id
        self.open_ports = open_ports if open_ports is not None else []
        self.services = services if services is not None else {}
        self.firewall = firewall if firewall is not None else Firewall()

    def scan_port(self, port, aggressive=False):
        if self.firewall.is_port_blocked(port):
            return False, "Port blocked by firewall"
        
        if port in self.open_ports:
            # Simulate IDS detection for aggressive scans
            if aggressive and random.random() < 0.3: # 30% chance of detection
                return True, f"Port {port} is open (IDS detected aggressive scan)", True
            return True, f"Port {port} is open", False
        return False, f"Port {port} is closed", False

    def get_service_on_port(self, port):
        return self.services.get(port)

class Network:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        self.devices[device.device_id] = device

    def get_device(self, device_id):
        return self.devices.get(device_id)

    def simulate_portscan(self, source_device_id, target_device_id, ports_to_scan, aggressive=False):
        target_device = self.get_device(target_device_id)
        if not target_device:
            return {"error": "Target device not found"}

        results = {}
        for port in ports_to_scan:
            is_open, message = target_device.scan_port(port, aggressive)
            results[port] = {"open": is_open, "message": message}
        return results
