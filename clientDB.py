from clickhouse_driver.client import Client


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
        sql = f"create table if not exists testBD.{name_tb} ({field_table}) " \
              f"ENGINE = MergeTree() " \
              f"PARTITION BY toYYYYMM(data) " \
              f"ORDER BY data;"
        self.client.execute(sql)
        return sql

    def test(self):
        return self.client.execute('SHOW DATABASES')


def main():
    b = ClientDB()
    print(b.create_table("variable"))


if __name__ == '__main__':
    main()
