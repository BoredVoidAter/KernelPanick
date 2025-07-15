
class Encryption:
    def __init__(self, algorithm, key):
        self.algorithm = algorithm
        self.key = key

    def encrypt(self, data):
        # Placeholder for actual encryption logic
        return f"ENCRYPTED_{self.algorithm}_{self.key}_{data}"

    def decrypt(self, encrypted_data):
        # Placeholder for actual decryption logic
        parts = encrypted_data.split('_')
        if len(parts) == 4 and parts[0] == "ENCRYPTED" and parts[1] == self.algorithm and parts[2] == self.key:
            return parts[3]
        return None # Decryption failed

class CryptographyManager:
    def __init__(self):
        self.encryption_utilities = {
            "AES": Encryption("AES", "default_aes_key"),
            "RSA": Encryption("RSA", "default_rsa_key"),
        }
        self.found_keys = {}

    def add_utility(self, algorithm, key):
        self.encryption_utilities[algorithm] = Encryption(algorithm, key)

    def add_key(self, algorithm, key):
        self.found_keys[algorithm] = key

    def decrypt_file(self, file_content, algorithm, key=None):
        if algorithm not in self.encryption_utilities:
            return None, "Unknown encryption algorithm."

        if key is None:
            key = self.found_keys.get(algorithm)
            if key is None:
                return None, f"No key found for {algorithm} algorithm."

        utility = self.encryption_utilities[algorithm]
        # Temporarily set the utility's key to the provided key for decryption
        original_key = utility.key
        utility.key = key
        decrypted_data = utility.decrypt(file_content)
        utility.key = original_key # Restore original key

        if decrypted_data:
            return decrypted_data, "Decryption successful."
        else:
            return None, "Decryption failed. Incorrect key or algorithm."

