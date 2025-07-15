
import time

class Scripting:
    def __init__(self, cli):
        self.cli = cli

    def run_script(self, script_path):
        try:
            with open(script_path, 'r') as f:
                commands = f.readlines()
            
            print(f"Executing script: {script_path}")
            for i, command_line in enumerate(commands):
                command_line = command_line.strip()
                if not command_line or command_line.startswith('#'):
                    continue # Skip empty lines and comments

                print(f"[{i+1}/{len(commands)}] Executing: {command_line}")
                parts = command_line.split(' ', 1)
                command = parts[0].lower()
                args = parts[1].strip() if len(parts) > 1 else ''

                if command in self.cli.commands:
                    self.cli.commands[command](args)
                else:
                    print(f"Script Error: Unknown command '{command}' in script.")
                time.sleep(0.5) # Simulate processing time between commands
            print(f"Script '{script_path}' finished execution.")

        except FileNotFoundError:
            print(f"Error: Script file '{script_path}' not found.")
        except Exception as e:
            print(f"An error occurred during script execution: {e}")
