from opcua import Client
import time

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
