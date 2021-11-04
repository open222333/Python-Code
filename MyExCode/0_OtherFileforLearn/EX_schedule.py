import schedule
import time
'''輕排程'''


class Test():
    def tesst(self):
        return self.test('sss')

    def test(self, s, s2):
        print(s, s2)

    def run(self):
        for i in range(5):
            if i < 5:
                schedule.every().sunday.at('18:45').do(self.test, str(i), 't2')
                schedule.every().saturday.at('22:29').do(self.tesst)


def job():
    print("I'm working...")


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
