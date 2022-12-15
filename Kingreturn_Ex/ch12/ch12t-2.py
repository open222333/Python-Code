class Myschool():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def msg(self):
        print("Hi ,%s. Your Score is %d" % (self.name.title(), self.score))


hung = Myschool('kevin', 80)
hung.msg()
