"""
Status: PASSED
Datum: 2026-08-05

Stap 2:
Initialisatie van de LocalECU class succesvol getest.
"""

"""
Test 02 - Initialisatie van de LocalECU class

Doel:
- Een LocalECU-object aanmaken.
- Controleren dat de basisgegevens correct zijn opgeslagen.

Verwachte uitvoer:

IP         : 192.168.1.220
Port       : 8899
Connected  : False
Socket     : None
"""


from apsystems_connect_core.local_ecu import LocalECU

ecu = LocalECU("192.168.1.220")

print("===== INIT TEST =====")
print(f"IP         : {ecu.ip}")
print(f"Port       : {ecu.port}")
print(f"Connected  : {ecu.connected}")
print(f"Socket     : {ecu.socket}")