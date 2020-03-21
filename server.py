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
a = Param.add_variable(addspace, 'Temperature', 0)
Temp = a(addspace, 'Temperature', 0)
Press = a(addspace, 'Pressure', 0)
Flow = a(addspace, 'Flow', 0)
Time = a(addspace, 'Time', 0)

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
    print(TIME)
    time.sleep(1)

    class OPCServer:

        def __init__(self, url="opc.tcp://127.0.0.1:48402/freeopcua/server/",
                     name="OPCUA_SIMULATION_SERVER"):
            self.server = Server()
            self.server.set_endpoint(url)
            self.addspace = self.server.register_namespace(name)
            self.node = self.server.get_objects_node()
            self.Param = node.add_object(addspace, "Parameters")

        def set_parameters(self, list_parameters: list):
            function_Parameters = list()
            for parameters in list_parameters:
                function_Parameters.clear()
                function_Parameters.append(Param.add_variable(addspace, f'{parameters}', 0))
            for function in function_Parameters:
                # TODO как вызывать функции из списка
                pass

        def run(self):
            self.server.start()
            print(f"Server start at {url}")

