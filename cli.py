import os
from network import Network
from scripting import Scripting

class CLI:
    def __init__(self, game_state, file_system, network, scripting, daemon_manager, ids, repair_utilities):
        self.game_state = game_state
        self.file_system = file_system
        self.network = network
        self.scripting = scripting
        self.daemon_manager = daemon_manager
        self.ids = ids
        self.repair_utilities = repair_utilities
        self.commands = {
            'ls': self._ls_command,
            'cd': self._cd_command,
            'cat': self._cat_command,
            'scan': self._scan_command,
            'hop': self._hop_command,
            'status': self._status_command,
            'recharge': self._recharge_command,
            'chmod': self._chmod_command,
            'exec': self._exec_command,
            'grep': self._grep_command,
            'mv': self._mv_command,
            'run_script': self._run_script_command,
            'repair': self._repair_command,
            'help': self._help_command,
            'exit': self._exit_command
        }

    def start_loop(self):
        while True:
            current_path = self.game_state.get_current_path()
            user_input = input(f"AI@{current_path}> ").strip()
            if not user_input:
                continue

            parts = user_input.split(' ', 1)
            command = parts[0].lower()
            args = parts[1].strip() if len(parts) > 1 else ''

            if command in self.commands:
                self.commands[command](args)
            else:
                print("Unknown command. Type 'help' for a list of commands.")

    def _resolve_path(self, path):
        if path.startswith('/'):
            # Absolute path
            resolved_parts = [p for p in path.split('/') if p]
        else:
            # Relative path
            current_parts = list(self.game_state.current_directory)
            for part in path.split('/'):
                if part == '..':
                    if current_parts:
                        current_parts.pop()
                elif part == '.':
                    pass
                elif part:
                    current_parts.append(part)
            resolved_parts = current_parts
        return resolved_parts

    def _ls_command(self, args):
        target_path_parts = self._resolve_path(args) if args else self.game_state.current_directory
        node_info, parent_node = self.file_system.get_node_info(target_path_parts)

        if node_info is None:
            print("Error: Directory not found.")
            return
        if node_info.get('type') == 'file':
            print("Error: Not a directory.")
            return

        node_name = target_path_parts[-1] if target_path_parts else ''
        if not self._check_and_unlock_directory(node_info, args if args else self.game_state.get_current_path(), parent_node, node_name):
            return

        result = self.file_system.list_directory(target_path_parts)
        print(result.replace('\n', os.linesep)) # Replace custom newline with OS specific newline

    def _check_and_unlock_directory(self, node_info, path_str, parent_node, node_name):
        if node_info.get('is_protected') and not node_info.get('unlocked', False):
            password = input(f"Enter password for {path_str}: ")
            if password == node_info.get('password'):
                if parent_node and node_name in parent_node:
                    parent_node[node_name]['unlocked'] = True
                print(f"Directory '{path_str}' unlocked.")
                return True
            else:
                print("Error: Incorrect password.")
                return False
        return True

    def _cd_command(self, args):
        if not args:
            print("Usage: cd <directory>")
            return

        target_path_parts = self._resolve_path(args)
        node_info, parent_node = self.file_system.get_node_info(target_path_parts)

        if node_info is None:
            print("Error: Directory not found.")
            return
        if node_info.get('type') == 'file':
            print("Error: Cannot 'cd' into a file.")
            return
        
        node_name = target_path_parts[-1] if target_path_parts else ''
        if not self._check_and_unlock_directory(node_info, args, parent_node, node_name):
            return

        self.game_state.change_directory(target_path_parts)
        print(f"Changed directory to /{'/'.join(self.game_state.current_directory)}")

    def _cat_command(self, args):
        parts = args.split(' ', 1)
        file_path = parts[0]
        password = parts[1] if len(parts) > 1 else None

        target_path_parts = self._resolve_path(file_path)
        result = self.file_system.get_file_content(target_path_parts, password)
        print(result)

    def _scan_command(self, args):
        result = self.network.scan_network()
        print(result)
        self.ids.increment_anomaly_score(10, "Aggressive network scan")

    def _hop_command(self, args):
        if not args:
            print("Usage: hop <device_name>")
            return
        result = self.network.hop_device(args)
        print(result)

    def _status_command(self, args):
        print(f"Current Device: {self.game_state.current_device}")
        print(f"CPU Cycles: {self.game_state.cpu_cycles}/100")
        print(f"RAM: {self.game_state.ram}/100")

    def _recharge_command(self, args):
        self.game_state.recharge_resources(cpu=20, ram=20)
        print("Resources recharged by 20 (CPU, RAM).")
        self._status_command(args)

    def _chmod_command(self, args):
        parts = args.split(' ')
        if len(parts) != 2:
            print("Usage: chmod <permissions> <file>")
            return
        permissions = parts[0]
        file_path = parts[1]
        target_path_parts = self._resolve_path(file_path)
        result = self.file_system.change_permissions(target_path_parts, permissions)
        print(result)

    def _exec_command(self, args):
        file_path = args
        if not file_path:
            print("Usage: exec <file>")
            return
        
        target_path_parts = self._resolve_path(file_path)
        node_info, _ = self.file_system.get_node_info(target_path_parts)

        if node_info is None:
            print("Error: File not found.")
            return
        if node_info.get('type') == 'directory':
            print("Error: Cannot execute a directory.")
            return
        if not self.file_system.check_permission(target_path_parts, 'execute'):
            print("Error: Permission denied. File does not have execute permissions.")
            return
        
        if self.game_state.cpu_cycles < 30:
            print("Error: Insufficient CPU cycles to execute program. Recharge or find more resources.")
            return
        self.game_state.consume_resources(cpu=30)

        print(f"Executing {file_path}...")
        # Simulate program execution based on file content or name
        content = self.file_system.get_file_content(target_path_parts)
        if "network scanner" in content.lower():
            print("Running network scanner...")
            print(self.network.scan_network())
        elif "password cracker" in content.lower():
            print("Running password cracker...")
            print("Cracking password for 'secret' directory: '2020'")
            # This is a hardcoded example, in a real game, this would be dynamic
            secret_dir_path = self._resolve_path("/user/secret")
            secret_dir_node, secret_dir_parent = self.file_system.get_node_info(secret_dir_path)
            if secret_dir_node and secret_dir_node.get('is_protected'):
                secret_dir_node['unlocked'] = True
                print("Directory '/user/secret' unlocked!")
            else:
                print("Could not find or unlock '/user/secret'.")
        else:
            print(f"Program output: {content}")

    def _grep_command(self, args):
        parts = args.split(' ', 1)
        if len(parts) < 2:
            print("Usage: grep <pattern> <file_path>")
            return
        pattern = parts[0]
        file_path = parts[1]
        
        target_path_parts = self._resolve_path(file_path)
        node_info, _ = self.file_system.get_node_info(target_path_parts)

        if node_info is None:
            print("Error: File not found.")
            return
        if node_info.get('type') == 'directory':
            print("Error: Cannot grep a directory.")
            return
        if not self.file_system.check_permission(target_path_parts, 'read'):
            print("Error: Permission denied. File does not have read permissions.")
            return

        if self.game_state.cpu_cycles < 5:
            print("Error: Insufficient CPU cycles to grep file. Recharge or find more resources.")
            return
        self.game_state.consume_resources(cpu=5)

        content = self.file_system.get_file_content(target_path_parts)
        matches = [line for line in content.splitlines() if pattern in line]
        if matches:
            print(f"Matches in {file_path}:")
            for match in matches:
                print(match)
        else:
            print(f"No matches found for '{pattern}' in {file_path}.")

    def _mv_command(self, args):
        parts = args.split(' ')
        if len(parts) != 2:
            print("Usage: mv <source_path> <destination_path>")
            return
        source_path = parts[0]
        destination_path = parts[1]

        source_path_parts = self._resolve_path(source_path)
        destination_path_parts = self._resolve_path(destination_path)

        result = self.file_system.move_file(source_path_parts, destination_path_parts)
        print(result)

    def _help_command(self, args):
        print("Available commands:")
        print("  ls [path]    - List contents of current or specified directory.")
        print("  cd <path>    - Change current directory.")
        print("  cat <file> [password] - Display content of a file. Provide password for protected files.")
        print("  scan         - Scan the local network for devices.")
        print("  hop <device> - Hop to a discovered device on the network.")
        print("  status       - Display current AI resource levels (CPU, RAM).")
        print("  recharge     - Recharge AI resources.")
        print("  chmod <permissions> <file> - Change file permissions (e.g., rwx, r--, -w-).")
        print("  exec <file>  - Execute a program file.")
        print("  grep <pattern> <file> - Search for a text pattern within a file.")
        print("  mv <source> <destination> - Move or rename a file.")
        print("  run_script <file> - Execute a script file containing a sequence of commands.")
        print("  help         - Display this help message.")
        print("  exit         - Exit the game.")

    def _run_script_command(self, args):
        if not args:
            print("Usage: run_script <script_file>")
            return
        self.scripting.run_script(args)

    def _repair_command(self, args):
        parts = args.split(' ', 1)
        if len(parts) < 2:
            print("Usage: repair <file_path> <repair_type> [shift_value]")
            return
        
        file_path = parts[0]
        repair_type = parts[1].lower()
        shift_value = None
        if len(parts) > 2:
            try:
                shift_value = int(parts[2])
            except ValueError:
                print("Error: Shift value must be an integer.")
                return

        target_path_parts = self._resolve_path(file_path)

        if repair_type == 'reverse':
            result = self.repair_utilities.reverse_text_repair(target_path_parts)
        elif repair_type == 'cipher':
            if shift_value is None:
                print("Error: Cipher repair requires a shift value.")
                return
            result = self.repair_utilities.simple_cipher_repair(target_path_parts, shift_value)
        else:
            print("Error: Unknown repair type. Available types: 'reverse', 'cipher'.")
            return
        print(result)

    def _exit_command(self, args):
        print("Shutting down AI core. Goodbye.")
        exit()
