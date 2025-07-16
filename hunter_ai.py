

class HunterAI:
    def __init__(self, name, network_map):
        self.name = name
        self.network_map = network_map
        self.current_device = None
        self.target_device = None
        self.anomaly_threshold = 50  # Anomaly score threshold to detect player

    def set_current_device(self, device):
        self.current_device = device

    def patrol(self):
        # Simple patrolling logic: move to a random connected device
        if self.current_device and self.current_device.connections:
            next_device = random.choice(list(self.current_device.connections.keys()))
            print(f"{self.name} patrolling to {next_device}")
            self.current_device = self.network_map.get_device(next_device)
        else:
            print(f"{self.name} has nowhere to patrol.")

    def detect_player(self, player_anomaly_score, player_location):
        if player_anomaly_score > self.anomaly_threshold:
            print(f"{self.name} detected high anomaly score from player at {player_location}!")
            self.target_device = player_location
            return True
        return False

    def hunt_player(self):
        if self.target_device:
            print(f"{self.name} is hunting player at {self.target_device}")
            # In a real game, this would involve pathfinding and moving towards the player
            # For now, let's just say it "arrives" at the target device
            self.current_device = self.network_map.get_device(self.target_device)
            self.target_device = None # Reset target after "reaching" it
        else:
            print(f"{self.name} has no target to hunt.")

    def compete_for_device(self, device):
        print(f"{self.name} is competing for control of {device.name}")
        # This would involve some game logic for taking over a device
        # For now, let's just say it attempts to gain control
        if random.random() < 0.3: # 30% chance to gain control
            device.set_owner(self.name)
            print(f"{self.name} gained control of {device.name}!")
            return True
        else:
            print(f"{self.name} failed to gain control of {device.name}.")
            return False

# Example Usage (requires Network and Device classes from other modules)
if __name__ == "__main__":
    import random
    from network import Network, Device # Assuming these exist

    # Create a dummy network for testing
    net = Network()
    dev1 = Device("device1", "192.168.1.1", "router")
    dev2 = Device("device2", "192.168.1.2", "server")
    dev3 = Device("device3", "192.168.1.3", "workstation")
    net.add_device(dev1)
    net.add_device(dev2)
    net.add_device(dev3)
    net.add_connection("device1", "device2")
    net.add_connection("device2", "device3")

    hunter = HunterAI("Sentinel", net)
    hunter.set_current_device(dev1)

    print("\n--- Hunter AI Patrol ---")
    hunter.patrol()
    print(f"Hunter is now at: {hunter.current_device.name}")

    print("\n--- Hunter AI Detection ---")
    player_anomaly = 70
    player_loc = dev3
    if hunter.detect_player(player_anomaly, player_loc):
        hunter.hunt_player()
        print(f"Hunter is now at: {hunter.current_device.name}")

    print("\n--- Hunter AI Competition ---")
    hunter.set_current_device(dev2) # Move hunter to dev2 for competition
    hunter.compete_for_device(dev2)
    print(f"Device2 owner: {dev2.owner}")
