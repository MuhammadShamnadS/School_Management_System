import json
import os
from validator import (
    validate_name,
    validate_reg_no,
    validate_age,
    validate_email,
    validate_phone,
    validate_course,
    COURSE_LIST
)

STUDENT_FILE = "data/students.json"

def load_students():
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, 'r') as f:
            return json.load(f)
    return []

def save_students(students):
    with open(STUDENT_FILE, 'w') as f:
        json.dump(students, f, indent=4)

def register_student():
    print("\n--- Register New Student ---")
    
    while True:
        name = input("Name: ")
        if validate_name(name):
            break
        print(" Invalid name. Name must be at least 2 alphabetic characters.")

    while True:
        reg_no = input("Registration Number (REG-YYYY-NNNN): ")
        if validate_reg_no(reg_no):
            break
        print(" Invalid registration number format (example: REG-2024-0001).")

    while True:
        age = input("Age: ")
        if validate_age(age):
            break
        print(" Age must be a number between 18 and 25.")

    while True:
        email = input("Email: ")
        if validate_email(email):
            break
        print(" Invalid email format.")

    while True:
        phone = input("Phone Number (10 digits): ")
        if validate_phone(phone):
            break
        print(" Phone number must be exactly 10 digits.")

    while True:
        course = input(f"Course {COURSE_LIST}: ")
        if validate_course(course):
            break
        print(f" Invalid course. Choose from {COURSE_LIST}.")

    student = {
        "name": name,
        "reg_no": reg_no,
        "age": age,
        "email": email,
        "phone": phone,
        "course": course
    }

    students = load_students()
    students.append(student)
    save_students(students)

    print(" Student registered successfully.")

def list_students():
    students = load_students()
    if not students:
        print("No students registered yet.")
        return

    print("\n--- List of Registered Students ---")
    print(f"{'Name':<15} {'Reg No':<15} {'Age':<5} {'Email':<25} {'Phone':<12} {'Course':<20}")
    print("-" * 95)
    
    for s in students:
        print(f"{s['name']:<15} {s['reg_no']:<15} {s['age']:<5} {s['email']:<25} {s['phone']:<12} {s['course']:<20}")