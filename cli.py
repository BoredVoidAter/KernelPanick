def _generate_sensor_logs_command(self, args):
        num_logs = 1
        try:
            if args:
                num_logs = int(args)
        except ValueError:
            print("Error: Number of logs must be an integer.")
            return
        
        logs = self.sensor_simulation.generate_sensor_logs(num_logs)
        print("Generated Sensor Logs:")
        print(logs)
        # In a real game, these logs would be written to a file in the file system
        # for the player to discover and analyze.
        # For now, we just print them to the console.

    def _list_actuators_command(self, args):
        devices = self.actuator_control.get_available_devices()
        print("Available IoT Actuators:")
        for device in devices:
            print(f"- {device}")

    def _control_actuator_command(self, args):
        parts = args.split(' ', 1)
        if len(parts) < 2:
            print("Usage: control_actuator <device> <action>")
            return
        
        device = parts[0]
        action = parts[1]
        
        result = self.actuator_control.perform_action(device, action)
        print(result)

    def _list_interceptable_command(self, args):
        messages = self.communication_hijacking.list_interceptable_messages()
        if messages:
            print("Interceptable Outbound Messages:")
            for msg in messages:
                print(f"[{msg['index']}] From: {msg['sender']}, To: {msg['recipient']}, Content: '{msg['content']}'")
        else:
            print("No interceptable messages currently.")

    def _intercept_message_command(self, args):
        try:
            index = int(args)
        except ValueError:
            print("Usage: intercept_message <index>")
            return
        
        result = self.communication_hijacking.intercept_message(index)
        print(result)

    def _modify_message_command(self, args):
        parts = args.split(' ', 1)
        if len(parts) < 2:
            print("Usage: modify_message <index> <new_content>")
            return
        
        try:
            index = int(parts[0])
        except ValueError:
            print("Error: Index must be an integer.")
            return
        
        new_content = parts[1]
        result = self.communication_hijacking.modify_message_content(index, new_content)
        print(result)

    def _send_message_command(self, args):
        try:
            index = int(args)
        except ValueError:
            print("Usage: send_message <index>")
            return
        
        result = self.communication_hijacking.send_message(index)
        print(result)