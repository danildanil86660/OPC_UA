import time
from opcua import Server
from random import randint
import datetime

server = Server()

url = "opc.tcp://127.0.0.1:48402/freeopcua/server/"
server.set_endpoint(url)
#server.set_application_uri(url)
name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, 'Temperature', 0)
Press = Param.add_variable(addspace, 'Pressure', 0)
Flow = Param.add_variable(addspace, 'Flow', 0)
Time = Param.add_variable(addspace, 'Time', 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()
Flow.set_writable()
server.start()
print(f"Server start at {url}")
while True:
    Temperature = randint(10, 50)
    Pressure = randint(100, 999)
    TIME = datetime.datetime.now()
    FLOW = randint(50, 60)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)
    Flow.set_value(FLOW)

    time.sleep(1)
