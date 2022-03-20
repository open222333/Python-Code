import os

command = 'ls -al'
result = os.popen(command)
print(result.read())

# 
host_data = {
    '172.105.55.247': 'root',
    '194.195.114.53': 'root'
}
path = '/Users/4ge0/.ssh/test_id_rsa.pub'

for host in host_data:
    command = f'ssh-copy-id -i {path} {host_data[host]}@{host}'
    print(command)
    # os.system(command)
