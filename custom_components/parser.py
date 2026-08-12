"""
Parser voor lokale data van een APsystems ECU-R.

Zet de ruwe bytes uit de ECU-response om naar bruikbare waarden.
"""


def read_string(data, start, length):
    return data[start:start + length].decode("utf-8")


def read_int(data, start, length):
    return int.from_bytes(
        data[start:start + length],
        byteorder="big",
    )


def parse_ecu_info(data):
    ecu_id = read_string(data, 13, 12)
    lifetime_energy = read_int(data, 27, 4) / 10
    current_power = read_int(data, 31, 4)
    today_energy = read_int(data, 35, 4) / 100

    return {
        "ecu_id": ecu_id,
        "lifetime_energy": lifetime_energy,
        "current_power": current_power,
        "today_energy": today_energy,
    }