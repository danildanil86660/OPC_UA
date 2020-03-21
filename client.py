from opcua import Client
import time

class Init_parametrs:

    def __init__(self, name, lower_bound, upper_bound):
        self.name = name
        self.restriction = [lower_bound, upper_bound]
        self.value = None

    def to_JSON(self):
        return {self.name: self.restriction, "value": self.value}

    def set_value(self, value):
        self.value = value


Parametrs = [Init_parametrs('Pressure', 0, 10e6), Init_parametrs('Humidity', 0, 100),
             Init_parametrs('Area_temperature', 15, 30), Init_parametrs('Work_temperature', 30, 90),
             Init_parametrs('pH_level', 0, 14), Init_parametrs('Weight', 1, 100),
             Init_parametrs('FLuid_flow', 1, 100), Init_parametrs('CO2_flow', 1, 100)]

url = "opc.tcp://127.0.0.1:48402/freeopcua/server/"

client = Client(url)
client.connect()
print('Client connected')

while True:
    Temp = client.get_node('ns=2; i=2')
    Temperature = Temp.get_value()

    Press = client.get_node('ns=2; i=3')
    Pressure = Press.get_value()

    Time = client.get_node('ns=2; i=4')
    Time_value = Time.get_value()

    Flow = client.get_node('ns=2; i=5')
    Flow_value = Flow.get_value()
    print(Time_value, Pressure, Temperature, Flow_value)

    time.sleep(1)
