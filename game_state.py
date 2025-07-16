class GameState:
    def __init__(self):
        self.current_directory = []  # Represents the current path as a list of directory names
        self.discovered_facts = set() # Stores facts discovered by the AI

    def get_current_path(self):
        return '/' + '/'.join(self.current_directory)

    def change_directory(self, new_path_parts):
        self.current_directory = new_path_parts

    def add_fact(self, fact):
        self.discovered_facts.add(fact)
