import time

from opcua import Server
from random import randint
import datetime

server = Server()

url = "opt.tcp://192.168.1.187:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, 'Temperature', 0)
Press = Param.add_variable(addspace, 'Pressure', 0)
Time = Param.add_variable(addspace, 'Time', 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

print(f"Server start at {url}")
while True:
    Temperature = randint(10, 50)
    Pressure = randint(100, 999)
    TIME = datetime.datetime.now()

    print(TIME, Temperature, Pressure)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_writable(TIME)

    time.sleep(2)
