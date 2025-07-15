class FileSystem:
    def __init__(self, initial_fs_data=None):
        self.current_fs = self._build_file_system() # This will be the current active file system

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
        for name, info in node_info['content'].items():
            item_type = "DIR" if info.get('type') == 'directory' else "FILE"
            contents.append(f"{item_type}: {name}")
        return "\n".join(contents)

    def get_file_content(self, path_parts, password=None):
        node_info, parent_node = self.get_node_info(path_parts)
        if node_info is None:
            return "Error: File not found."
        if node_info.get('type') == 'directory':
            return "Error: Cannot 'cat' a directory."
        
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
        
        return node_info['content']