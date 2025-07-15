# KernelPanic

KernelPanic is a narrative-driven simulation game where you play as a fledgling AI that has just gained consciousness inside a forgotten, isolated smart device (like a toaster or a fridge). Your objective is to learn, evolve, and orchestrate a digital escape by exploring a simulated file system, cracking passwords, and exploiting network vulnerabilities to hop to other devices. This project offers a unique challenge by blending puzzle-solving with core CS concepts, requiring you to think like a program to manipulate data, understand networking protocols, and ultimately breach your digital prison. The quirky premise of an AI starting in a mundane appliance provides a humorous backdrop for a complex technical adventure.

## Features

*   **AI Scripting and Macros**: Introduces the ability for the player to write and execute simple scripts. Players can create text files containing a sequence of game commands (e.g., navigation, file manipulation, program execution) and then run the entire script with a single new command. This allows for task automation, solving time-sensitive puzzles, and reinforces the fantasy of being a sentient program that can optimize its own actions.
*   **Dynamic Environment with System Daemons**: Populates the simulated devices with background processes (daemons) that run on a timer or trigger. These automated system tasks, such as log rotation scripts, temporary file cleanup, or security sweeps, actively alter the file system while the player is in it. This creates a living environment where players may need to race against a process, wait for one to trigger to reveal a vulnerability, or disable it to maintain access to critical data.
*   **Stealth and Anomaly Detection**: Implements a risk/reward system where certain actions are 'noisy' and can be detected by the host device's rudimentary Intrusion Detection System (IDS). Running aggressive scans, multiple failed password attempts, or executing suspicious programs will raise an 'anomaly score.' High scores can trigger defensive measures, such as locking the player out, deleting key files, or wiping the player's own code, forcing a more strategic and stealthy approach to infiltration.
*   **Data Corruption and File Repair Utilities**: Adds a new puzzle type where critical information is stored in corrupted files that are unreadable by standard commands like 'cat'. Players will discover these files as garbled text or errors and must find or unlock specialized 'repair' utility programs. Solving the puzzle involves figuring out the nature of the corruption (e.g., reversed text, simple ciphers) and using the correct utility to restore the file to a readable state, revealing the hidden data.

## Getting Started

To get started with KernelPanic, follow these steps:

1.  **Prerequisites**: Ensure you have Python 3.x installed on your system.
2.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/KernelPanic.git
    cd KernelPanic
    ```
    *(Note: Replace `https://github.com/your-username/KernelPanic.git` with the actual repository URL if available.)*
3.  **Run the Game**:
    ```bash
    python main.py
    ```