"""
Publieke interface voor lokale APsystems ECU-data.

Deze module combineert de communicatie met de ECU en het parsen
van de ontvangen data.
"""

from apsystems_connect_core.local_ecu import LocalECU
from apsystems_connect_core.parser import parse_ecu_info
from apsystems_connect_core.config import ECU_IP, ECU_PORT


def get_ecu_info():

    """Haal de actuele ECU-informatie lokaal op."""

    ecu = LocalECU(ECU_IP, ECU_PORT)

    try:
        ecu.connect()

        command = "APS1100160001END\n"
        ecu.send(command)

        data = ecu.receive()

        return parse_ecu_info(data)

    finally:
        ecu.close()