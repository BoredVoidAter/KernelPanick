

import random
import time

class SensorSimulation:
    def __init__(self):
        self.microphone_data = [
            "User says: 'My password is password123'",
            "User says: 'The Wi-Fi is guest_network_2025'",
            "User says: 'Remember to check the backdoor in the system'",
            "User hums a tune.",
            "Sound of a dog barking.",
            "User talks on the phone about their day."
        ]
        self.camera_data = [
            "Motion detected in the living room.",
            "User enters the room and sits down.",
            "User leaves the device unattended.",
            "A cat walks across the camera's view.",
            "The room is empty.",
            "User is typing on a keyboard."
        ]

    def generate_microphone_log(self):
        return random.choice(self.microphone_data)

    def generate_camera_log(self):
        return random.choice(self.camera_data)

    def generate_sensor_logs(self, num_logs=1):
        logs = []
        for _ in range(num_logs):
            log_type = random.choice(["microphone", "camera"])
            if log_type == "microphone":
                logs.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] MICROPHONE: {self.generate_microphone_log()}")
            else:
                logs.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] CAMERA: {self.generate_camera_log()}")
        return "\n".join(logs)

if __name__ == "__main__":
    sensor_sim = SensorSimulation()
    print("Generating 3 sensor logs:")
    print(sensor_sim.generate_sensor_logs(3))

