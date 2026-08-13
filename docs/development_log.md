# APsystems-Connect Development Log

## Milestone 1
Lokale TCP-communicatie bewezen.

- ECU-R bereikbaar op poort 8899.
- Eerste ruwe data ontvangen.

---

## Milestone 2
Parser gebouwd.

- Current Power
- Today Energy
- Lifetime Energy

---

## Milestone 3 - TCP Connect

### Doel
De LocalECU class zelfstandig een TCP-verbinding laten opzetten met de ECU.

### Resultaat
- connect() geïmplementeerd.
- Verbinding met ECU op poort 8899 succesvol.
- connected-status toegevoegd.

### Opmerking
Tijdens de ontwikkeling bleek poort 8899 soms niet bereikbaar. Uiteindelijk vastgesteld dat de ECU de poort weer opent na activatie van de lokale AP-modus.

## Milestone 4 - Send

### Doel
Een commando naar de ECU versturen.

### Resultaat
- send() geïmplementeerd.
- Commando APS1100160001END succesvol verzonden.

## Milestone 5 - Receive

### Doel
Data van de ECU ontvangen.

### Resultaat
- receive() geïmplementeerd.
- Eerste succesvolle ontvangst van 96 bytes via LocalECU.
- Buffer_size als optionele parameter toegevoegd.

### Opmerking
De communicatieketen connect → send → receive functioneert volledig.

## Milestone 6 - Parser basispakket

### Doel
De ontvangen bytes omzetten naar bruikbare Python-waarden.

### Resultaat
Parser leest succesvol:
- ECU ID
- Lifetime Energy
- Current Power
- Today Energy

### Testresultaat
De parser geeft dezelfde waarden terug als eerder handmatig uit de ruwe data zijn afgeleid.

### Volgende stap
De byte-offsets centraliseren in parser.py door een parse_ecu_info()-functie te introduceren.

### ECU poort 8899 - observatie

Na herstel van de lokale AP-modus is poort 8899 ook in de normale
wifi-modus bereikbaar gebleven.

De bereikbaarheid wordt voorlopig periodiek gecontroleerd.
Een automatische powercycle van de ECU is daarom nog niet nodig.

**Status:** stabiel, verdere observatie gewenst.

### Milestone 7: ECU info uit parser succesvol

- ECU ID succesvol uit de ECU-response gehaald
- Lifetime Energy succesvol uitgelezen
- Current Power succesvol uitgelezen
- Today Energy succesvol uitgelezen
- `parse_ecu_info()` werkt correct met de ontvangen ECU-data
- Test uitgevoerd via `test_07_ecu_info.py`

### Milestone 8: Current Power uit parser succesvol

- `current_power` wordt succesvol uit de ECU-response gehaald via `parse_ecu_info()`
- De waarde wordt door de parser als Watt teruggegeven
- Test uitgevoerd via `test_08_current_power.py`
- De test is meerdere keren uitgevoerd en gaf de actuele productie correct weer
- `Current Power` vormt later de basis voor de betreffende sensor in Home Assistant

### Milestone 9: Lokale API-laag succesvol

- Nieuwe `local_api.py` toegevoegd als publieke interface voor lokale ECU-data
- `get_ecu_info()` combineert ECU-communicatie en parsing in één functie
- De bestaande `LocalECU`-driver uitgebreid met `close()` voor het correct sluiten van de TCP-verbinding
- De ECU-verbinding wordt met `try/finally` altijd netjes afgesloten
- Nieuwe test toegevoegd: `test_09_local_api.py`
- ECU ID, Lifetime Energy, Current Power en Today Energy worden succesvol via de lokale API-laag uitgelezen
- Hogere lagen hoeven hierdoor geen kennis meer te hebben van de TCP-communicatie of parser

### Milestone 10: APsystems core als zelfstandig Python-package

- De APsystems-logica is ondergebracht in `src/apsystems_connect_core`
- `api.py`, `auth.py`, `config.py`, `local_api.py`, `local_ecu.py` en `parser.py`
  vormen nu één zelfstandig Python-package
- `pyproject.toml` toegevoegd voor installatie van de core
- Core succesvol als editable package geïnstalleerd met `pip install -e .`
- Import van `apsystems_connect_core` werkt zonder `PYTHONPATH=src`
- `test_09_local_api.py` succesvol uitgevoerd zonder `PYTHONPATH`
- Tests 01 t/m 09 opnieuw succesvol gevalideerd na de refactor
- Cloud API opnieuw getest met HTTP 200
- Oude dubbele `local_ecu.py` en `parser.py` uit `custom_components` verwijderd
- Home Assistant-laag gescheiden van de APsystems core
- Home Assistant coordinator toegevoegd voor centrale polling van ECU-data
- Current Power sensor gebruikt voortaan `coordinator.data`
- Volgende stap: distributie/configuratie van de core voor Home Assistant uitwerken