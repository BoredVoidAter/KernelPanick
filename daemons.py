import random
import time

class Daemon:
    def __init__(self, name, interval, action_func):
        self.name = name
        self.interval = interval # in seconds
        self.action_func = action_func
        self.last_run_time = time.time()

    def run_if_due(self, filesystem, game_state):
        if time.time() - self.last_run_time >= self.interval:
            print(f"[DAEMON] {self.name} is running...")
            self.action_func(filesystem, game_state)
            self.last_run_time = time.time()

class DaemonManager:
    def __init__(self, filesystem, game_state):
        self.filesystem = filesystem
        self.game_state = game_state
        self.daemons = self._initialize_daemons()

    def _initialize_daemons(self):
        daemons = [
            Daemon(
                name="LogRotator",
                interval=30, # Every 30 seconds
                action_func=self._log_rotator_action
            ),
            Daemon(
                name="TempFileCleanup",
                interval=45, # Every 45 seconds
                action_func=self._temp_file_cleanup_action
            ),
            Daemon(
                name="SecurityScan",
                interval=60, # Every 60 seconds
                action_func=self._security_scan_action
            )
        ]
        return daemons

    def run_daemons(self):
        for daemon in self.daemons:
            daemon.run_if_due(self.filesystem, self.game_state)

    def _log_rotator_action(self, filesystem, game_state):
        # Simulate log rotation: append a new entry to a log file
        log_path = ['log', 'system_events.log']
        node_info, parent_node = filesystem.get_node_info(log_path)
        if node_info and node_info.get('type') == 'file':
            new_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Daemon: LogRotator added new entry.\n"
            node_info['content'] += new_entry
            print("[DAEMON] LogRotator: Appended new entry to system_events.log")
        else:
            print("[DAEMON] LogRotator: system_events.log not found.")

    def _temp_file_cleanup_action(self, filesystem, game_state):
        # Simulate temp file cleanup: remove a random temp file if it exists
        tmp_path = ['tmp']
        node_info, _ = filesystem.get_node_info(tmp_path)
        if node_info and node_info.get('type') == 'directory':
            temp_files = [name for name, info in node_info['content'].items() if info.get('type') == 'file']
            if temp_files:
                file_to_delete = random.choice(temp_files)
                filesystem.delete_file(tmp_path + [file_to_delete])
                print(f"[DAEMON] TempFileCleanup: Deleted {file_to_delete} from /tmp/")
            else:
                print("[DAEMON] TempFileCleanup: No temp files to clean.")
        else:
            print("[DAEMON] TempFileCleanup: /tmp/ directory not found.")

    def _security_scan_action(self, filesystem, game_state):
        # Simulate a security scan: potentially increase anomaly score or add a new log entry
        print("[DAEMON] SecurityScan: Performing system scan...")
        # Example: If anomaly score is high, trigger a defensive action (to be implemented later)
        if hasattr(game_state, 'anomaly_score') and game_state.anomaly_score > 50:
            print("[DAEMON] SecurityScan: High anomaly detected! Initiating defensive measures.")
            # Further actions like locking out player, deleting files, etc.
        else:
            log_path = ['log', 'security.log']
            node_info, parent_node = filesystem.get_node_info(log_path)
            if node_info and node_info.get('type') == 'file':
                new_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Daemon: SecurityScan completed. No anomalies detected.\n"
                node_info['content'] += new_entry
                print("[DAEMON] SecurityScan: Logged scan completion.")
            else:
                print("[DAEMON] SecurityScan: security.log not found. Creating it.")
                filesystem.create_file(log_path, f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Daemon: SecurityScan initialized.\n", 'r--')
