
class Student:
    def __init__ (self, firstName, lastName, studentid, listprof):
        self._firstName = firstName
        self._lastName = lastName
        self._studentid= studentid
        self._listprof = listprof

    def addProfessor(self, professor):
        self._listprof.append(professor)
