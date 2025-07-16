import sys
from game_state import GameState
from filesystem import FileSystem
from cli import CLI
from narrative import display_boot_sequence

def main():
    file_system = FileSystem()
    game_state = GameState()
    cli = CLI(game_state, file_system)

    display_boot_sequence()
    cli.start_loop()

if __name__ == "__main__":
    main()
