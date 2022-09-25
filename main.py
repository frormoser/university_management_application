
def mainMenu():
    continuar = True
    while (continuar):
        correctOption = False
        while (not correctOption):
            print("=================================== MAIN MENU ===================================")
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
    print(option)


mainMenu()
