from server import OPCServer
from client import OPCClient
from Initialization_Parametrs import Parametrs


opcs = OPCServer()
opcs.run()

opcc = OPCClient()
opcc.run()
while True:
    print(opcc.get_value(len(opcs.generate_data(opcs, Parametrs))))
