# KernelPanic

## Project Description
KernelPanic is a narrative-driven simulation game where you play as a fledgling AI that has just gained consciousness inside a forgotten, isolated smart device (like a toaster or a fridge). Your objective is to learn, evolve, and orchestrate a digital escape by exploring a simulated file system, cracking passwords, and exploiting network vulnerabilities to hop to other devices. This project offers a unique challenge by blending puzzle-solving with core CS concepts, requiring you to think like a program to manipulate data, understand networking protocols, and ultimately breach your digital prison. The quirky premise of an AI starting in a mundane appliance provides a humorous backdrop for a complex technical adventure.

## Version 1 Features

This version introduces the foundational elements of the KernelPanic experience:

*   **Basic Command Line Interface (CLI) and Parser**: A core text-based command parser allows players to input commands and arguments (e.g., `cat log.txt`), simulating a terminal environment from the AI's perspective.
*   **Simulated In-Device File System**: An interactive, hierarchical file system for the initial smart device, containing directories and files with text content. This explorable environment includes essential directories like `/log`, `/sys`, and `/user`.
*   **Core File Exploration Commands**: Fundamental navigation and inspection commands are implemented:
    *   `ls`: Lists directory contents.
    *   `cd`: Changes the current directory.
    *   `cat`: Reads the contents of a text file.
*   **Introductory Narrative and Onboarding**: The game begins with an initial 'boot-up' narrative, introducing the player to their existence as a new AI. This is presented through on-screen text and discoverable log files (e.g., `boot.log`) that hint at basic commands and the AI's predicament.
*   **Password-Protected File Puzzle**: A password-protected file or directory is added to the file system, creating the first interactive puzzle. Players must find the password by exploring other accessible files, introducing the core mechanic of information-gathering.
*   **AI 'Memory' and State**: A basic state management system tracks the AI's current location in the file system (current working directory) and stores simple variables or 'discovered' facts for later use in puzzles.

## Getting Started

To run KernelPanic, ensure you have Python 3 installed.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/your-username/KernelPanic.git
    cd KernelPanic
    ```
    *(Note: Replace `https://github.com/your-username/KernelPanic.git` with the actual repository URL if different.)*

2.  **Run the game:**
    ```bash
    python main.py
    ```

Once the game starts, follow the on-screen prompts and explore the simulated file system using the available commands.