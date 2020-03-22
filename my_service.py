from server import OPCServer
from client import OPCClient
from clientDB import ClientDB
from Initialization_Parametrs import Parametrs

opcserver = OPCServer()
opcserver.run()
data = opcserver.generate_data(opcserver, parameters=Parametrs)

opcclient = OPCClient()
opcclient.run()


cliendb = ClientDB()
cliendb.create_table('variable')
for i in range(0, 100):
    opcserver.set_variable(Parametrs)
    val = opcclient.get_value(data)
    print(cliendb.insert_data('variable', val))
cliendb.disconnect()

opcclient.stop()
opcserver.stop()
