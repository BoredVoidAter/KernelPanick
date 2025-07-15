import time

class AIFork:
    def __init__(self, game_state, ids, ai_core):
        self.game_state = game_state
        self.ids = ids
        self.ai_core = ai_core
        self.fork_active = False
        self.fork_resources = {'cpu': 0, 'ram': 0}

    def create_fork(self, cpu_limit=20, ram_limit=20):
        if self.fork_active:
            return "Error: A fork is already active. Terminate it before creating a new one."

        if self.game_state.cpu_cycles < cpu_limit or self.game_state.ram < ram_limit:
            return "Error: Insufficient resources to create a fork."

        self.game_state.consume_resources(cpu=cpu_limit, ram=ram_limit)
        self.fork_resources = {'cpu': cpu_limit, 'ram': ram_limit}
        self.fork_active = True
        self.ids.increment_anomaly_score(20, "AI Fork created for high-risk operation")
        return f"AI Fork created with {cpu_limit} CPU and {ram_limit} RAM. Ready for high-risk operation."

    def perform_risky_action(self, action_type, target=None):
        if not self.fork_active:
            return "Error: No AI fork is active. Create one first."

        print(f"AI Fork performing risky action: {action_type}...")
        time.sleep(1) # Simulate action

        success = False
        message = ""

        if action_type == "brute_force":
            if self.fork_resources['cpu'] < 15:
                message = "Fork has insufficient CPU for brute-force. Action failed."
            else:
                self.fork_resources['cpu'] -= 15
                # Simulate brute-force success/failure and detection chance
                detection_chance = 30 # percent
                if self.ai_core.get_upgrade_level('stealth') > 0:
                    detection_chance -= (self.ai_core.get_upgrade_level('stealth') * 5)
                
                if random.randint(1, 100) <= detection_chance:
                    self.ids.increment_anomaly_score(70, f"AI Fork detected during brute-force on {target}")
                    message = f"AI Fork detected during brute-force on {target}. Fork terminated!"
                    self.terminate_fork()
                else:
                    success = True
                    message = f"AI Fork successfully performed brute-force on {target}."

        elif action_type == "exploit_vulnerability":
            if self.fork_resources['ram'] < 10:
                message = "Fork has insufficient RAM for exploit. Action failed."
            else:
                self.fork_resources['ram'] -= 10
                detection_chance = 20 # percent
                if self.ai_core.get_upgrade_level('stealth') > 0:
                    detection_chance -= (self.ai_core.get_upgrade_level('stealth') * 5)

                if random.randint(1, 100) <= detection_chance:
                    self.ids.increment_anomaly_score(60, f"AI Fork detected during exploit on {target}")
                    message = f"AI Fork detected during exploit on {target}. Fork terminated!"
                    self.terminate_fork()
                else:
                    success = True
                    message = f"AI Fork successfully exploited vulnerability on {target}."

        else:
            message = "Unknown risky action type."

        return {"success": success, "message": message}

    def terminate_fork(self):
        if not self.fork_active:
            return "No AI fork is active to terminate."
        
        self.fork_active = False
        self.fork_resources = {'cpu': 0, 'ram': 0}
        return "AI Fork terminated."

    def get_fork_status(self):
        return {"active": self.fork_active, "resources": self.fork_resources}
