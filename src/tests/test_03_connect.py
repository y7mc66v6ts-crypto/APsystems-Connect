"""
===============================================================================
TEST 03 - TCP CONNECTIE
===============================================================================

Doel
-----
Controleren of de LocalECU class zelfstandig een TCP-verbinding kan openen
naar de APsystems ECU-R.

Projectfase
-----------
Stap 3 van APsystems-Connect.

Geteste functionaliteit
-----------------------
- LocalECU object bestaat.
- connect() opent een TCP socket.
- connected verandert van False naar True.
- socket object wordt opgeslagen in self.socket.

Verwachte uitvoer
-----------------
===== CONNECT TEST =====

Voor connect(): False
Na connect():   True

Socket:
<socket.socket ...>

Belangrijke observaties
-----------------------
- ECU-R model: 2160-serie
- Communicatie via TCP poort 8899.
- De beschikbaarheid van poort 8899 lijkt afhankelijk te zijn van de
  toestand van de ECU.
- Tijdens de ontwikkeling is waargenomen dat poort 8899 soms niet bereikbaar
  was (Connection Refused), terwijl de ECU wel reageerde op ping.
- Na activeren van de AP-modus en vervolgens terugkeren naar normale
  wifi-werking werd poort 8899 weer bereikbaar.
- De exacte oorzaak is nog onbekend en wordt verder onderzocht.
- Er wordt bewust nog geen workaround (zoals een automatische powercycle)
  ingebouwd zolang de oorzaak niet is vastgesteld.

Status
------
PASSED
"""


from apsystems_connect_core.local_ecu import LocalECU

ecu = LocalECU("192.168.1.220")

print("===== CONNECT TEST =====")

print(f"Voor connect(): {ecu.connected}")

ecu.connect()

print(f"Na connect():   {ecu.connected}")
print(f"Socket:         {ecu.socket}")