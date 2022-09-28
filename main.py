from BD.connection import DAO
import functions


def mainMenu():
    continuar = True
    while (continuar):
        correctOption = False
        while (not correctOption):
            print(
                "=================================== MAIN MENU ===================================")
            print("1.- List Courses")
            print("2.- Register Course")
            print("3.- Update Course")
            print("4.- Delete Course")
            print("5.- Exit")
            print("===================================")
            option = int(input("Select an option: "))

            if option < 1 or option > 5:
                print("Unregistered option, select an option again...")
            elif option == 5:
                continuar = False
                print("Thank you for using this system.")
                break
            else:
                correctOption = True
                runOption(option)


def runOption(option):
    dao = DAO()

    if option == 1:
        try: 
            courses = dao.listCourses()
            if len(courses) > 0:
                functions.listCourses(courses)
            else:
                print("No courses found...")
        except:
            print("an error occurred...")
    elif option == 2:
        print("Register")
    elif option == 3:
        print("Update")
    elif option == 4:
        print("Delete")
    else:
        print("Invalid option")


mainMenu()
