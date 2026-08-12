"""
TEST 08 - CURRENT POWER

Doel:
Testen of de actuele productie van de zonnepanelen correct uit de
ECU-response kan worden gehaald.

De actuele productie wordt door de APsystems ECU aangeleverd als
current_power in Watt.

Deze waarde is belangrijk voor de toekomstige energiehuishouding
in Home Assistant, omdat hiermee bepaald kan worden hoeveel
zonnestroom op dit moment beschikbaar is.

Status:
- ECU verbinding: werkend
- Raw data ontvangen: werkend
- ECU informatie parseren: werkend
- Current Power uitlezen: deze test
- Home Assistant integratie: nog niet geïmplementeerd
"""


from apsystems_connect_core.local_ecu import LocalECU
from apsystems_connect_core.parser import parse_ecu_info


ecu = LocalECU("192.168.1.220")

print("===== CURRENT POWER TEST =====")

ecu.connect()

command = "APS1100160001END\n"

ecu.send(command)

data = ecu.receive()

info = parse_ecu_info(data)

# Current Power wordt door de parser uit de ECU-response gehaald
current_power = info["current_power"]

print(f"Current Power : {current_power} W")

"""
Referentie:
- Current Power wordt uit de ECU-response gehaald via parse_ecu_info().
- De waarde wordt door de parser als Watt teruggegeven.
- Test succesvol uitgevoerd met de lokale ECU op 192.168.1.220.
- Tijdens de test was de actuele productie 0 W.
- Deze waarde vormt later de basis voor de Current Power sensor in Home Assistant.
"""