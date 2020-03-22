from clickhouse_driver.client import Client
from client import OPCClient
from datetime import datetime
import random


class ClientDB:

    def __init__(self, url_server_click_haus='localhost'):
        self.client = Client(url_server_click_haus)
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
        self.client.execute(f'CREATE DATABASE IF NOT EXISTS {name_bd}')

    def create_table(self, name_tb: str):
        tmp = list()
        for field in self.list_fields:
            tmp.append(" ".join(i for i in [field, self.list_fields[field]]))
        tmp.append('data Date')
        field_table = ', '.join(i for i in tmp)
        sql = f"create table if not exists {name_tb} ({field_table}) " \
              f"ENGINE = MergeTree() " \
              f"PARTITION BY toYYYYMM(data) " \
              f"ORDER BY data;"
        self.client.execute(sql)
        return sql

    def insert_data(self, name_tb: str, list_value: list):
        #colums = 'data, '
        colums = ', '.join(i for i in self.list_fields)
        valu = ', '.join(str(i) for i in list_value)
        sql = f"insert INTO {name_tb} ({colums}) FORMAT Values ({valu})"
        #self.client.execute(sql)
        return sql

    def disconnect(self):
        print("Disconnect ClickHous")
        self.client.disconnect()

    def test(self):
        return self.client.execute('SHOW DATABASES')


def main():
    b = ClientDB()
    print(b.create_table('var'))
    #print(b.insert_data("test", []))


if __name__ == '__main__':
    main()
