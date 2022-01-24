from http import client
from pssh.clients import SSHClient


def get_the_connection_count(host, port):
    client = SSHClient(host, port)
    cmd = 'netstat -na | grep 80 | wc -l'
    host_out = client.run_command(cmd)
    for msg in host_out.stdout:
        print(msg)

get_the_connection_count(
    '192.168.31.56',
    32001
)
client = SSHClient('192.168.31.56', port=32001)
cmd = 'netstat -na | grep 80 | wc -l'
host_out = client.run_command(cmd)
for msg in host_out.stdout:
    print(msg)