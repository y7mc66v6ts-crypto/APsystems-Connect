"""
TEST 07 - ECU INFO

Doel:
Testen of we de basisinformatie uit de ECU-response correct kunnen
uitlezen via parse_ecu_info().

Deze test controleert momenteel:
- ECU ID
- Lifetime Energy
- Current Power
- Today Energy

De test gebruikt een echte verbinding met de APsystems ECU via TCP
poort 8899.

Belangrijk:
Dit is nog een zelfstandige test. De uiteindelijke LocalECU-class
gaat deze parser later zelf aanroepen.

Status:
- ECU verbinding: werkend
- Raw data ontvangen: werkend
- ECU informatie parseren: werkend
- Home Assistant integratie: nog niet geïmplementeerd
"""


from local_ecu import LocalECU
from parser import parse_ecu_info


ecu = LocalECU("192.168.1.220")

print("===== ECU INFO TEST =====")

ecu.connect()

command = "APS1100160001END\n"

ecu.send(command)

data = ecu.receive()

info = parse_ecu_info(data)

print(f"ECU ID          : {info['ecu_id']}")
print(f"Lifetime Energy : {info['lifetime_energy']:.1f} kWh")
print(f"Current Power   : {info['current_power']} W")
print(f"Today Energy    : {info['today_energy']:.2f} kWh")


# De parser zet de ruwe ECU-response om naar begrijpelijke waarden.
# Deze test controleert of de belangrijkste ECU-informatie correct
# uit de response wordt gehaald.