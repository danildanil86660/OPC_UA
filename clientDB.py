from clickhouse_driver.client import Client

client = Client('localhost')
print(client.execute('SHOW TABLE'))


class ClientDB:

    def __int__(self, url_server_click_haus='localhost'):
        self.clien = Client(url_server_click_haus)
        self.list_fields = {'Pressure': 'Float64',
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
        tmp = list()
        for field in self.list_fields:
            tmp.append(" ".join(i for i in ["'" + field + "'", self.list_fields[field]]))

        field_table = ', '.join(i for i in tmp)
        sql = f'CREATE TABLE test_table({field_table})'
        self.clien.execute(sql)
        pass
