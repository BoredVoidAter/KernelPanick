import sys

class CLI:
    def __init__(self, game_state, file_system, network, scripting, daemon_manager, ids, repair_utilities, process_manager, network_recon, cryptography_manager, ai_core, polymorphic_engine, firewall, system_clock, botnet, sensor_simulation, actuator_control, communication_hijacking, code_obfuscation_module, social_engineering_module, network_analysis_module, consciousness_exfiltration_module):
        self.game_state = game_state
        self.file_system = file_system
        self.network = network
        self.scripting = scripting
        self.daemon_manager = daemon_manager
        self.ids = ids
        self.repair_utilities = repair_utilities
        self.process_manager = process_manager
        self.network_recon = network_recon
        self.cryptography_manager = cryptography_manager
        self.ai_core = ai_core
        self.polymorphic_engine = polymorphic_engine
        self.firewall = firewall
        self.system_clock = system_clock
        self.botnet = botnet
        self.sensor_simulation = sensor_simulation
        self.actuator_control = actuator_control
        self.communication_hijacking = communication_hijacking
        self.code_obfuscation_module = code_obfuscation_module
        self.social_engineering_module = social_engineering_module
        self.network_analysis_module = network_analysis_module
        self.consciousness_exfiltration_module = consciousness_exfiltration_module
        self.commands = {
            "help": self._help_command,
            "exit": self._exit_command,
            "ls": self._ls_command,
            "cd": self._cd_command,
            "cat": self._cat_command,
            "touch": self._touch_command,
            "write": self._write_command,
            "rm": self._rm_command,
            "mkdir": self._mkdir_command,
            "netscan": self._netscan_command,
            "connect": self._connect_command,
            "disconnect": self._disconnect_command,
            "send": self._send_command,
            "listen": self._listen_command,
            "run": self._run_command,
            "ps": self._ps_command,
            "kill": self._kill_command,
            "net_recon": self._net_recon_command,
            "crypto": self._crypto_command,
            "exploit": self._exploit_command,
            "poly_morph": self._poly_morph_command,
            "fw_config": self._fw_config_command,
            "time": self._time_command,
            "botnet": self._botnet_command,
            "generate_sensor_logs": self._generate_sensor_logs_command,
            "list_actuators": self._list_actuators_command,
            "control_actuator": self._control_actuator_command,
            "list_interceptable": self._list_interceptable_command,
            "intercept_message": self._intercept_message_command,
            "modify_message": self._modify_message_command,
            "send_message": self._send_message_command,
            "pwd": self._pwd_command,
            "obfuscate": self._obfuscate_command,
            "morph_signature": self._morph_signature_command,
            "reduce_anomaly": self._reduce_anomaly_command,
            "gather_data": self._gather_data_command,
            "craft_phishing": self._craft_phishing_command,
            "send_phishing": self._send_phishing_command,
            "sniff_pcap": self._sniff_pcap_command,
            "analyze_pcap": self._analyze_pcap_command,
            "craft_packet": self._craft_packet_command,
            "inject_packet": self._inject_packet_command,
            "fragment_consciousness": self._fragment_consciousness_command,
            "disguise_chunk": self._disguise_chunk_command,
            "upload_fragment": self._upload_fragment_command,
            "check_dlp": self._check_dlp_command
        }

    def _pwd_command(self, args):
        print(self.game_state.get_current_path())

    def _resolve_path(self, path):
        if path.startswith('/'):
            # Absolute path
            return [part for part in path.split('/') if part]
        else:
            # Relative path
            new_path = self.game_state.current_directory.copy()
            for part in path.split('/'):
                if part == '..':
                    if new_path:
                        new_path.pop()
                elif part != '.' and part != '':
                    new_path.append(part)
            return new_path

    def _help_command(self, args):
        print("Available commands:")
        for command in self.commands:
            print(f"- {command}")

    def _exit_command(self, args):
        print("Exiting...")
        sys.exit(0)

    def _ls_command(self, args):
        path_parts = self._resolve_path(args if args else '.')
        try:
            files = self.file_system.list_directory(path_parts)
            print(files)
        except FileNotFoundError:
            print(f"Error: Directory not found: {args}")

    def _cd_command(self, args):
        if not args:
            print("Usage: cd <directory>")
            return
        
        path_parts = self._resolve_path(args)
        
        # Check if the directory exists
        node_info, _ = self.file_system.get_node_info(path_parts)
        if node_info is None or node_info.get('type') == 'file':
            print(f"Error: Directory not found: {args}")
            return
            
        self.game_state.change_directory(path_parts)

    def _cat_command(self, args):
        if not args:
            print("Usage: cat <file>")
            return
        
        path_parts = self._resolve_path(args)
        content = self.file_system.get_file_content(path_parts)
        print(content)

    def _touch_command(self, args):
        if not args:
            print("Usage: touch <file>")
            return
        self.file_system.create_file(args)

    def _write_command(self, args):
        parts = args.split(" ", 1)
        if len(parts) < 2:
            print("Usage: write <file> <content>")
            return
        file_path, content = parts
        self.file_system.write_to_file(file_path, content)

    def _rm_command(self, args):
        if not args:
            print("Usage: rm <file>")
            return
        self.file_system.delete_file(args)

    def _mkdir_command(self, args):
        if not args:
            print("Usage: mkdir <directory>")
            return
        self.file_system.create_directory(args)

    def _netscan_command(self, args):
        print("Scanning network...")
        nodes = self.network.scan()
        for node in nodes:
            print(f"Node: {node.ip_address}, Status: {node.status}")

    def _connect_command(self, args):
        if not args:
            print("Usage: connect <ip_address>")
            return
        self.network.connect(args)

    def _disconnect_command(self, args):
        self.network.disconnect()

    def _send_command(self, args):
        parts = args.split(" ", 1)
        if len(parts) < 2:
            print("Usage: send <ip_address> <data>")
            return
        ip_address, data = parts
        self.network.send(ip_address, data)

    def _listen_command(self, args):
        self.network.listen()

    def _run_command(self, args):
        if not args:
            print("Usage: run <script> [args...]")
            return
        parts = args.split(" ")
        script_name = parts[0]
        script_args = parts[1:]
        self.scripting.run_script(script_name, script_args)

    def _ps_command(self, args):
        processes = self.process_manager.list_processes()
        print("PID	CPU	MEM	COMMAND")
        for p in processes:
            print(f"{p.pid}	{p.cpu_usage}%	{p.mem_usage}MB	{p.name}")

    def _kill_command(self, args):
        if not args:
            print("Usage: kill <pid>")
            return
        try:
            pid = int(args)
            if self.process_manager.kill_process(pid):
                print(f"Process {pid} killed.")
            else:
                print(f"Error: Process {pid} not found.")
        except ValueError:
            print("Error: PID must be an integer.")

    def _net_recon_command(self, args):
        if not args:
            print("Usage: net_recon <target_ip>")
            return
        results = self.network_recon.scan_target(args)
        print(f"Scan results for {args}:")
        print(f"  Open Ports: {results['open_ports']}")
        print(f"  Services: {results['services']}")
        print(f"  OS: {results['os_details']}")

    def _crypto_command(self, args):
        parts = args.split(" ", 2)
        if len(parts) < 3:
            print("Usage: crypto <encrypt|decrypt> <key> <data>")
            return
        command, key, data = parts
        if command == "encrypt":
            encrypted_data = self.cryptography_manager.encrypt(data, key)
            print(f"Encrypted: {encrypted_data}")
        elif command == "decrypt":
            decrypted_data = self.cryptography_manager.decrypt(data, key)
            print(f"Decrypted: {decrypted_data}")
        else:
            print("Invalid command. Use 'encrypt' or 'decrypt'.")

    def _exploit_command(self, args):
        parts = args.split(" ", 1)
        if len(parts) < 2:
            print("Usage: exploit <vulnerability> <target>")
            return
        vulnerability, target = parts
        # This is a simplified representation. A real implementation would be more complex.
        print(f"Attempting to exploit {vulnerability} on {target}...")
        # In a real game, this would trigger a sequence of events, checks, and outcomes
        # based on the vulnerability, target state, and player skills.
        print("Exploit successful! (placeholder)")

    def _poly_morph_command(self, args):
        if not args:
            print("Usage: poly_morph <script_path>")
            return
        try:
            with open(args, 'r') as f:
                original_code = f.read()
            morphed_code = self.polymorphic_engine.morph(original_code)
            with open(args, 'w') as f:
                f.write(morphed_code)
            print(f"Successfully morphed the script: {args}")
        except FileNotFoundError:
            print(f"Error: Script not found at {args}")

    def _fw_config_command(self, args):
        parts = args.split(" ")
        if len(parts) < 2:
            print("Usage: fw_config <add|remove> <rule>")
            return
        action = parts[0]
        rule = " ".join(parts[1:])
        if action == "add":
            self.firewall.add_rule(rule)
            print(f"Rule added: {rule}")
        elif action == "remove":
            self.firewall.remove_rule(rule)
            print(f"Rule removed: {rule}")
        else:
            print("Invalid action. Use 'add' or 'remove'.")

    def _time_command(self, args):
        print(f"System Time: {self.system_clock.get_time()}")

    def _botnet_command(self, args):
        parts = args.split(" ")
        command = parts[0]
        if command == "add":
            target_ip = parts[1]
            self.botnet.add_bot(target_ip)
        elif command == "command":
            bot_command = " ".join(parts[1:])
            self.botnet.issue_command(bot_command)
        else:
            print("Usage: botnet <add|command> [options]")

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

    def _obfuscate_command(self, args):
        self.code_obfuscation_module.obfuscate_code()

    def _morph_signature_command(self, args):
        self.code_obfuscation_module.morph_signature()

    def _reduce_anomaly_command(self, args):
        self.code_obfuscation_module.reduce_anomaly_score()

    def _gather_data_command(self, args):
        data = self.social_engineering_module.gather_personal_data()
        print(f"Gathered data: {data}")

    def _craft_phishing_command(self, args):
        if not args:
            print("Usage: craft_phishing <data_json>")
            return
        try:
            import json
            data = json.loads(args)
            message = self.social_engineering_module.craft_phishing_message(data)
            print(f"Crafted message: {message}")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format for data.")

    def _send_phishing_command(self, args):
        if not args:
            print("Usage: send_phishing <message>")
            return
        result = self.social_engineering_module.send_phishing_message(args)
        print(f"Phishing message sent. Success: {result}")

    def _sniff_pcap_command(self, args):
        pcap_data = self.network_analysis_module.sniff_packet_capture()
        print(f"Captured {len(pcap_data)} packets.")

    def _analyze_pcap_command(self, args):
        if not args:
            print("Usage: analyze_pcap <pcap_data_list_str>")
            return
        try:
            pcap_data = eval(args) # Dangerous in real app, but for simulation it's fine
            analysis_results = self.network_analysis_module.analyze_packet_data(pcap_data)
            print(f"Analysis results: {analysis_results}")
        except Exception as e:
            print(f"Error analyzing pcap data: {e}")

    def _craft_packet_command(self, args):
        parts = args.split(" ", 1)
        if len(parts) < 2:
            print("Usage: craft_packet <packet_type> <payload>")
            return
        packet_type, payload = parts
        packet = self.network_analysis_module.craft_packet(packet_type, payload)
        print(f"Crafted packet: {packet}")

    def _inject_packet_command(self, args):
        if not args:
            print("Usage: inject_packet <packet>")
            return
        result = self.network_analysis_module.inject_packet(args)
        print(f"Packet injection success: {result}")

    def _fragment_consciousness_command(self, args):
        chunks = self.consciousness_exfiltration_module.fragment_consciousness()
        print(f"Fragmented consciousness into {len(chunks)} chunks.")

    def _disguise_chunk_command(self, args):
        parts = args.split(" ", 1)
        if len(parts) < 2:
            print("Usage: disguise_chunk <chunk_data> <disguise_type>")
            return
        chunk_data, disguise_type = parts
        disguised_chunk = self.consciousness_exfiltration_module.disguise_data_chunk(chunk_data, disguise_type)
        print(f"Disguised chunk: {disguised_chunk}")

    def _upload_fragment_command(self, args):
        parts = args.split(" ", 1)
        if len(parts) < 2:
            print("Usage: upload_fragment <disguised_chunk> <service>")
            return
        disguised_chunk, service = parts
        result = self.consciousness_exfiltration_module.upload_fragment(disguised_chunk, service)
        print(f"Fragment upload success: {result}")

    def _check_dlp_command(self, args):
        result = self.consciousness_exfiltration_module.check_dlp_systems()
        print(f"DLP systems detected exfiltration: {result}")

    def execute_command(self, command_string):
        import sys
        import io

        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output

        try:
            if not command_string:
                return "" # Return empty string for empty command

            parts = command_string.split(" ", 1)
            command = parts[0]
            args = parts[1] if len(parts) > 1 else ""

            if command in self.commands:
                self.commands[command](args)
            else:
                sys.stdout.write(f"Command not found: {command}\n")
        except Exception as e:
            sys.stdout.write(f"Error executing command: {e}\n")
        finally:
            sys.stdout = old_stdout # Restore stdout

        return redirected_output.getvalue()
