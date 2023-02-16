from odoo_web_service import CourseManger


def main():
    cm = CourseManger()
    try:
        print("Perform query on E-learning platform")
        action = input("Enter create or update to perform action: ")
        if action not in ["create", "update"]:
            raise ValueError("Actions are 'create' and 'delete")
        if action == "create":
            payload = dict(
                school_name=input("Enter school name: "),
                level = input("Enter level: "),
                academic_year = input("Enter academic year: "),
                semester = input("Enter semester: "),
                faculty = input("Enter faculty: "),
                department = input("Enter department: "),
                course_title = input("Enter course title: "),
                course_code = input("Enter course code: ")
            )

            _ = cm.create(payload)

        elif action == "update":
            payload = dict(
                id=int(input("Enter record id: ")),
                school_name=input("Enter school name: "),
                level=input("Enter level: "),
                academic_year=input("Enter academic year: "),
                semester=input("Enter semester: "),
                faculty=input("Enter faculty: "),
                department=input("Enter department: "),
                course_title=input("Enter course title: "),
                course_code=input("Enter course code: ")
            )

            _ = cm.update(id=payload.pop("id"), payload=payload)
            return True
    except Exception as e:
        print({"error": f"{e}"})
        return False









