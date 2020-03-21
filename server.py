from opcua import Server
from random import uniform, seed

seed(42)
class OPCServer:

    def __init__(self, url="opc.tcp://127.0.0.1:48402/freeopcua/server/",
                 name="OPCUA_SIMULATION_SERVER"):
        self.url = url
        self.server = Server()
        self.server.set_endpoint(self.url)
        self.addspace = self.server.register_namespace(name)
        self.node = self.server.get_objects_node()
        self.Object_node = self.node.add_object(self.addspace, "Parameters")
        self.temp = 0
        self.list_variables = list()

    def set_variable(self, list_parameters: list):
        variable = list()
        for parameters in list_parameters:
            variable.append(self.Object_node.add_variable(self.addspace, f'{parameters.name}', 0))
        return variable

    def stop(self):
        self.server.stop()

    @staticmethod
    def set_values(variables: list, list_parameters: list):
        i = 0
        for var in variables:
<<<<<<< HEAD
            var.set_value(round(random.uniform(list_parameters[i].restriction[0], list_parameters[i].restriction[1]), 2))
=======
            var.set_writable()
            r = uniform(list_parameters[i].restriction[0], list_parameters[i].restriction[1])
            var.set_value(r)
>>>>>>> 076cbf11b65772f01fb3eba69f22ec9fcc6e3004
            i += 1

    #@staticmethod
    def generate_data(self, opc, parameters: list):
        if self.temp == 0:
            self.list_variables = opc.set_variable(parameters)
            self.temp += 1
        while True:
            opc.set_values(self.list_variables, parameters)
            return self.list_variables

    def run(self):
        self.server.start()
        print(f"Server start at {self.url}")
