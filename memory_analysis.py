import random

class Memdump:
    def __init__(self, game_state):
        self.game_state = game_state
        self.last_dump = None

    def capture_ram_snapshot(self):
        if self.game_state.ram < 50: # Example resource cost
            return "Error: Insufficient RAM to capture snapshot. Recharge or find more resources."
        self.game_state.consume_resources(ram=50)

        # Simulate capturing raw data from RAM
        # This is a simplified representation; in a real game, this would be more complex
        data_fragments = []
        possible_data = [
            "auth_token: 1a2b3c4d5e6f",
            "encryption_key: XOR_KEY_ABC",
            "cached_input: user_login_attempt",
            "temp_password: guestpass",
            "network_session_id: 987654321",
            "process_handle: 0xDEADBEEF",
            "recent_command: ls -la /var/log",
            "partial_file_content: This is a secret message...",
            "api_endpoint: /admin/users/",
            "debug_log: Error at line 123, function xyz",
            "clipboard_data: sensitive_info_copy",
            "dns_query: example.com",
            "open_port_info: 8080/TCP",
            "kernel_module_load: netfilter.ko",
            "system_call_trace: sys_read(fd, buf, count)"
        ]

        num_fragments = random.randint(5, 15)
        for _ in range(num_fragments):
            data_fragments.append(random.choice(possible_data))
        
        self.last_dump = "\n".join(data_fragments)
        self.game_state.ids.increment_anomaly_score(30, "Volatile memory dump captured")
        return f"RAM snapshot captured. Size: {len(self.last_dump)} bytes."

    def analyze_dump(self, keyword=None):
        if not self.last_dump:
            return "No RAM dump available to analyze. Use 'memdump' first."

        if self.game_state.cpu_cycles < 20: # Example resource cost
            return "Error: Insufficient CPU cycles to analyze dump. Recharge or find more resources."
        self.game_state.consume_resources(cpu=20)

        lines = self.last_dump.splitlines()
        if keyword:
            results = [line for line in lines if keyword.lower() in line.lower()]
            if results:
                return "Analysis Results (filtered by keyword):\n" + "\n".join(results)
            else:
                return f"No data found matching '{keyword}' in the dump."
        else:
            return "Full RAM Dump Analysis:\n" + self.last_dump

# Example Usage
if __name__ == "__main__":
    from game_state import GameState
    from ids import IDS

    class MockNetwork:
        def __init__(self):
            pass
        def get_device(self, device_id):
            return None

    gs = GameState()
    gs.ram = 100 # Ensure enough RAM for example
    gs.cpu_cycles = 100 # Ensure enough CPU for example
    gs.ids = IDS(gs, None) # Mock IDS

    memdump_tool = Memdump(gs)

    print("--- Capturing RAM Snapshot ---")
    print(memdump_tool.capture_ram_snapshot())
    print(f"Current RAM: {gs.ram}")
    print(f"Current Anomaly Score: {gs.ids.anomaly_score}")

    print("\n--- Analyzing Full Dump ---")
    print(memdump_tool.analyze_dump())
    print(f"Current CPU: {gs.cpu_cycles}")

    print("\n--- Analyzing Dump with Keyword 'token' ---")
    print(memdump_tool.analyze_dump(keyword="token"))

    print("\n--- Analyzing Dump with Keyword 'nonexistent' ---")
    print(memdump_tool.analyze_dump(keyword="nonexistent"))
