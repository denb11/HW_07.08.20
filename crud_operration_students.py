# CRUD - creat ,  read,   , delete

students_names    = ["Ion Drop", "Tatiana Hush", "Maria Nush"]  # str values
students_specials = ["IT",           "Filology",   "Filology"]
students_grades   = [ 9.567,              9.667,       8.001 ]       # float values


def read():
    for i in range(len(students_names)):
        print( f" > {students_names[i]:30s} ( {students_specials[i]:10s} )" )

def details():
    name = input(" Which student? > ").lower().title()
    for i in range(len(students_names)):
        if students_names[i] == name:
            print("STUDENT FOUND!")
            print(f" >>> {students_names[i]:30s} ( {students_specials[i]:10s} ) {students_grades[i]:4.1f}")
        else:
            print(" STUDENT NOT FOUND!!!")
        break

def delete():
    name = input(" Which student? > ").lower().title()
    for i in range(len(students_names)):
        if students_names[i] == name:
            print("STUDENT FOUND!")
            students_names.pop(i)
            students_specials.pop(i)
            students_grades.pop(i)
        break

def edit():
    name = input(" Which student? > ").lower().title()
    for i in range(len(students_names)):
        if students_names[i] == name:
            print("STUDENT FOUND!")

            new_name     = input(" ENTER NEW NAME >").lower().title()
            new_specials = input("ENTER NEW SPECIALTY >").lower().title()
            new_grades   = input("ENTER NEW GRADES >")
            if new_name == "":
                students_names[i] = name
            else:
                students_names[i] = new_name

            if new_specials == "":
                new_specials == students_specials[i]
            else:
                students_specials[i] = new_specials
            if new_grades == "":
                students_grades[i]   = students_grades
            else:
                students_grades[i]   = new_grades


def menu():
    option = -1
    while option != 0:
        print("\n\n")
        print( "########## MENU ###########" )
        print( "###########################" )
        print( "1. Show student list" )
        print( "2. Show student details" )
        print( "3. Edit student details" )
        print( "4. Delete student" )
        print( "0. Exit" )
        print( " CHOOSE OPTION  > " )
        option = int(input())


        if option == 1:
            read()
        if option == 2:
            details()
        if option == 3:
            edit()
        if option == 4:
            delete()

menu()
