'''
1.14 在不支援原生的比較運算的情形下排序物件
問題：
想排序(sort)同一類別(class)的物件，但沒原生支援(natively support)的比較運算可用。
解法：
內建的sorted()函式接受一個key引數，可藉此傳入一個可呼叫物件(callable)，這個callable會回傳物件中的某些值，而sorted會用這些值來比較物件。
可使用lambda以及operator.attrgetter()
討論：
可使用lambda以及operator.attrgetter()，attrgetter()速度通常較快一點，且多了「允許同時擷取出多個欄位」的功能。類似為字典使用operator.itemgetter()的選擇(1.13)。
也可套用到min()或max()這樣的函式。
'''
from operator import attrgetter


class User:
    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def __repr__(self) -> str:
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
# 可使用lambda以及operator.attrgetter()
print(sorted(users, key=lambda u: u.user_id))
print(sorted(users, key=attrgetter('user_id')))

# attrgetter()速度通常較快一點，且多了「允許同時擷取出多個欄位」的功能。
by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
print(by_name)

# 也可套用到min()或max()這樣的函式。
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
