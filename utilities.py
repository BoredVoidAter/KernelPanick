
class RepairUtilities:
    def __init__(self, filesystem):
        self.filesystem = filesystem

    def reverse_text_repair(self, file_path_parts):
        node_info, _ = self.filesystem.get_node_info(file_path_parts)
        if node_info is None or node_info.get('type') == 'directory':
            return "Error: File not found."

        if not node_info.get('corrupted'):
            return "File is not corrupted."

        original_content = node_info['content']
        repaired_content = original_content[::-1] # Reverse the string

        node_info['content'] = repaired_content
        node_info['corrupted'] = False
        return f"File '{file_path_parts[-1]}' repaired (reversed text)."

    def simple_cipher_repair(self, file_path_parts, shift=1):
        node_info, _ = self.filesystem.get_node_info(file_path_parts)
        if node_info is None or node_info.get('type') == 'directory':
            return "Error: File not found."

        if not node_info.get('corrupted'):
            return "File is not corrupted."

        original_content = node_info['content']
        repaired_content = ""
        for char in original_content:
            if 'a' <= char <= 'z':
                repaired_content += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                repaired_content += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                repaired_content += char

        node_info['content'] = repaired_content
        node_info['corrupted'] = False
        return f"File '{file_path_parts[-1]}' repaired (simple cipher, shift {shift})."
