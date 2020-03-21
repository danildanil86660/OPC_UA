from clickhouse_driver.client import Client

client = Client('localhost')
print(client.execute('SHOW TABLE'))


class ClientDB:

    def __int__(self, url_server_click_haus='localhost'):
        self.clien = Client(url_server_click_haus)
        self.list_parameters = {'Pressure': 'Float64',
                                'Humidity': 'Float64',
                                'Area_temperature': 'Float64',
                                'Work_temperature': 'Float64',
                                'pH_level': 'Float64',
                                'Weight': 'Float64',
                                'Fluid_flow': 'Float64',
                                'CO2_flow': 'Float64',
                                }

    def create_bd(self, name_bd: str):
        self.clien.execute(f'CREATE DATABASE IF NOT EXISTS {name_bd}')

    def create_table(self):
        pass
