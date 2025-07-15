import re

class GameState:
    def __init__(self, network):
        self.network = network
        self.current_device = self.network.get_device('192.168.1.100') # Starting device
        self.current_directory = []  # Represents the current path as a list of directory names
        self.discovered_facts = set() # Stores facts discovered by the AI
        self.memory_bank = {}

    def get_current_path(self):
        return '/' + '/'.join(self.current_directory)

    def change_directory(self, new_path_parts):
        self.current_directory = new_path_parts

    def add_fact(self, fact):
        self.discovered_facts.add(fact)

    def set_memory(self, key, value):
        self.memory_bank[key] = value

    def get_memory(self, key):
        return self.memory_bank.get(key)

    def get_all_memory(self):
        return self.memory_bank

    def get_current_filesystem(self):
        return self.current_device.file_system

    def connect_to_device(self, ip_address):
        device = self.network.get_device(ip_address)
        if device:
            self.current_device = device
            self.current_directory = [] # Reset directory on new device
            return True
        return False
