"""
local_ecu.py

Driver voor lokale communicatie met een APsystems ECU-R via TCP-poort 8899.
"""

import socket


class LocalECU:

    def __init__(self, ip, port=8899):
        self.ip = ip
        self.port = port

        self.socket = None
        self.connected = False

    def connect(self):

        """Maak verbinding met de ECU."""

        self.socket = socket.create_connection(
            (self.ip, self.port),
            timeout=5,
    )

        self.connected = True

    def send(self):
        pass

    def receive(self):
        pass

    def get_current_power(self):
        pass

    def get_today_energy(self):
        pass

    def get_lifetime_energy(self):
        pass