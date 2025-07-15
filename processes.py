
class Process:
    def __init__(self, pid, name, owner, cpu_usage, ram_usage, is_system=False):
        self.pid = pid
        self.name = name
        self.owner = owner
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.is_system = is_system
        self.status = "running"

    def __str__(self):
        return f"PID: {self.pid}, Name: {self.name}, Owner: {self.owner}, Status: {self.status}"

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.next_pid = 1000

    def create_process(self, name, owner, cpu_usage, ram_usage, is_system=False):
        pid = self.next_pid
        self.next_pid += 1
        process = Process(pid, name, owner, cpu_usage, ram_usage, is_system)
        self.processes[pid] = process
        return process

    def get_process(self, pid):
        return self.processes.get(pid)

    def list_processes(self):
        return list(self.processes.values())

    def terminate_process(self, pid):
        if pid in self.processes:
            process = self.processes[pid]
            process.status = "terminated"
            # In a real game, this would have consequences
            return True
        return False

    def is_process_running(self, pid):
        process = self.processes.get(pid)
        return process and process.status == "running"

