# __repr__()
class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s' % self.name
    __repr__ = __str__


a = Name('Hung')
print(a)
