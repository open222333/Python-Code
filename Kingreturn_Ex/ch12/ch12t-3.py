class Myschool():
    title = "明志科大"
    schoolname = 'Python School'

    def departments(self):
        return ['機械', '電機', '化工']

    def msg(self):
        print(self.schoolname)


A = Myschool()
print(A.title)
print(A.departments())
print(A.schoolname)
