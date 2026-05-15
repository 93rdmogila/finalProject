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