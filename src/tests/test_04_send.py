"""
===============================================================================
TEST 04 - SEND COMMAND
===============================================================================

Doel
-----
Controleren of de LocalECU class een commando succesvol kan versturen
naar de APsystems ECU via een reeds geopende TCP-verbinding.

Projectfase
-----------
Stap 4 van APsystems-Connect.

Geteste functionaliteit
-----------------------
- connect() opent een TCP-verbinding.
- send() verstuurt een ASCII-commando naar de ECU.
- De TCP-verbinding blijft actief na het verzenden.
- Het socket-object blijft geldig.

Verzonden commando
------------------
APS1100160001END

Dit is het basiscommando waarmee de ECU algemene systeeminformatie
terugstuurt, waaronder:

- ECU-ID
- Current Power
- Today Energy
- Lifetime Energy
- Firmwareinformatie
- Aantal aangesloten omvormers

Opmerking:
Deze test controleert uitsluitend het VERSTUREN van het commando.
Het ontvangen van de data wordt afzonderlijk getest in test_05_receive.py.

Verwachte uitvoer
-----------------
===== SEND TEST =====

Verbonden
Verstuur: APS1100160001END

Commando verzonden.

Connected : True
Socket    : True

Belangrijke observaties
-----------------------
- send() gebruikt de bestaande TCP-verbinding.
- Er wordt geen nieuwe socket geopend.
- De verbinding blijft actief na het verzenden.
- Er wordt nog geen data gelezen; de ECU wacht op een recv()-aanroep.

Status
------
PASSED
===============================================================================
"""


from apsystems_connect_core.local_ecu import LocalECU

ecu = LocalECU("192.168.1.220")

print("===== SEND TEST =====")

ecu.connect()

print("Verbonden")

command = "APS1100160001END\n"

print(f"Verstuur: {command.strip()}")

ecu.send(command)

print("Commando verzonden.")
print(f"Connected : {ecu.connected}")
print(f"Socket    : {ecu.socket is not None}")
