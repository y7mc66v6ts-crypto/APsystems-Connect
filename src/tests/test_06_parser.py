"""
===============================================================================
TEST 06 - PARSER
===============================================================================

Doel
-----
Controleren of de parser ruwe ECU-data kan omzetten naar leesbare waarden.

Projectfase
-----------
Stap 6 van APsystems-Connect.

Eerste test
-----------
Uitlezen van de ECU-ID.

Status
------
PASSED
===============================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from local_ecu import LocalECU
from parser import read_string, read_int

ecu = LocalECU("192.168.1.220")

command = "APS1100160001END\n"

print("===== PARSER TEST =====")

ecu.connect()
ecu.send(command)

data = ecu.receive()

ecu_id = read_string(data, 13, 12)

print(f"ECU ID : {ecu_id}")
lifetime_energy = read_int(data, 27, 4) / 10
current_power = read_int(data, 31, 4)
today_energy = read_int(data, 35, 4) / 100

print(f"Lifetime Energy : {lifetime_energy:.1f} kWh")
print(f"Current Power   : {current_power} W")
print(f"Today Energy    : {today_energy:.2f} kWh")