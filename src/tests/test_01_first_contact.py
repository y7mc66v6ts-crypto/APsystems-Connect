import socket

from parser import read_string, read_int

ECU_IP = "192.168.1.220"
ECU_PORT = 8899

COMMAND = "APS1100160001END\n"

print(f"Verbinden met {ECU_IP}:{ECU_PORT}...")

sock = socket.create_connection((ECU_IP, ECU_PORT), timeout=5)

print("Verbonden!")
print(f"Verstuur: {COMMAND.strip()}")

sock.sendall(COMMAND.encode("utf-8"))

data = sock.recv(4096)

print()
print(f"{len(data)} bytes ontvangen")
print()

print("HEX:")
print(data.hex())

print()
print("RAW:")
print()
print("===== GEDECODEERD =====")

ecu_id = read_string(data, 13, 12)

lifetime = read_int(data, 27, 4) / 10
current_power = read_int(data, 31, 4)
today = read_int(data, 35, 4) / 100

print("ECU ID          :", ecu_id)
print("Lifetime Energy :", lifetime, "kWh")
print("Current Power   :", current_power, "W")
print("Today Energy    :", today, "kWh")

sock.close()