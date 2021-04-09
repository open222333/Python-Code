from typing import get_args


class Score():
    def __init__(self, score):
        self.__score = score

    def getscore(self):
        print("inside the getscore")
        return self.__score

    def setscore(self, score):
        print("inside the setscore")
        self.__score = score
    sc = property(getscore, setscore) # Python風格
