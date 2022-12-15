# 從存取屬性值看Python風格property()
class Score():
    def __init__(self, score):
        self.score = score


stu = Score(50)
print(stu.score)
stu.score = 100
print(stu.score)
