from threading import Thread


def add_job(func):
    t = Thread(target=func)
    t.start()


def testa():
    for i in range(1, 10):
        print(f'testa : {i}')


def testb():
    for i in range(1, 10):
        print(f'testb : {i}')


count = 0
while count < 50:
    add_job(testa)
    add_job(testb)
    count += 1
