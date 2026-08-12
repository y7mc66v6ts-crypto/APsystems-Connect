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


from apsystems_connect_core.local_ecu import LocalECU
from apsystems_connect_core.parser import parse_ecu_info

ecu = LocalECU("192.168.1.220")

command = "APS1100160001END\n"

print("===== PARSER TEST =====")

ecu.connect()
ecu.send(command)

data = ecu.receive()

info = parse_ecu_info(data)

print(f"ECU ID          : {info['ecu_id']}")
print(f"Lifetime Energy : {info['lifetime_energy']:.1f} kWh")
print(f"Current Power   : {info['current_power']} W")
print(f"Today Energy    : {info['today_energy']:.2f} kWh")