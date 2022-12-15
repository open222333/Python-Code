import os

command = 'ls -al'
result = os.popen(command)
print(result.read())

#
host_data = {
    '127.0.0.1': 'root',
    '127.0.0.1': 'root'
}
path = '/Users/4ge0/.ssh/test_id_rsa.pub'

for host in host_data:
    command = f'ssh-copy-id -i {path} {host_data[host]}@{host}'
    print(command)
    # os.system(command)
