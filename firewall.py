class Firewall:
    def __init__(self, rules_content=""):
        self.rules = self._parse_rules(rules_content)

    def _parse_rules(self, content):
        rules = []
        for line in content.split('\n'):
            line = line.strip()
            if line and not line.startswith('#'): # Ignore empty lines and comments
                parts = line.split()
                if len(parts) >= 3 and parts[0].upper() in ['ALLOW', 'DENY']:
                    action = parts[0].upper()
                    port = parts[1]
                    source = parts[2] if len(parts) > 2 else 'ANY'
                    rules.append({'action': action, 'port': port, 'source': source})
        return rules

    def add_rule(self, action, port, source='ANY'):
        new_rule = {'action': action.upper(), 'port': port, 'source': source}
        if new_rule not in self.rules:
            self.rules.append(new_rule)
            print(f"Added rule: {action} {port} from {source}")
            return True
        print(f"Rule already exists: {action} {port} from {source}")
        return False

    def delete_rule(self, action, port, source='ANY'):
        rule_to_delete = {'action': action.upper(), 'port': port, 'source': source}
        if rule_to_delete in self.rules:
            self.rules.remove(rule_to_delete)
            print(f"Deleted rule: {action} {port} from {source}")
            return True
        print(f"Rule not found: {action} {port} from {source}")
        return False

    def alter_rule(self, old_action, old_port, old_source, new_action=None, new_port=None, new_source=None):
        old_rule = {'action': old_action.upper(), 'port': old_port, 'source': old_source}
        if old_rule in self.rules:
            index = self.rules.index(old_rule)
            if new_action: old_rule['action'] = new_action.upper()
            if new_port: old_rule['port'] = new_port
            if new_source: old_rule['source'] = new_source
            self.rules[index] = old_rule
            print(f"Altered rule from {old_action} {old_port} from {old_source} to {old_rule['action']} {old_rule['port']} from {old_rule['source']}")
            return True
        print(f"Rule not found for alteration: {old_action} {old_port} from {old_source}")
        return False

    def serialize_rules(self):
        return '\n'.join([f"{rule['action']} {rule['port']} {rule['source']}" for rule in self.rules])

    def get_rules(self):
        return self.rules

# Example Usage:
if __name__ == "__main__":
    initial_rules = """
    ALLOW 22 ANY
    DENY 8080 192.168.1.100
    ALLOW 443 ANY
    """
    firewall = Firewall(initial_rules)
    print("Initial Rules:\n" + firewall.serialize_rules())

    firewall.add_rule("ALLOW", "80", "ANY")
    firewall.delete_rule("DENY", "8080", "192.168.1.100")
    firewall.alter_rule("ALLOW", "22", "ANY", new_port="2222")

    print("\nModified Rules:\n" + firewall.serialize_rules())
