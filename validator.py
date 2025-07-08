
import re
COURSE_LIST = ["Math", "Physics", "Chemistry", "Biology", "Computer Science"]
def validate_name(name):
    return re.fullmatch(r"[A-Za-z ]{2,}", name) is not None

def validate_reg_no(reg_no):
    return re.fullmatch(r"REG-\d{4}-\d{4}", reg_no) is not None

def validate_age(age):
    if not age.isdigit():
        return False
    age = int(age)
    return 18 <= age <= 25

def validate_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_phone(phone):
    return re.fullmatch(r"\d{10}", phone) is not None

def validate_course(course):
    return course in COURSE_LIST