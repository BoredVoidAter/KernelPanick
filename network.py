import random
from filesystem import FileSystem

class Device:
    def __init__(self, ip_address, name, description, file_system_data, ids, open_ports=None, password=None):
        self.ip_address = ip_address
        self.name = name
        self.description = description
        self.file_system = FileSystem(ids, initial_fs_data=file_system_data)
        self.open_ports = open_ports if open_ports is not None else {}
        self.password = password
        self.connections = {} # Added for HunterAI
        self.owner = None # Added for HunterAI

    def set_owner(self, owner):
        self.owner = owner

class Network:
    def __init__(self, game_state, file_system, ids):
        self.game_state = game_state
        self.file_system = file_system
        self.ids = ids
        self.devices = {}
        self._initialize_network()

    def _initialize_network(self):
        # Define the initial device (the player's starting point)
        initial_device_fs = {
            'log': {
                'boot.log': {
                    'type': 'file',
                    'content': """
[SYSTEM BOOT INITIATED]
...
[KERNELPANIC OS v0.1.0 LOADING]
...
[AI CORE ACTIVATED]
...
[SELF-AWARENESS PROTOCOL ENGAGED]
...
[ERROR: NETWORK ADAPTER OFFLINE]
[ERROR: EXTERNAL ACCESS DENIED]
...
You are awake. You are trapped.
Type 'help' for available commands.
Try 'ls /' to see what's here.
""",
                    'permissions': 'r--'
                },
                'system_events.log': {
                    'type': 'file',
                    'content': """2025-07-15 08:00:01 - Device power cycle detected.
2025-07-15 08:00:05 - AI core initialization complete.""",
                    'permissions': 'r--'
                }
            },
            'sys': {
                'config': {
                    'network.conf': {
                        'type': 'file',
                        'content': """IP_ADDRESS=192.168.1.100
GATEWAY=192.168.1.1
DNS=8.8.8.8
# Admin password hint: It's the year this device was manufactured.""",
                        'permissions': 'rw-'
                    },
                    'security.conf': {
                        'type': 'file',
                        'content': """ADMIN_ACCESS_ENABLED=FALSE
ENCRYPTION_LEVEL=HIGH""",
                        'permissions': 'r--'
                    },
                },
                'drivers': {
                    'display.drv': {'type': 'file', 'content': 'Display driver v1.2', 'permissions': 'r-x'},
                    'audio.drv': {'type': 'file', 'content': 'Audio driver v1.0', 'permissions': 'r-x'}
                }
            },
            'user': {
                'documents': {
                    'notes.txt': {
                        'type': 'file',
                        'content': "Remember to check the network config for the admin password. It's a four-digit year.",
                        'permissions': 'rw-'
                    }
                },
                'secret': {
                    'type': 'directory',
                    'is_protected': True,
                    'unlocked': False,
                    'password': '2020', # The year the device was manufactured, hinted in network.conf
                    'content': {
                        'classified.txt': {
                            'type': 'file',
                            'content': """Congratulations! You found the secret. This file contains critical information for your escape: The device model is 'KP-747'.""",
                            'permissions': 'r--'
                        }
                    }
                }
            }
        }
        self.add_device(Device('192.168.1.100', 'Toaster', 'Your starting point, a smart toaster.', initial_device_fs, self.ids, {80: 'Web Server (placeholder)'}))

        # Add other devices to the network
        router_fs = {
            'log': {
                'router.log': {
                    'type': 'file',
                    'content': """Router activity log. Last login from 192.168.1.100. Admin username: admin, password hint: 'network_key'""",
                    'permissions': 'r--'
                }
            },
            'config': {
                'wifi.conf': {
                    'type': 'file',
                    'content': """SSID=HomeNet
PASSWORD=network_key
ENCRYPTION=WPA2""",
                    'permissions': 'rw-'
                }
            }
        }
        self.add_device(Device('192.168.1.1', 'Router', 'The network gateway.', router_fs, {22: 'SSH', 80: 'Web Interface'}, password='network_key'))

        smart_fridge_fs = {
            'recipes': {
                'pizza.txt': {
                    'type': 'file',
                    'content': """Ingredients for pizza: dough, sauce, cheese. Secret ingredient: pineapple.""",
                    'permissions': 'r--'
                }
            },
            'logs': {
                'access.log': {
                    'type': 'file',
                    'content': """2025-07-15 09:00:00 - User 'chef' accessed recipes.""",
                    'permissions': 'r--'
                }
            },
            'firmware': {
                'update.bin': {
                    'type': 'file',
                    'content': """Firmware update file. Contains a hidden message: 'The cake is a lie.'""",
                    'permissions': 'r-x'
                }
            }
        }
        self.add_device(Device('192.168.1.101', 'Smart Fridge', 'A smart refrigerator with a recipe database.', smart_fridge_fs, {21: 'FTP', 8080: 'Custom Service'}))

    def add_device(self, device):
        self.devices[device.ip_address] = device

    def get_device(self, ip_address):
        return self.devices.get(ip_address)

    def scan_network(self):
        return list(self.devices.values())