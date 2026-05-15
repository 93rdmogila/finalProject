import csv
class Student:
    def __init__(self, student_id,group_name,full_name,course,graduation_year,grades,gpa,tuition_status):
        self.student_id = student_id
        self.group_name = group_name
        self.full_name = full_name
        self.course = course
        self.graduation_year = graduation_year
        self.grades = grades
        self.gpa = gpa
        self.tuition_status = tuition_status

with open("students_fixed.csv", mode = "r", newline="", encoding = "utf-8") as f:
    data_csv = csv.DictReader(f)
    student_dict = dict()
    for i in data_csv:
        object_student = Student(i.get("student_id"), i.get("group_name"), i.get("full_name"), i.get("course"),
                                 i.get("graduation_year"), i.get("grades"), i.get("gpa"), i.get("tuition_status"))
        student_dict[object_student.student_id] = object_student
def add_student(student_dict,group_name,full_name,course,graduation_year,grades = "",gpa = 0.0, tuition_status = "grant"):
    if student_dict:
        new_id = max(int(key) for key in student_dict.keys()) + 1
    else:
        new_id = 1
    
    student_dict[new_id] = Student(new_id,group_name,full_name,course,graduation_year,grades,gpa, tuition_status)
    print("Студент был успешно добавлен")


def print_by_course(student_dict, course1):
    course1 = str(course1)
    dict_by_course = dict()
    for i, j in student_dict.items():
        if course1 == j.course:
            dict_by_course[i] = j
    if dict_by_course:
        for i, j in dict_by_course.items():
            print(j.student_id, " ", j.group_name, " ",  j.full_name, " ",  j.course, " ",
        j.graduation_year, " ", j.grades, " ",  j.gpa, " ", j.tuition_status)
    else:
        print("На этом курсе нет студентов")


def print_by_group(student_dict, group1):
    dict_by_group = dict()
    for i, j, in student_dict.items():
        if group1 == j.group_name:
            dict_by_group[i] = j
    if dict_by_group:
        for i, j in dict_by_group.items():
            print(j.student_id, " ", j.group_name, " ",  j.full_name, " ",  j.course, " ",
        j.graduation_year, " ", j.grades, " ",  j.gpa, " ", j.tuition_status)
    else:
        print("В этой нет студентов")

