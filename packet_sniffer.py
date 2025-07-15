import time
import random

class PacketSniffer:
    def __init__(self, network, game_state, ids):
        self.network = network
        self.game_state = game_state
        self.ids = ids
        self.captured_packets = []

    def start_sniffing(self, duration=5, packets_to_capture=10):
        if self.game_state.ram < 10:
            return "Error: Insufficient RAM to start packet sniffer. Recharge or find more resources."
        self.game_state.consume_resources(ram=10)

        print(f"Starting packet sniffer on {self.game_state.current_device} for {duration} seconds...")
        self.ids.increment_anomaly_score(5, "Network packet sniffing initiated")

        # Simulate capturing packets
        for i in range(packets_to_capture):
            time.sleep(random.uniform(0.1, duration / packets_to_capture))
            packet = self._generate_simulated_packet()
            self.captured_packets.append(packet)
            print(f"Captured packet {i+1}/{packets_to_capture}")
        
        return f"Packet sniffing complete. Captured {len(self.captured_packets)} packets."

    def _generate_simulated_packet(self):
        # Simulate various types of network traffic
        packet_types = [
            "ARP Request: Who has 192.168.1.1? Tell 192.168.1.100",
            "TCP SYN: 192.168.1.100:54321 -> 192.168.1.1:80 (HTTP)",
            "UDP DNS Query: 192.168.1.101 -> 8.8.8.8:53 (google.com)",
            "ICMP Echo Request: 192.168.1.102 -> 192.168.1.1",
            "HTTP GET /index.html HTTP/1.1 Host: example.com",
            "SSH Login Attempt: user:admin pass:password123",
            "FTP Data Transfer: file.txt (unencrypted)",
            "SMB Share Access: \\SERVER\share\document.docx",
            "Email (SMTP): From: user@example.com To: admin@example.com Subject: Urgent!",
            "Internal API Call: GET /api/v1/users/123/profile",
            "Database Query: SELECT * FROM users WHERE username='root'",
            "System Update Check: OS_VERSION=1.0.0 NEW_VERSION=1.0.1",
            "Device Heartbeat: DEVICE_ID=toaster_001 STATUS=online",
            "Encrypted Traffic (TLS): [encrypted data]",
            "Unencrypted Credential Transfer: username=testuser&password=testpass",
            "Configuration Update: DEVICE_ID=router_001 SETTINGS=new_config.json",
            "Log Transfer: LOG_ENTRY=Anomaly detected from 192.168.1.5",
            "Software License Check: LICENSE_KEY=ABC-123-XYZ",
            "Remote Command Execution: CMD=reboot_system",
            "IoT Sensor Data: TEMP=25C HUMIDITY=60%"
        ]
        return random.choice(packet_types)

    def save_packets(self, file_system, file_path):
        if not self.captured_packets:
            return "No packets have been captured yet. Run 'sniff' first."
        
        content = "\n".join(self.captured_packets)
        path_parts = file_path.split('/')
        result = file_system.create_file(path_parts, content, 'rw-')
        if "Error" in result:
            return result
        else:
            self.captured_packets = [] # Clear captured packets after saving
            return f"Captured packets saved to {file_path}."