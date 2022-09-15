from OOPS_LMS import LMS

try:
    test_LMS = LMS("List_of_books.txt", "Python's")

    press_key_list = {
        "D" : "Display Books", "I" : "Issue Books", "A" : "Add Books", "R" : "Return Books", "Q" : "Quit"
        }

    key_press = False

    while not key_press == "q":
        
        print(f"\n----------{test_LMS.library_name} Library Management System----------\n")

        for key, value in press_key_list.items():
            print("Press", key, "to", value)
            
        key_press = input("\nPress key: ").lower()

        if key_press == "d":
            print("\nCurrent selection : Display Books\n")
            test_LMS.display_books()

        elif key_press == "i":
            print("\nCurrent selection : Issue Books\n")
            test_LMS.issue_books()

        elif key_press == "a":
            print("\nCurrent selection : Add Books\n")
            test_LMS.add_books()
        
        elif key_press == "r":
            print("\nCurrent selection : Return Books\n")
            test_LMS.return_books()

        else:
            continue

except Exception as e:
    print("\nSomething went wrong! Please check your input!!!")