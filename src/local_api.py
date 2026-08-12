"""
Publieke interface voor lokale APsystems ECU-data.

Deze module combineert de communicatie met de ECU en het parsen
van de ontvangen data.
"""

from local_ecu import LocalECU
from parser import parse_ecu_info

def get_ecu_info():
    """Haal de actuele ECU-informatie lokaal op."""

    ecu = LocalECU("192.168.1.220")

    try:
        ecu.connect()

        command = "APS1100160001END\n"
        ecu.send(command)

        data = ecu.receive()

        return parse_ecu_info(data)

    finally:
        ecu.close()