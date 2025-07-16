class HardwareInterface:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type
        self.status = {"power": "off"}

    def toggle_led(self, led_id, state):
        print(f"Device {self.device_id}: Toggling LED {led_id} to {state}")
        # Simulate LED state change
        self.status[f"led_{led_id}"] = state
        return True

    def read_sensor(self, sensor_id):
        print(f"Device {self.device_id}: Reading sensor {sensor_id}")
        # Simulate sensor reading (e.g., temperature)
        if sensor_id == "temperature":
            return {"value": 25.5, "unit": "celsius"} # Example reading
        return None

    def activate_motor(self, motor_id, duration):
        print(f"Device {self.device_id}: Activating motor {motor_id} for {duration} seconds")
        # Simulate motor activation
        return True

    def get_status(self):
        return self.status

# Example hardware devices
HARDWARE_DEVICES = {
    "toaster_hwi": HardwareInterface("toaster_01", "toaster"),
    "fridge_hwi": HardwareInterface("fridge_01", "fridge"),
}

def get_hardware_interface(device_id):
    return HARDWARE_DEVICES.get(device_id)
