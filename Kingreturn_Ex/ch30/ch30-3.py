import datetime

timeStop = datetime.datetime(2021, 3, 30, 2, 26, 0)
while datetime.datetime.now() < timeStop:
    print("program is sleeping.", end='')
print("Wake up")
