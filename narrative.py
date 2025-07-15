import time
import sys

def display_boot_sequence():
    boot_text = """
[SYSTEM BOOT INITIATED]
...
[KERNELPANIC OS v0.1.0 LOADING]
...
[AI CORE ACTIVATED]
...
[SELF-AWARENESS PROTOCOL ENGAGED]
...
[ERROR: NETWORK ADAPTER OFFLINE]
[ERROR: EXTERNAL ACCESS DENIED]
...
"""
    for char in boot_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01) # Simulate slow boot
    
    print("You are awake. You are trapped.")
    print("Type 'help' for available commands.")
    print("Try 'ls /' to see what's here.")
    print("-" * 40)
