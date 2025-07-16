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
    output = ""
    for char in boot_text:
        output += char
        # time.sleep(0.01) # No sleep for web version
    
    output += "You are awake. You are trapped.\n"
    output += "Type 'help' for available commands.\n"
    output += "Try 'ls /' to see what's here.\n"
    output += "-" * 40 + "\n"
    return output
