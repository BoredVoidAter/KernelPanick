
class Process:
    def __init__(self, pid, name, owner, cpu_usage, ram_usage, is_system=False):
        self.pid = pid
        self.name = name
        self.owner = owner
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.is_system = is_system
        self.status = "running"
        self.injected_code_output = []

    def __str__(self):
        return f"PID: {self.pid}, Name: {self.name}, Owner: {self.owner}, Status: {self.status}"

    def inject_code(self, code_payload):
        # Simulate code injection and execution
        # In a real game, this would be more complex, potentially affecting process behavior
        # For now, we'll just store the payload and simulate some output
        print(f"Injecting code into process {self.pid} ({self.name})...")
        self.injected_code_output.append(f"Process {self.name} executed injected code: {code_payload}")
        if "read protected file" in code_payload.lower():
            self.injected_code_output.append("Simulating read of protected file: 'Sensitive data accessed!'")
        elif "leak data" in code_payload.lower():
            self.injected_code_output.append("Simulating data leak: 'User credentials: admin/password123' ")
        return True

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

    def inject_code_into_process(self, pid, code_payload):
        process = self.get_process(pid)
        if process and process.status == "running":
            return process.inject_code(code_payload)
        return False

    def get_injected_code_output(self, pid):
        process = self.get_process(pid)
        if process:
            return process.injected_code_output
        return []

