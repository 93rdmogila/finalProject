from data_loader import student_dict, Student

GPA_PAID = 50.0
GPA_GRANT = 70.0
GPA_SCHOLARSHIP = 90.0


def _parse_grades(grades_str: str) -> list[float]:
    result = []
    for part in grades_str.split(","):
        part = part.strip()
        if part:
            try:
                result.append(float(part))
            except ValueError:
                pass
    return result


def calculate_gpa(student: Student) -> float:
    grades = _parse_grades(student.grades)
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 2)


def get_tuition_status(gpa: float) -> str:
    if gpa >= GPA_SCHOLARSHIP:
        return "повышенная стипендия"
    elif gpa >= GPA_GRANT:
        return "стипендия"
    elif gpa >= GPA_PAID:
        return "грант (без стипендии)"
    else:
        return "платник"


def recalculate_student(student: Student) -> None:
    student.gpa = calculate_gpa(student)
    student.tuition_status = get_tuition_status(student.gpa)


def recalculate_all(student_dict: dict) -> None:
    for student in student_dict.values():
        recalculate_student(student)


def add_grade(student_dict: dict, student_id: str, new_grade: float) -> None:
    if student_id in student_dict:
        grades_list = student_dict[student_id].grades.split(",")
        grades_list.append(str(new_grade))
        student_dict[student_id].grades = ",".join(grades_list)
        recalculate_student(student_dict[student_id])


def edit_grade(student_dict: dict, student_id: str, index: int, new_grade: float) -> None:
    if student_id in student_dict:
        grades_list = student_dict[student_id].grades.split(",")
        if index < len(grades_list):
            grades_list[index] = str(new_grade)
            student_dict[student_id].grades = ",".join(grades_list)
            recalculate_student(student_dict[student_id])


def get_gpa_report(student_dict: dict) -> list[dict]:
    return [
        {
            "id": s.student_id,
            "имя": s.full_name,
            "gpa": calculate_gpa(s),
            "статус": get_tuition_status(calculate_gpa(s)),
        }
        for s in student_dict.values()
    ]


def get_status_groups(student_dict: dict) -> dict[str, list]:
    groups: dict[str, list] = {
        "повышенная стипендия": [],
        "стипендия": [],
        "грант (без стипендии)": [],
        "платник": [],
    }
    for student in student_dict.values():
        gpa = calculate_gpa(student)
        status = get_tuition_status(gpa)
        groups[status].append((student, gpa))
    return groups