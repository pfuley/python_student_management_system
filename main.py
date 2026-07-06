from menu import show_menu
from file_handler import load_students


def main():
    students = load_students()
    show_menu(students)


if __name__ == "__main__":
    main()
