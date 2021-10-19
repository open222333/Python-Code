import os

command = 'ls -al'
result = os.popen(command)
print(result.read())
