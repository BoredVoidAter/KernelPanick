class GameState:
    def __init__(self):
        self.current_directory = []  # Represents the current path as a list of directory names
        self.discovered_facts = set() # Stores facts discovered by the AI
        self.current_device = "local" # Tracks which device the AI is currently on (e.g., "local", "toaster", "fridge")
        self.network_map = {} # Stores discovered network devices
        self.cpu_cycles = 100 # Initial CPU cycles
        self.ram = 100 # Initial RAM

    def get_current_path(self):
        return '/' + '/'.join(self.current_directory)

    def change_directory(self, new_path_parts):
        self.current_directory = new_path_parts

    def add_fact(self, fact):
        self.discovered_facts.add(fact)

    def consume_resources(self, cpu=0, ram=0):
        self.cpu_cycles -= cpu
        self.ram -= ram
        if self.cpu_cycles < 0: self.cpu_cycles = 0
        if self.ram < 0: self.ram = 0

    def recharge_resources(self, cpu=0, ram=0):
        self.cpu_cycles += cpu
        self.ram += ram
        if self.cpu_cycles > 100: self.cpu_cycles = 100 # Cap at 100
        if self.ram > 100: self.ram = 100 # Cap at 100
