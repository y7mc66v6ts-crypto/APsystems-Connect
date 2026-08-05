"""
===============================================================================
TEST 05 - RECEIVE DATA
===============================================================================

Doel
-----
Controleren of de LocalECU class data kan ontvangen van de ECU
na het versturen van een geldig commando.

Projectfase
-----------
Stap 5 van APsystems-Connect.

Status
------
IN ONTWIKKELING
===============================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from local_ecu import LocalECU

ecu = LocalECU("192.168.1.220")

command = "APS1100160001END\n"

print("===== RECEIVE TEST =====")

ecu.connect()

ecu.send(command)

data = ecu.receive()

print(f"Ontvangen bytes : {len(data)}")
print()
print("RAW HEX:")
print(data.hex())