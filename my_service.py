from server import OPCServer
from client import OPCClient
from clientDB import ClientDB
from Initialization_Parametrs import Parametrs

opcserver = OPCServer()
opcserver.run()
data = opcserver.generate_data(opcserver, parameters=Parametrs)

opcclient = OPCClient()
opcclient.run()
print(opcclient.get_value(data))

opcclient.stop()
opcserver.stop()
