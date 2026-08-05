class LocalECU:

    def __init__(self, ip, port=8899):
        self.ip = ip
        self.port = port

        self.socket = None
        self.connected = False

    def connect(self):
        pass

    def send(self):
        pass

    def receive(self):
        pass

    def get_current_power(self):
        pass

    def get_today_energy(self):
        pass

    def get_lifetime_energy(self):
        pass