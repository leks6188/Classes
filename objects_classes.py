from functools import total_ordering

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.course_lc:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        medium = self.grades.values()
        x = []
        for i in medium:
            x.extend(i)

        inprogress = (', ').join(self.courses_in_progress)
        fincourse = (', ').join(self.finished_courses)
        return (f'Имя: {self.name} \n'
        f'Фамилия: {self.surname} \n'
        f'Средняя оценка за домашние задания: {round(sum(x)/len(x),1)} \n'
        f'Курсы в процессе изучения: {inprogress}\n'
        f'Завершенные курсы: {fincourse}')

    def average_raiting(self):
        grades_ar = []
        for i in self.grades.values():
            grades_ar.extend(i)
        return round(sum(grades_ar) / len(grades_ar), 1)

    def __eq__(self, student_ar):
        return self.average_raiting() == student_ar.average_raiting()

    def __lt__(self, student_ar):
        return self.average_raiting() < student_ar.average_raiting()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

@total_ordering
class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name,surname)
        self.course_lc = []
        self.grades = {}
        self.grad = []

    def __str__(self):
        grades_lc = []
        for i in self.grades.values():
            grades_lc.extend(i)
        return (f' Имя: {self.name} \n'
                f' Фамилия: {self.surname} \n'
                f' Средняя оценка за лекции: {round(sum(grades_lc) / len(grades_lc), 1)}')

    def srzn(self):
        grades_lc = []
        for i in self.grades.values():
            grades_lc.extend(i)
        return round(sum(grades_lc) / len(grades_lc), 1)

    def __eq__(self, lector_gr):
        return self.srzn() == lector_gr.srzn()

    def __lt__(self, lector_gr):
        return self.srzn() < lector_gr.srzn()

class Reviever(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f' Имя: {self.name} \n'
                f' Фамилия: {self.surname} \n')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Go', 'C++']
best_student.finished_courses += ['OOP']

bad_student = Student('Drako', 'Malfoy', 'male')
bad_student.courses_in_progress += ['Python', 'C++']
bad_student.finished_courses += ['Slizerin']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cold_mentor = Mentor('Severus','Snegg')
cold_mentor.courses_attached += ['Python', 'Potions']


hot_reviever = Reviever('Some','Buddy')
hot_reviever.courses_attached += ['Python', 'Go']
hot_reviever.rate_hw(best_student, 'Python', 2)
hot_reviever.rate_hw(best_student, 'Python', 10)
hot_reviever.rate_hw(best_student, 'Go', 10)


very_hot_reviuver = Reviever('Harley', 'Queen')
very_hot_reviuver.courses_attached += ['Python', 'Go', 'Psihology']
very_hot_reviuver.rate_hw(bad_student, 'C++',7)
very_hot_reviuver.rate_hw(bad_student, 'Python', 9)


lecturer1 = Lecturer('Some','Buddy')
lecturer1.course_lc += ['Python', 'C++']

lecturer2 = Lecturer('Captain','America')
lecturer2.course_lc += ['Python','Go']


best_student.rate_lc(lecturer1,'Python',3)
best_student.rate_lc(lecturer1, 'C++', 5)
bad_student.rate_lc(lecturer2, 'Python', 7)
bad_student.rate_lc(lecturer2, 'C++',9)

print(best_student)
print(bad_student)
print(best_student > bad_student)

print(lecturer1)
print(lecturer2)
print(lecturer1 == lecturer2)

print(hot_reviever)
print(very_hot_reviuver)


studets_list = [best_student,bad_student]
def get_medgrade_students(students_list, name_course):
    result = []
    for i in students_list:
        result.extend(i.grades[name_course])
    return sum(result)/len(result)
x = get_medgrade_students(studets_list,'Python')
print(f'Средняя оценка всех студентов по курсу: {x}')


lectors_list = [lecturer1,lecturer2]
def get_medgrade_lectors(lectors_list, name_course):
    res = []
    for n in lectors_list:
        res.extend(n.grades[name_course])
    return sum(res)/len(res)
y = get_medgrade_lectors(lectors_list,'Python')
print(f' Средняя оценка за ведение курса: {y}')
