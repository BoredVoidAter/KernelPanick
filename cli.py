import os
from network import Network
from scripting import Scripting
from memory import AIMemory
from packet_sniffer import PacketSniffer
from ai_fork import AIFork

class CLI:
    def __init__(self, game_state, file_system, network, scripting, daemon_manager, ids, repair_utilities, process_manager, network_recon, cryptography_manager, ai_core):
        self.game_state = game_state
        self.file_system = file_system
        self.network = network
        self.scripting = scripting
        self.daemon_manager = daemon_manager
        self.ids = ids
        self.repair_utilities = repair_utilities
        self.process_manager = process_manager
        self.network_recon = network_recon
        self.cryptography_manager = cryptography_manager
        self.ai_core = ai_core
        self.memory = AIMemory()
        self.packet_sniffer = PacketSniffer(network, game_state, ids)
        self.ai_fork = AIFork(game_state, ids, ai_core)
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
            'ps': self._ps_command,
            'kill': self._kill_command,
            'portscan': self._portscan_command,
            'decrypt': self._decrypt_command,
            'upgrade': self._upgrade_command,
            'store': self._store_command,
            'retrieve': self._retrieve_command,
            'tag': self._tag_command,
            'list_memory': self._list_memory_command,
            'sniff': self._sniff_command,
            'save_packets': self._save_packets_command,
            'fork': self._fork_command,
            'risky_action': self._risky_action_command,
            'terminate_fork': self._terminate_fork_command,
            'fork_status': self._fork_status_command,
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
        if node_info.get('is_honeypot'):
            self.ids.increment_anomaly_score(50, "Interaction with honeypot directory (ls)")
            print("Access Denied: This directory appears to be a trap. Anomaly detected!")
            return

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

        if node_info.get('is_honeypot'):
            self.ids.increment_anomaly_score(50, "Interaction with honeypot directory (cd)")
            print("Access Denied: This directory appears to be a trap. Anomaly detected!")
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

    def _ps_command(self, args):
        processes = self.process_manager.list_processes()
        if not processes:
            print("No processes running.")
            return
        print("PID	Name	Owner	CPU%	RAM%	Status")
        for p in processes:
            print(f"{p.pid}	{p.name}	{p.owner}	{p.cpu_usage}	{p.ram_usage}	{p.status}")

    def _kill_command(self, args):
        try:
            pid = int(args)
        except ValueError:
            print("Usage: kill <PID>")
            return
        
        if self.process_manager.terminate_process(pid):
            print(f"Process {pid} terminated.")
        else:
            print(f"Error: Process {pid} not found or could not be terminated.")

    def _portscan_command(self, args):
        parts = args.split(' ')
        if len(parts) < 2:
            print("Usage: portscan <target_device_id> <ports_to_scan> [aggressive]")
            return
        
        target_device_id = parts[0]
        ports_str = parts[1]
        aggressive = False
        if len(parts) > 2 and parts[2].lower() == "aggressive":
            aggressive = True

        try:
            ports_to_scan = [int(p) for p in ports_str.split(',')]
        except ValueError:
            print("Error: Ports must be a comma-separated list of numbers (e.g., '22,80,443').")
            return

        if aggressive:
            self.ids.increment_anomaly_score(self.ai_core.calculate_anomaly_reduction(), "Aggressive portscan")

        results = self.network_recon.simulate_portscan(self.game_state.current_device, target_device_id, ports_to_scan, aggressive)
        if "error" in results:
            print(f"Error: {results['error']}")
            return
        
        print(f"Portscan results for {target_device_id}:")
        for port, status in results.items():
            print(f"Port {port}: {'Open' if status['open'] else 'Closed'} - {status['message']}")

    def _decrypt_command(self, args):
        parts = args.split(' ')
        if len(parts) < 2:
            print("Usage: decrypt <file_path> <algorithm> [key]")
            return
        
        file_path = parts[0]
        algorithm = parts[1].upper()
        key = parts[2] if len(parts) > 2 else None

        target_path_parts = self._resolve_path(file_path)
        node_info, _ = self.file_system.get_node_info(target_path_parts)

        if node_info is None:
            print("Error: File not found.")
            return
        if node_info.get('type') == 'directory':
            print("Error: Cannot decrypt a directory.")
            return
        if not self.file_system.check_permission(target_path_parts, 'read'):
            print("Error: Permission denied. File does not have read permissions.")
            return

        content = self.file_system.get_file_content(target_path_parts)
        decrypted_content, message = self.cryptography_manager.decrypt_file(content, algorithm, key)

        if decrypted_content:
            print(f"Decryption successful. Content:
{decrypted_content}")
            # Optionally, update the file content in the file system
            self.file_system.write_file(target_path_parts, decrypted_content)
        else:
            print(f"Decryption failed: {message}")

    def _sniff_command(self, args):
        parts = args.split(' ')
        duration = 5
        packets_to_capture = 10
        if len(parts) > 0 and parts[0].isdigit():
            duration = int(parts[0])
        if len(parts) > 1 and parts[1].isdigit():
            packets_to_capture = int(parts[1])
        
        result = self.packet_sniffer.start_sniffing(duration, packets_to_capture)
        print(result)

    def _save_packets_command(self, args):
        if not args:
            print("Usage: save_packets <file_path>")
            return
        result = self.packet_sniffer.save_packets(self.file_system, self._resolve_path(args))
        print(result)

    def _save_packets_command(self, args):
        if not args:
            print("Usage: save_packets <file_path>")
            return
        result = self.packet_sniffer.save_packets(self.file_system, self._resolve_path(args))
        print(result)

    def _fork_command(self, args):
        parts = args.split(' ')
        cpu_limit = 20
        ram_limit = 20
        if len(parts) > 0 and parts[0].isdigit():
            cpu_limit = int(parts[0])
        if len(parts) > 1 and parts[1].isdigit():
            ram_limit = int(parts[1])
        
        result = self.ai_fork.create_fork(cpu_limit, ram_limit)
        print(result)

    def _risky_action_command(self, args):
        parts = args.split(' ', 1)
        if not parts[0]:
            print("Usage: risky_action <action_type> [target]")
            return
        action_type = parts[0]
        target = parts[1] if len(parts) > 1 else None
        
        result = self.ai_fork.perform_risky_action(action_type, target)
        print(result["message"])

    def _terminate_fork_command(self, args):
        result = self.ai_fork.terminate_fork()
        print(result)

    def _fork_status_command(self, args):
        status = self.ai_fork.get_fork_status()
        print(f"Fork Active: {status['active']}")
        print(f"Fork Resources: CPU={status['resources']['cpu']}, RAM={status['resources']['ram']}")

    def _upgrade_command(self, args):
        parts = args.split(' ')
        if len(parts) < 1:
            print("Usage: upgrade <upgrade_type> [level]")
            return
        
        upgrade_type = parts[0].lower()
        level = 1
        if len(parts) > 1:
            try:
                level = int(parts[1])
            except ValueError:
                print("Error: Upgrade level must be an integer.")
                return
        
        if self.ai_core.apply_upgrade(upgrade_type, level):
            print(f"AI Core upgraded: {upgrade_type} to level {self.ai_core.get_upgrade_level(upgrade_type)}.")
        else:
            print(f"Error: Unknown upgrade type '{upgrade_type}'.")

    def _store_command(self, args):
        if not args:
            print("Usage: store <content> [tags]")
            return
        
        parts = args.split(' tags:', 1)
        content = parts[0].strip()
        tags = [t.strip() for t in parts[1].split(',')] if len(parts) > 1 else []

        if self.memory.store_info(content, tags):
            print("Information stored in AI memory.")
        else:
            print("Failed to store information.")

    def _retrieve_command(self, args):
        if not args:
            print("Usage: retrieve <query> [tags]")
            return
        
        parts = args.split(' tags:', 1)
        query = parts[0].strip()
        tags = [t.strip() for t in parts[1].split(',')] if len(parts) > 1 else []

        results = self.memory.retrieve_info(query, tags)
        if results:
            print("Retrieved information:")
            for i, entry in enumerate(results):
                print(f"[{i}] Content: {entry['content']}")
                print(f"    Tags: {', '.join(entry['tags'])}")
        else:
            print("No matching information found.")

    def _tag_command(self, args):
        parts = args.split(' ', 1)
        if len(parts) < 2:
            print("Usage: tag <index> <new_tags>")
            return
        
        try:
            index = int(parts[0])
        except ValueError:
            print("Error: Index must be an integer.")
            return
        
        new_tags = [t.strip() for t in parts[1].split(',')]

        if self.memory.tag_info(index, new_tags):
            print(f"Tags added to memory entry {index}.")
        else:
            print("Error: Invalid index or failed to add tags.")

    def _list_memory_command(self, args):
        entries = self.memory.list_all()
        if entries:
            print("All AI memory entries:")
            for i, entry in enumerate(entries):
                print(f"[{i}] Content: {entry['content']}")
                print(f"    Tags: {', '.join(entry['tags'])}")
        else:
            print("AI memory is empty.")

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
        print("  repair <file_path> <repair_type> [shift_value] - Repair corrupted files.")
        print("  ps           - List running processes on the current device.")
        print("  kill <PID>   - Terminate a process by its PID.")
        print("  portscan <target_device_id> <ports_to_scan> [aggressive] - Scan a target device for open ports.")
        print("  decrypt <file_path> <algorithm> [key] - Decrypt an encrypted file.")
        print("  upgrade <upgrade_type> [level] - Upgrade AI core capabilities.")
        print("  store <content> [tags] - Store information in AI memory with optional tags.")
        print("  retrieve <query> [tags] - Retrieve information from AI memory based on query and tags.")
        print("  tag <index> <new_tags> - Add new tags to an existing memory entry.")
        print("  list_memory  - List all entries in AI memory.")
        print("  sniff [duration] [packets] - Start network packet sniffer.")
        print("  save_packets <file_path> - Save captured packets to a file.")
        print("  fork [cpu_limit] [ram_limit] - Create a temporary AI fork for high-risk operations.")
        print("  risky_action <action_type> [target] - Perform a risky action with the AI fork.")
        print("  terminate_fork - Terminate the active AI fork.")
        print("  fork_status  - Display the status of the AI fork.")
        print("  help         - Display this help message.")
        print("  exit         - Exit the game.")

    def _exit_command(self, args):
        print("Shutting down AI core. Goodbye.")
        exit()
