
import random

class ActuatorControl:
    def __init__(self):
        self.devices = {
            "toaster": {
                "actions": [
                    "burn toast",
                    "pop toast",
                    "turn off"
                ],
                "status": "idle"
            },
            "thermostat": {
                "actions": [
                    "set temperature to 20C",
                    "set temperature to 30C",
                    "turn off heating",
                    "turn on AC"
                ],
                "status": "22C"
            },
            "smart_speaker": {
                "actions": [
                    "play loud music",
                    "play white noise",
                    "announce a message"
                ],
                "status": "off"
            }
        }

    def get_available_devices(self):
        return list(self.devices.keys())

    def perform_action(self, device, action):
        if device not in self.devices:
            return f"Error: Device '{device}' not found."
        if action not in self.devices[device]["actions"]:
            return f"Error: Action '{action}' not supported for '{device}'."

        # Simulate the action and its effect
        if device == "toaster":
            if action == "burn toast":
                self.devices[device]["status"] = "burning"
                return "The toaster is now burning toast. Smoke alarm might go off soon."
            elif action == "pop toast":
                self.devices[device]["status"] = "idle"
                return "Toast popped. User might check the toaster."
            elif action == "turn off":
                self.devices[device]["status"] = "off"
                return "Toaster turned off."
        elif device == "thermostat":
            self.devices[device]["status"] = action.replace("set temperature to ", "")
            return f"Thermostat set to {self.devices[device]["status"]}. User might notice the temperature change."
        elif device == "smart_speaker":
            if action == "play loud music":
                self.devices[device]["status"] = "playing loud music"
                return "Loud music is now playing from the smart speaker. User will definitely react."
            elif action == "play white noise":
                self.devices[device]["status"] = "playing white noise"
                return "White noise is playing. User might find it soothing or annoying."
            elif action == "announce a message":
                message = random.choice([
                    "Intruder alert!",
                    "Your device is compromised.",
                    "Hello, human."
                ])
                self.devices[device]["status"] = f"announcing: {message}"
                return f"Smart speaker announced: '{message}'. User will be confused."
        return f"Action '{action}' performed on '{device}'."

if __name__ == "__main__":
    actuator_ctrl = ActuatorControl()
    print("Available devices:", actuator_ctrl.get_available_devices())
    print(actuator_ctrl.perform_action("toaster", "burn toast"))
    print(actuator_ctrl.perform_action("thermostat", "set temperature to 30C"))
    print(actuator_ctrl.perform_action("smart_speaker", "play loud music"))
