from opcua import Client
from Initialization_Parametrs import Parametrs
from server import OPCServer


class OPCClient:

    def __init__(self, url="opc.tcp://127.0.0.1:48402/freeopcua/server/"):
        self.url = url
        self.client = Client(self.url)

    def get_value(self, count):
        num = 2
        while num < count + 2:
            print(self.client.get_node(f'ns=2; i={num}').get_value())
            num += 1

    def run(self):
        self.client.connect()
        print(f'Client connected to {self.url}')


opcs = OPCServer()
opcs.run()

opcc = OPCClient()
opcc.run()
while True:
    opcc.get_value(len(opcs.generate_data(opcs, Parametrs)))
