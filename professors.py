
class Professor:
    def __init__(self, firstName, last, listofStudents):
        self._firstName = firstName
        self._lastName = last
        self._listStudents = listofStudents

    def addStudents(self, student):
        self._listStudents.append(student)