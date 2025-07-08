from auth import authenticate
from student import register_student, list_students

def main_menu():
    while True:
        print("\n1. Register Student")
        print("2. List Students")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            register_student()
        elif choice == '2':
            list_students()
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    print("Welcome to School Management System")
    if authenticate():
        main_menu()