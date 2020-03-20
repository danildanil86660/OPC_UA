from opcua import Client
import time

url = "opt.tcp://192.168.1.187:4840"

client = Client(url)

client.connect()
print('Client connected')

while True:
    Temp = client.get_node('ns=2; i=2')
    Temperature = Temp.get_value()
    print(Temperature)

    Press = client.get_node('ns=2; i=3')
    Pressure = Press.get_value()
    print(Pressure)

    Time = client.get_node('ns=2; i=4')
    Time_value = Time.get_value()
    print(Time_value)

    time.sleep(1)