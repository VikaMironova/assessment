class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                       f'Средняя оценка за домашнее задание: {average_grade(self.grades)}\nКурсы в процессе изучения:' \
                       f' {"".join(self.courses_in_progress)}\n' \
                       f'Завершенные курсы: {"".join(self.finished_courses)}'
        return some_student

    def rate_lecturer(self, specific_lecturer, course, grade):
        if isinstance(specific_lecturer, Lecturer) \
                and course in specific_lecturer.courses_attached \
                and course in self.courses_in_progress \
                and 0 < grade <= 10:

            specific_lecturer.grades.append(grade)

        else:
            return 'Ошибка'

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return average_grade(self.grades) < average_grade(other_student.grades)
        else:
            return None


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}'
        return some_lecturer

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return average_grade(self.grades) < average_grade(other_lecturer.grades)
        else:
            return None


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_grade(all_grades):
    if type(all_grades) is dict:
        amount_grades = []
        for grades in all_grades.values():
            for grade in grades:
                amount_grades.append(grade)
        return average_grade(amount_grades)
    elif type(all_grades) is list and all_grades[0] is not None:
        average = round(sum(all_grades) / len(all_grades), 2)
        return average
    else:
        return 'Ошибка'


def average_course_grade(all_students, current_course):
    all_course_grades = []
    for current_student in all_students:
        if current_course in current_student.grades.keys():
            for every_grade in current_student.grades.get(current_course):
                all_course_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у студента {current_student.name} {current_student.surname}')
    return average_grade(all_course_grades)


def average_lecturers_grade(all_lecturers):
    all_lecturers_grades = []
    for current_lecturer in all_lecturers:
        for every_grade in current_lecturer.grades:
            all_lecturers_grades.append(every_grade)
    return average_grade(all_lecturers_grades)


# Студенты
student_1 = Student('Kirill', 'Kirkorov', 'M')
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['C++']
student_1.grades['Java'] = [1, 5, 6, 2]
student_1.grades['C++'] = [10, 2, 8, 5]

student_2 = Student('Boris', 'Baskov', 'M')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['C++']
student_2.grades['Java'] = [10, 10, 8, 8]
student_2.grades['C++'] = [5, 7, 3, 10]

student_list = [student_1, student_2]

# Лекторы
lecturer_1 = Lecturer('Egor', 'Egorov')
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['C++']

lecturer_2 = Lecturer('Brad', 'Pitt')
lecturer_2.courses_attached += ['Java']
lecturer_2.courses_attached += ['C++']

lecturer_list = [lecturer_1, lecturer_2]

# Проверяющий
reviewer_1 = Reviewer('Jason', 'Statham')
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Angelina', 'Jolie')
reviewer_2.courses_attached += ['С++']

# Проверяющий ставит оценки
reviewer_1.rate_hw(student_1, 'Java', 1)
reviewer_1.rate_hw(student_1, 'C++', 1)

reviewer_2.rate_hw(student_1, 'Java', 2)
reviewer_2.rate_hw(student_1, 'C++', 2)

# Студент ставит оценки лектору
student_1.rate_lecturer(lecturer_1, 'Java', 5)
student_1.rate_lecturer(lecturer_1, 'C++', 5)

student_2.rate_lecturer(lecturer_1, 'Java', 8)
student_2.rate_lecturer(lecturer_1, 'C++', 2)

student_1.rate_lecturer(lecturer_2, 'Java', 4)
student_1.rate_lecturer(lecturer_2, 'C++', 6)

student_2.rate_lecturer(lecturer_2, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'C++', 7)

print('№ 3.1')
print('Список проверяющих:')
print(reviewer_1)
print()
print(reviewer_2)
print('------------------')
print('Список лекторов:')
print(lecturer_1)
print()
print(lecturer_2)
print('------------------')
print('Список студентов:')
print(student_1)
print()
print(student_2)
print()
print('№ 3.2 - Сравнение средних оценок:')
print(average_course_grade(student_list, 'Java') > average_lecturers_grade(lecturer_list))
print(average_course_grade(student_list, 'C++') < average_lecturers_grade(lecturer_list))
print()
print('№ 4')
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)
print(student_1 < student_2)
print(student_1 > student_2)
