from clickhouse_driver.client import Client

client = Client('192.168.56.1:8123')
print(client.execute('select 1'))
