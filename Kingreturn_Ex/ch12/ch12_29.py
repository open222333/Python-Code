# __str__()
class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s' % self.name


a = Name('Hung')
print(a)
