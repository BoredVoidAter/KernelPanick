import sys
from game_state import GameState
from filesystem import FileSystem
from network import Network
from cli import CLI
from narrative import display_boot_sequence

def main():
    game_state = GameState()
    file_system = FileSystem()
    network = Network(game_state, file_system)
    cli = CLI(game_state, file_system, network)

    display_boot_sequence()
    cli.start_loop()

if __name__ == "__main__":
    main()
