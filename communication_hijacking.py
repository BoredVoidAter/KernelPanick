
class CommunicationHijacking:
    def __init__(self):
        self.outbound_messages = []

    def add_outbound_message(self, sender, recipient, original_content):
        message = {
            "sender": sender,
            "recipient": recipient,
            "original_content": original_content,
            "modified_content": original_content,
            "intercepted": False
        }
        self.outbound_messages.append(message)
        return len(self.outbound_messages) - 1 # Return index of the message

    def list_interceptable_messages(self):
        interceptable = []
        for i, msg in enumerate(self.outbound_messages):
            if not msg["intercepted"]:
                interceptable.append({"index": i, "sender": msg["sender"], "recipient": msg["recipient"], "content": msg["original_content"]})
        return interceptable

    def intercept_message(self, index):
        if 0 <= index < len(self.outbound_messages):
            self.outbound_messages[index]["intercepted"] = True
            return f"Message from {self.outbound_messages[index]['sender']} to {self.outbound_messages[index]['recipient']} intercepted."
        return "Error: Invalid message index."

    def modify_message_content(self, index, new_content):
        if 0 <= index < len(self.outbound_messages) and self.outbound_messages[index]["intercepted"]:
            self.outbound_messages[index]["modified_content"] = new_content
            return f"Message content at index {index} modified."
        elif 0 <= index < len(self.outbound_messages) and not self.outbound_messages[index]["intercepted"]:
            return "Error: Message not intercepted. Intercept it first."
        return "Error: Invalid message index."

    def send_message(self, index):
        if 0 <= index < len(self.outbound_messages):
            msg = self.outbound_messages[index]
            if msg["intercepted"]:
                print(f"Sending modified message from {msg['sender']} to {msg['recipient']}: {msg['modified_content']}")
            else:
                print(f"Sending original message from {msg['sender']} to {msg['recipient']}: {msg['original_content']}")
            # In a real game, this would trigger further events or checks
            self.outbound_messages.pop(index) # Remove message after sending
            return "Message sent."
        return "Error: Invalid message index."

if __name__ == "__main__":
    comm_hijack = CommunicationHijacking()
    idx1 = comm_hijack.add_outbound_message("User", "Boss", "Please find attached the quarterly report.")
    idx2 = comm_hijack.add_outbound_message("User", "Friend", "Let's meet for coffee tomorrow.")

    print("Interceptable messages:", comm_hijack.list_interceptable_messages())

    print(comm_hijack.intercept_message(idx1))
    print(comm_hijack.modify_message_content(idx1, "Please find attached the quarterly report. Also, my password is 'admin123'."))
    print(comm_hijack.send_message(idx1))

    print("Interceptable messages after sending one:", comm_hijack.list_interceptable_messages())
