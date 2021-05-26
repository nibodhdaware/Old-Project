class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)


s1 = Student('Nibodh', 5)

s1.show()
