"""
Test voor de publieke lokale APsystems API.

Controleert of get_ecu_info() de ECU-data correct
ophaalt via de nieuwe local_api-laag.
"""

from apsystems_connect_core.local_api import get_ecu_info


print("===== LOCAL API TEST =====")

info = get_ecu_info()

print("ECU ID          :", info["ecu_id"])
print("Lifetime Energy :", info["lifetime_energy"], "kWh")
print("Current Power   :", info["current_power"], "W")
print("Today Energy    :", info["today_energy"], "kWh")