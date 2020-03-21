from clickhouse_driver.client import Client

client = Client('localhost')
print(client.execute('SHOW TABLE'))
