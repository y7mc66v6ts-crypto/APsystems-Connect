def read_string(data, start, length):
    return data[start:start + length].decode("utf-8")


def read_int(data, start, length):
    return int.from_bytes(
        data[start:start + length],
        byteorder="big",
    )