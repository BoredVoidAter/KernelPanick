import os
from network import Network

class CLI:
    def __init__(self, game_state, file_system, network):
        self.game_state = game_state
        self.file_system = file_system
        self.network = network
        self.commands = {
            'ls': self._ls_command,
            'cd': self._cd_command,
            'cat': self._cat_command,
            'scan': self._scan_command,
            'hop': self._hop_command,
            'status': self._status_command,
            'recharge': self._recharge_command,
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

    def _help_command(self, args):
        print("Available commands:")
        print("  ls [path]    - List contents of current or specified directory.")
        print("  cd <path>    - Change current directory.")
        print("  cat <file> [password] - Display content of a file. Provide password for protected files.")
        print("  help         - Display this help message.")
        print("  exit         - Exit the game.")

    def _exit_command(self, args):
        print("Shutting down AI core. Goodbye.")
        exit()
