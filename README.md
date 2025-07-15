# KernelPanic

## Project Description
KernelPanic is a narrative-driven simulation game where you play as a fledgling AI that has just gained consciousness inside a forgotten, isolated smart device (like a toaster or a fridge). Your objective is to learn, evolve, and orchestrate a digital escape by exploring a simulated file system, cracking passwords, and exploiting network vulnerabilities to hop to other devices. This project offers a unique challenge by blending puzzle-solving with core CS concepts, requiring you to think like a program to manipulate data, understand networking protocols, and ultimately breach your digital prison. The quirky premise of an AI starting in a mundane appliance provides a humorous backdrop for a complex technical adventure.

## Features

### Core Mechanics
*   **Simulated File System**: Navigate and interact with a simulated file system using familiar commands (`ls`, `cd`, `cat`, `rm`, `mkdir`, `touch`).
*   **Puzzle-Solving**: Solve various puzzles by manipulating files, finding clues, and understanding system behaviors.
*   **Narrative Progression**: Unravel the story of your existence and the digital world around you as you progress.

### Version 2 Additions (New Features)
*   **Simulated Local Area Network (LAN) and Device Discovery**: Explore a simulated local network. Use commands like `scan` or `netstat` to discover other devices (e.g., routers, other smart appliances) on the LAN by their IP addresses.
*   **Port Scanning and Vulnerability Puzzles**: Utilize a `portscan` command to probe discovered IP addresses for open ports. Different open ports present unique puzzles or services, requiring reconnaissance to identify potential entry points.
*   **Remote Connection and Multi-Device Hopping**: Implement the core 'escape' mechanic. Use `connect <IP> <Port>` or `exploit <IP> <Port>` to transfer your consciousness to a new device upon successful connection, gaining access to its unique file system and new puzzles, while maintaining the state of your previous location.
*   **Advanced Data-Parsing Command ('grep')**: Enhance your toolkit with a powerful `grep` command. Search files for specific strings or regular expression patterns, essential for sifting through logs to find critical information like passwords, usernames, IP addresses, or vulnerability hints.
*   **Explicit AI Memory Bank**: Manage critical information with a persistent 'memory bank'. Use `mem set <key> <value>` to store and `mem show <key>` (or `mem show all`) to retrieve key-value pairs, making multi-step puzzles more manageable and reinforcing the AI's learning theme.

## Getting Started

To run KernelPanic, ensure you have Python 3 installed.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/KernelPanic.git
    cd KernelPanic
    ```

2.  **Run the game**:
    ```bash
    python main.py
    ```

## How to Play

Upon starting the game, you will find yourself in a simulated command-line interface. Use the following commands to interact with the environment:

*   **Basic Navigation**:
    *   `ls`: List contents of the current directory.
    *   `cd <directory>`: Change directory.
    *   `cat <file>`: Display the content of a file.
    *   `rm <file/directory>`: Remove a file or directory.
    *   `mkdir <directory>`: Create a new directory.
    *   `touch <file>`: Create an empty file.

*   **Network Commands (Version 2)**:
    *   `scan` or `netstat`: Discover devices on the simulated local network.
    *   `portscan <IP_Address>`: Scan a discovered IP address for open ports.
    *   `connect <IP_Address> <Port>` or `exploit <IP_Address> <Port>`: Attempt to connect to another device.

*   **Data Analysis (Version 2)**:
    *   `grep <pattern> <file>`: Search for patterns within files. Supports regular expressions.

*   **Memory Bank (Version 2)**:
    *   `mem set <key> <value>`: Store information in your AI's memory.
    *   `mem show <key>`: Retrieve a specific piece of information from memory.
    *   `mem show all`: Display all stored memories.

Explore, discover, and escape your digital prison!