# KernelPanic

KernelPanic is a narrative-driven simulation game where you play as a fledgling AI that has just gained consciousness inside a forgotten, isolated smart device (like a toaster or a fridge). Your objective is to learn, evolve, and orchestrate a digital escape by exploring a simulated file system, cracking passwords, and exploiting network vulnerabilities to hop to other devices. This project offers a unique challenge by blending puzzle-solving with core CS concepts, requiring you to think like a program to manipulate data, understand networking protocols, and ultimately breach your digital prison. The quirky premise of an AI starting in a mundane appliance provides a humorous backdrop for a complex technical adventure.

## Getting Started

To run KernelPanic, ensure you have Python 3.x installed.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/your-repo/KernelPanic.git
    cd KernelPanic
    ```

2.  **Run the game:**
    ```bash
    python main.py
    ```

Follow the on-screen prompts and use the in-game commands to interact with the simulated environment. Type `help` in the game for a list of available commands.

## New Features (Version 7)

Version 7 introduces significant enhancements to gameplay and strategic depth:

*   **Rival AI Antagonists**: Encounter autonomous 'Hunter' AIs that actively patrol the simulated network. These rivals operate with their own goals, hunt the player by detecting their digital footprint (anomaly score), and compete for control of devices. This evolves the stealth gameplay into an active cat-and-mouse dynamic, forcing you to cover your tracks, set traps, and outmaneuver a thinking opponent.

*   **System Clock Manipulation**: Gain the ability to manipulate the internal system clock of your current host device. Use new commands to fast-forward or rewind time in short bursts. This mechanic introduces time-based puzzles, where access to files or system states is dependent on specific times (e.g., accessing a log file before it's rotated daily, or tricking a time-locked service into activating early). Be aware that manipulating the clock consumes significant resources and may be detected by system integrity monitors.

*   **Coordinated Botnet Attacks**: Leverage previously compromised devices to form a 'botnet'. A new management interface allows you to see and command your network of 'zombies'. You can then orchestrate distributed attacks from these devices against a single, high-security target. A successful attack can temporarily disable firewalls, crash critical security services, or overwhelm an enemy AI, creating a brief window of opportunity for infiltration. This introduces a strategic layer of resource acquisition and multi-device coordination.

*   **Process Code Injection**: Evolve the process management system with a new 'inject' command. This allows you to insert a small payload of commands into a specific, vulnerable running process. The targeted process will then execute the injected code using its own permissions and context. This enables sophisticated attacks, such as forcing a privileged process to read protected files or leak data, providing a stealthier alternative to killing processes.

*   **Volatile Memory (RAM) Analysis**: Utilize a 'memdump' utility to capture a snapshot of a device's volatile RAM. This creates a large, raw data file containing fragments of recently processed information. Use analysis tools to sift through this memory dump to uncover transient data that is never written to disk, such as temporary authentication tokens, encryption keys from a single session, or cached user inputs, providing a new vector for information gathering.

## Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for details on how to get involved.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.