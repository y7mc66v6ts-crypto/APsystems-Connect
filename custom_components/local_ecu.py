"""
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

    def send(self, command):
        """Verstuur een commando naar de ECU."""

        self.socket.sendall(command.encode("utf-8"))

    def receive(self, buffer_size=4096):
        """Ontvang ruwe data van de ECU."""

        return self.socket.recv(buffer_size)

    def close(self):
        """Sluit de verbinding met de ECU."""

        if self.socket is not None:
            self.socket.close()

        self.socket = None
        self.connected = False