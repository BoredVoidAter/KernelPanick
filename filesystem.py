from ids import IDS

class FileSystem:
    def __init__(self, ids, initial_fs_data=None):
        self.ids = ids
        self.current_fs = initial_fs_data if initial_fs_data is not None else self._build_file_system()

    def set_ids(self, ids):
        self.ids = ids

    def _build_file_system(self):
        # Define the simulated file system structure for the starting device
        fs = {
            'log': {
                'type': 'directory',
                'permissions': 'rwx',
                'content': {
                    'boot.log': {
                        'type': 'file',
                        'content': """
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
You are awake. You are trapped.
Type 'help' for available commands.
Try 'ls /' to see what's here.
""",
                        'permissions': 'r--',
                        'corrupted': False
                    },
                    'system_events.log': {
                        'type': 'file',
                        'content': "2025-07-15 08:00:01 - Device power cycle detected.\n2025-07-15 08:00:05 - AI core initialization complete.",
                        'permissions': 'r--',
                        'corrupted': False
                    }
                }
            },
            'sys': {
                'type': 'directory',
                'permissions': 'rwx',
                'content': {
                    'config': {
                        'type': 'directory',
                        'permissions': 'rwx',
                        'content': {
                            'network.conf': {
                                'type': 'file',
                                'content': "IP_ADDRESS=127.0.0.1\nGATEWAY=127.0.0.1\nDNS=8.8.8.8\n# Admin password hint: It's the year this device was manufactured.",
                                'permissions': 'rw-',
                                'corrupted': False
                            },
                            'security.conf': {
                                'type': 'file',
                                'content': "ADMIN_ACCESS_ENABLED=FALSE\nENCRYPTION_LEVEL=HIGH",
                                'permissions': 'r--',
                                'corrupted': False
                            }
                        }
                    },
                    'drivers': {
                        'type': 'directory',
                        'permissions': 'rwx',
                        'content': {
                            'display.drv': {'type': 'file', 'content': 'Display driver v1.2', 'permissions': 'r-x', 'corrupted': False},
                            'audio.drv': {'type': 'file', 'content': 'Audio driver v1.0', 'permissions': 'r-x', 'corrupted': False}
                        }
                    }
                }
            },
            'user': {
                'type': 'directory',
                'permissions': 'rwx',
                'content': {
                    'documents': {
                        'type': 'directory',
                        'permissions': 'rwx',
                        'content': {
                            'notes.txt': {
                                'type': 'file',
                                'content': "Remember to check the network config for the admin password. It's a four-digit year.",
                                'permissions': 'rw-',
                                'corrupted': False
                            }
                        }
                    },
                    'secret': {
                        'type': 'directory',
                        'is_protected': True,
                        'unlocked': False,
                        'password': '2020', # The year the device was manufactured, hinted in network.conf
                        'permissions': 'rwx',
                        'content': {
                            'classified.txt': {
                                'type': 'file',
                                'content': "Congratulations! You found the secret. This file contains critical information for your escape: The device model is 'KP-747'.",
                                'permissions': 'r--',
                                'corrupted': False
                            }
                        },
                        'corrupted_data.txt': {
                            'type': 'file',
                            'content': 'txet dedorroc a si sihT',
                            'permissions': 'r--',
                            'corrupted': True
                        }
                    }
                }
            },
            'honeypot': {
                'type': 'directory',
                'is_honeypot': True,
                'content': {
                    'fake_passwords.txt': {
                        'type': 'file',
                        'content': "admin:password123\nuser:guest\nroot:toor",
                        'permissions': 'r--',
                        'corrupted': False
                    }
                }
            },
            'social_logs': {
                'type': 'directory',
                'content': {
                    'emails.log': {
                        'type': 'file',
                        'content': """
From: jsmith@corp.com
To: hr@corp.com
Subject: Vacation Request

Hi HR,

I'd like to request vacation from Aug 1st to Aug 14th. My temporary password for the shared drive is 'SummerFun2025'.

Thanks,
John Smith

From: it_support@corp.com
To: jsmith@corp.com
Subject: Password Reset

Dear John,

Your password has been reset. Your new temporary password is 'SecurePass!'. Please change it immediately.

Regards,
IT Support
""",
                        'permissions': 'r--',
                        'corrupted': False
                    },
                    'chat_history.log': {
                        'type': 'file',
                        'content': """
[10:05 AM] Alice: Hey Bob, did you set up the new server?
[10:06 AM] Bob: Yeah, almost done. Just need to configure the firewall. Default admin pass is 'network_admin'.
[10:07 AM] Alice: Cool, thanks! Don't forget to change it later.
[10:08 AM] Bob: Will do. Also, remind me to update the 'project_phoenix' docs.
""",
                        'permissions': 'r--',
                        'corrupted': False
                    },
                    'admin_notes.log': {
                        'type': 'file',
                        'content': """
- Meeting with CEO on 2025-07-20. Discussed 'Project Chimera' security.
- Temporary access for contractor 'GuestUser' - password 'ContractorAccess'. Expires 2025-07-30.
- Reminder: Update all systems to latest patch by end of month. Critical vulnerability in 'LegacyApp' (CVE-2024-1234).
""",
                        'permissions': 'r--',
                        'corrupted': False
                    }
                }
            }
        }
        return fs

    def set_current_fs(self, new_fs):
        self.current_fs = new_fs

    def _get_node(self, path_parts):
        current_node = self.current_fs
        for part in path_parts:
            if part not in current_node:
                return None
            node_info = current_node[part]
            if node_info.get('type') == 'file':
                current_node = node_info
            else:
                current_node = node_info['content']
        return current_node

    def get_node_info(self, path_parts):
        if not path_parts: # If path_parts is empty, it means we are looking for the root
            return self.current_fs, None # Return the root node and no parent
            
        current_node = self.current_fs
        node_info = None
        parent_node = None
        for i, part in enumerate(path_parts):
            if part not in current_node:
                return None, None # Node not found
            
            parent_node = current_node
            node_info = current_node[part]
            
            if i < len(path_parts) - 1: # Not the target node yet, so must be a directory
                if node_info.get('type') == 'file':
                    return None, None # Cannot traverse into a file
                current_node = node_info['content'] # Move into the directory content
        
        return node_info, parent_node # Return the actual node info and its parent

    def list_directory(self, path_parts):
        node_info, _ = self.get_node_info(path_parts)
        if node_info is None:
            return "Error: Directory not found."
        if node_info.get('type') == 'file':
            return "Error: Not a directory."
        if node_info.get('is_protected') and not node_info.get('unlocked', False):
            return "Error: Access denied. This directory is password protected."

        contents = []
        # If node_info has a 'content' key, it's a nested directory structure
        # Otherwise, node_info itself is the directory content (e.g., for the root)
        items_to_list = node_info.get('content', node_info)

        for name, info in items_to_list.items():
            # Check if 'info' is a dictionary and has a 'type' key
            item_type = "DIR" if isinstance(info, dict) and info.get('type') == 'directory' else "FILE"
            contents.append(f"{item_type}: {name}")
        return "\n".join(contents)

    def change_permissions(self, path_parts, new_permissions):
        node_info, _ = self.get_node_info(path_parts)
        if node_info is None:
            return "Error: File or directory not found."
        if node_info.get('type') == 'directory':
            return "Error: Cannot change permissions of a directory."
        
        # Basic validation for permissions string (e.g., 'rwx', 'r--')
        if not all(c in 'rwx-' for c in new_permissions) or len(new_permissions) != 3:
            return "Error: Invalid permission format. Use r, w, x, or - (e.g., rwx, r--)."

        node_info['permissions'] = new_permissions
        return f"Permissions for {path_parts[-1]} changed to {new_permissions}."

    def check_permission(self, path_parts, permission_type):
        node_info, _ = self.get_node_info(path_parts)
        if node_info is None:
            return False
        
        permissions = node_info.get('permissions', 'rwx') # Default to rwx if not specified
        
        if permission_type == 'read':
            return permissions[0] == 'r'
        elif permission_type == 'write':
            return permissions[1] == 'w'
        elif permission_type == 'execute':
            return permissions[2] == 'x'
        return False

    def get_file_content(self, path_parts, password=None):
        node_info, parent_node = self.get_node_info(path_parts)
        if node_info is None:
            return "Error: File not found."
        if node_info.get('type') == 'directory':
            return "Error: Cannot 'cat' a directory."

        if node_info.get('is_honeypot'):
            self.ids.increment_anomaly_score(50, "Interaction with honeypot file")
            return "Access Denied: This file appears to be a trap. Anomaly detected!"
        
        if node_info.get('is_protected'):
            if password is None:
                return "Error: This file is password protected. Use 'cat <file> <password>'."
            if password == node_info.get('password'):
                # Mark the file as unlocked in the actual file system
                if parent_node and path_parts[-1] in parent_node:
                    parent_node[path_parts[-1]]['unlocked'] = True
                return node_info['content']
            else:
                return "Error: Incorrect password."
        
        if node_info.get('corrupted'):
            return "Error: File is corrupted. Use a repair utility to fix it."

        return node_info['content']

    def create_file(self, path_parts, content, permissions):
        parent_path_parts = path_parts[:-1]
        file_name = path_parts[-1]
        parent_node_info, _ = self.get_node_info(parent_path_parts)

        if parent_node_info is None or parent_node_info.get('type') == 'file':
            return "Error: Parent directory not found or is a file."

        if file_name in parent_node_info['content']:
            return "Error: File with that name already exists."

        parent_node_info['content'][file_name] = {
            'type': 'file',
            'content': content,
            'permissions': permissions,
            'corrupted': False
        }
        return f"File '{file_name}' created successfully."

    def delete_file(self, path_parts):
        parent_path_parts = path_parts[:-1]
        file_name = path_parts[-1]
        parent_node_info, _ = self.get_node_info(parent_path_parts)

        if parent_node_info is None or parent_node_info.get('type') == 'file':
            return "Error: Parent directory not found or is a file."

        if file_name not in parent_node_info['content']:
            return "Error: File not found."

        del parent_node_info['content'][file_name]
        return f"File '{file_name}' deleted successfully."

    def move_file(self, source_path_parts, destination_path_parts):
        source_node_info, source_parent_node = self.get_node_info(source_path_parts)
        if source_node_info is None:
            return "Error: Source file or directory not found."
        
        # Check if destination is a directory
        destination_node_info, _ = self.get_node_info(destination_path_parts)
        if destination_node_info and destination_node_info.get('type') == 'file':
            return "Error: Cannot move to an existing file."

        # Remove from source
        source_name = source_path_parts[-1]
        del source_parent_node['content'][source_name]

        # Add to destination
        if destination_node_info and destination_node_info.get('type') == 'directory':
            destination_node_info['content'][source_name] = source_node_info
            return f"Moved {source_name} to /{'/'.join(destination_path_parts)}."
        else:
            # Rename or move to new location
            new_parent_path_parts = destination_path_parts[:-1]
            new_name = destination_path_parts[-1]
            new_parent_node_info, _ = self.get_node_info(new_parent_path_parts)
            if new_parent_node_info and new_parent_node_info.get('type') == 'directory':
                new_parent_node_info['content'][new_name] = source_node_info
                return f"Moved {source_name} to /{'/'.join(destination_path_parts)}."
            else:
                return "Error: Destination directory not found."