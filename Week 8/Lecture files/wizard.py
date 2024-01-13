class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def _init__(self, name, house):
        super().__init__(name)
        self.house = house


    ...

class Proffesor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
proffesor = Proffesor("Severus", "Defense Against the Dark Arts")
