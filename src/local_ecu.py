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

    def send(self, command):

        """Verstuur een commando naar de ECU."""

        self.socket.sendall(command.encode("utf-8"))

    def receive(self, buffer_size=4096):

        """Ontvang data van de ECU.

    Parameters
    ----------
    buffer_size : int, optional
        Maximum aantal bytes dat in één keer wordt ontvangen.
        Standaard: 4096 bytes.

    Returns
    -------
    bytes
        De ruwe data die door de ECU is verzonden.
    """

        return self.socket.recv(buffer_size)

        return data

    def get_current_power(self):
        pass

    def get_today_energy(self):
        pass

    def get_lifetime_energy(self):
        pass