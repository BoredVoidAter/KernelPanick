import sys
from game_state import GameState
from network import Network
from cli import CLI
from narrative import display_boot_sequence

def main():
    network = Network()
    game_state = GameState(network)
    cli = CLI(game_state)

    display_boot_sequence()
    cli.start_loop()

if __name__ == "__main__":
    main()
