from server import OPCServer
from Initialization_Parametrs import Parametrs

opcs = OPCServer()
opcs.run()

while True:
    opcs.generate_data(opcs, Parametrs)
