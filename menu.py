def show_menu():
    while True:
        print("\n==============================")
        print(" Student Management System")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Statistics")
        print("7. Sort Students")
        print("8. Save Data")
        print("9. Exit")

        choice = input("\nChoose an option: ")

        if choice == "9":
            print("Exiting Student Management System.")
            break
        else:
            print("Feature not added yet.")