import time
from opcua import Server
from random import randint
from Initialization_Parametrs import Parametrs


class OPCServer:

    def __init__(self, url="opc.tcp://127.0.0.1:48402/freeopcua/server/",
                 name="OPCUA_SIMULATION_SERVER"):
        self.url = url
        self.server = Server()
        self.server.set_endpoint(self.url)
        self.addspace = self.server.register_namespace(name)
        self.node = self.server.get_objects_node()
        self.Object_node = self.node.add_object(self.addspace, "Parameters")

    def set_variable(self, list_parameters: list):
        variable = list()
        for parameters in list_parameters:
            variable.append(self.Object_node.add_variable(self.addspace, f'{parameters.name}', 0))
        return variable


    def set_value(self, variables: list, list_parameters: list):
        i = 0
        for var in variables:
            var.set_writable()
            var.set_value(randint(list_parameters[i].restriction[0], list_parameters[i].restriction[1]))
            i += 1
        return variables

    def run(self):
        self.server.start()
        print(f"Server start at {self.url}")


opc = OPCServer()
opc.run()

while True:
    list_variables = opc.set_variable(Parametrs)
    value = opc.set_value(list_variables, Parametrs)
    for v in value:
        print(v.get_value())
    #time.sleep(1)

