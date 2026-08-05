"""
Test 03 - Verbinding maken met de ECU

Doel:
- Socket openen
- Controleren dat connected=True wordt
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from local_ecu import LocalECU

ecu = LocalECU("192.168.1.220")

print("===== CONNECT TEST =====")

print(f"Voor connect(): {ecu.connected}")

ecu.connect()

print(f"Na connect():   {ecu.connected}")
print(f"Socket:         {ecu.socket}")