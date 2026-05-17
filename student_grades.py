from data_loader import student_dict, Student
import csv

def print_grades(student_dict, student_id):
    if student_id in student_dict.keys():
        grades = student_dict[student_id].grades
        grades_list = grades.split(",")
        print(f'Оценки студента {student_dict[student_id].full_name}: {grades_list}')
    else:
        print("Студента с таким айди не найдено")

def add_grades(student_dict, student_id, new_grade):
    if student_id in student_dict.keys():
        grades = student_dict[student_id].grades
        grades_list = grades.split(",")
        grades_list.append(str(new_grade))
        student_dict[student_id].grades = ",".join(grades_list)
        print("Оценка успешно добавлена!")
    else:
        print("Студента с таким айди не найдено")
def edit_grades(student_dict, student_id, index, new_grade):
    if student_id in student_dict.keys():
        grades = student_dict[student_id].grades
        grades_list = grades.split(",")
        if index < len(grades_list):
            grades_list[index] = str(new_grade)
            student_dict[student_id].grades = ",".join(grades_list)
            print("Оценка изменeна")
        else:
            print("Индекс за пределами списка оценок")
    else:
        print("Студента с таким айди не найдено")