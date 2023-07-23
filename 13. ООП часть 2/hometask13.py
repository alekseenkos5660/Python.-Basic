# Создать иерархию классов для описания академии.
# Примерный список классов: Person, Teacher, Student, Subject, Academy и тд.
# Продумать архитектуру: реализовать принципы ООП

class Faculty:
    __faculty: str = "no name"

    def __init__(self, faculty):
        self.faculty = faculty

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        if 2 < len(faculty) < 50:
            self.__faculty = faculty
        else:
            print("Incorrect faculty name!")

    def show_info(self):
        print(f"Faculty: {self.faculty}")


class Department(Faculty):
    __department: str = "no name"

    def __init__(self, faculty, department):
        super().__init__(faculty)
        self.department = department

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        if 2 < len(department) < 50:
            self.__department = department
        else:
            print("Incorrect department name!")

    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}")


class Speciality(Department):
    __speciality = "no name"

    def __init__(self, faculty, department, speciality):
        super().__init__(faculty, department)
        self.speciality = speciality

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, speciality):
        if 2 < len(speciality) < 50:
            self.__speciality = speciality
        else:
            print("Incorrect department name!")

    def show_info(self):
        super().show_info()
        print(f"Speciality: {self.speciality}")


class Subject(Speciality):
    __subject: str = "no name"

    def __init__(self, faculty, department, speciality, subject):
        super().__init__(faculty, department, speciality)
        self.subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        if 2 < len(subject) < 50:
            self.__subject = subject
        else:
            print("Incorrect subject name!")

    def show_info(self):
        super().show_info()
        print(f"Subject: {self.subject}")


class Person:
    __name: str = "no name"
    __age: int = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 < len(name) < 50:
            self.__name = name
        else:
            print("Incorrect name!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 15 <= age <= 150:
            self.__age = age
        else:
            print("Incorrect age!")

    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class Student(Person, Speciality):
    __academy: str = "no name"

    def __init__(self, name, age, academy, faculty, department, speciality):
        Person.__init__(self, name, age)
        Speciality.__init__(self, faculty, department, speciality)
        self.academy = academy

    @property
    def academy(self):
        return self.__academy

    @academy.setter
    def academy(self, academy):
        if 2 < len(academy) < 50:
            self.__academy = academy
        else:
            print("Incorrect academy name!")

    def show_info(self):
        super().show_info()
        print(f"Academy: {self.academy}")
        Speciality.show_info(self)


class Teacher(Person, Subject):
    __academy: str = "no name"

    def __init__(self, name, age, academy, faculty, department, speciality, subject):
        Person.__init__(self, name, age)
        Subject.__init__(self, faculty, department, speciality, subject)
        self.academy = academy

    @property
    def academy(self):
        return self.__academy

    @academy.setter
    def academy(self, academy):
        if 2 < len(academy) < 50:
            self.__academy = academy
        else:
            print("Incorrect academy name!")

    def show_info(self):
        super().show_info()
        print(f"Academy: {self.academy}")
        Subject.show_info(self)


class Building:
    __num_of_floors: int = 1
    __square: int = 1

    def __init__(self, num_of_floors, square):
        self.__num_of_floors = num_of_floors
        self.__square = square

    @property
    def num_of_floors(self):
        return self.__num_of_floors

    @num_of_floors.setter
    def num_of_floors(self, num_of_floors):
        if 0 < num_of_floors <= 150:
            self.__num_of_floors = num_of_floors
        else:
            print("Incorrect number of floors!")

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, square):
        if 10 <= square <= 150000:
            self.__square = square
        else:
            print("Incorrect square!")

    def show_info(self):
        print(f"Number of floors: {self.num_of_floors}\nSquare: {self.square}")


class Institution:
    __name: str = "no name"
    __specialization: str = "no specialization"

    def __init__(self, name, specialization):
        self.__name = name
        self.__specialization = specialization

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 < len(name) <= 50:
            self.__name = name
        else:
            print("Incorrect education institution name!")

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, specialization):
        if 2 <= len(specialization) <= 50:
            self.__specialization = specialization
        else:
            print("Incorrect specialization!")

    def show_info(self):
        print(f"Name of education institution: {self.name}\nSpecialization: {self.specialization}")


class Academy(Institution, Building):
    def __init__(self, name, specialization, num_of_floors, square):
        Institution.__init__(self, name, specialization)
        Building.__init__(self, num_of_floors, square)

    def show_info(self):
        print(f"Name of the academy: {self.name}\nSpecialization: {self.specialization}\n"
              f"Number of floors: {self.num_of_floors}\nSquare: {self.square}")


f_lty = Faculty("Gryffindor")
f_lty.show_info()
dep = Department("Gryffindor", "Magic")
dep.show_info()
spec = Speciality("Gryffindor", "Magic", "Brewing")
spec.show_info()
subj = Subject("Gryffindor", "Magic", "Brewing", "Poisons")
subj.show_info()
pers = Person("Hagrid", 63)
pers.show_info()
harry = Student("Harry", 18, "Hogwarts", "Gryffindor", "Magic", "Brewing")
harry.show_info()
horace = Teacher("Horace", 80, "Hogwarts", "Gryffindor", "Magic", "Brewing", "Poisons")
horace.show_info()
building = Building(16, 100)
building.show_info()
institution = Institution("Hogwarts", "Magic")
institution.show_info()
hogwarts = Academy("Hogwarts", "Magic", 7, 126187000)
hogwarts.show_info()
