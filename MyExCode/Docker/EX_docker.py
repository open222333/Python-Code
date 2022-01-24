import re
import docker


def get_container_name():
    containe_name = []
    for container in docker.from_env().containers.list():
        containe_name.append(container.name)
    return containe_name


def get_container_port_connection_count(port, *container_name):
    '''https://docker-py.readthedocs.io/en/stable/containers.html'''
    client = docker.from_env()
    stack = []

    for c in client.containers.list():
        if c.name in container_name:
            container = client.containers.get(c.name)
            result = container.exec_run(
                # cmd='netstat -na | grep 3306 | grep ESTABLISHED | wc -l',
                cmd=f'netstat -na | grep {port}',
                tty=True
            )
            result_str = bytes(result.output).decode('utf-8')
            count = len(re.findall(r'ESTABLISHED', result_str))
            stack.append((c.name, count))
    return stack


print(get_container_port_connection_count('3306', 'mysql', 'mysql_1', 'mysql_2'))
