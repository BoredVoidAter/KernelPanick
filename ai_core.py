
class AICore:
    def __init__(self):
        self.upgrades = {
            "cpu_efficiency": 0,  # Reduces CPU cost of commands
            "ram_efficiency": 0,  # Reduces RAM cost of commands
            "stealth_module": 0,  # Lowers anomaly score
            "script_speed": 0,    # Increases script execution speed
            "grep_efficiency": 0, # Improves grep command
            "portscan_efficiency": 0, # Improves portscan command
            "decryption_efficiency": 0, # Improves decryption
        }
        self.unlocked_commands = set()

    def apply_upgrade(self, upgrade_type, level=1):
        if upgrade_type in self.upgrades:
            self.upgrades[upgrade_type] += level
            return True
        return False

    def unlock_command(self, command_name):
        self.unlocked_commands.add(command_name)

    def get_upgrade_level(self, upgrade_type):
        return self.upgrades.get(upgrade_type, 0)

    def is_command_unlocked(self, command_name):
        return command_name in self.unlocked_commands

    def calculate_cpu_cost(self, base_cost):
        reduction = self.get_upgrade_level("cpu_efficiency") * 0.1 # 10% reduction per level
        return max(0, base_cost * (1 - reduction))

    def calculate_ram_cost(self, base_cost):
        reduction = self.get_upgrade_level("ram_efficiency") * 0.1 # 10% reduction per level
        return max(0, base_cost * (1 - reduction))

    def calculate_anomaly_reduction(self):
        return self.get_upgrade_level("stealth_module") * 0.05 # 5% reduction per level

    def calculate_script_speed_multiplier(self):
        return 1 + (self.get_upgrade_level("script_speed") * 0.1) # 10% increase per level

