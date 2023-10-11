#Jordan Giraud
#10/11/23
#USING FUNCTIONS


#create functions

def adding(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

#main function
def main():
    user_choice = 0

    while user_choice != 3:
        print("Welcome to the Main Menu")
        print("------------------------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. End program")

        user_choice = int(input("Enter a choice: "))

        if user_choice == 1:
            num1 = int(input("Enter an interger: "))
            num2 = int(input("Enter another interger: "))
            print(adding(num1, num2))
            user_choice = int(input("Enter a choice: "))
                       
        if user_choice == 2:
            num1 = int(input("Enter an interger: "))
            num2 = int(input("Enter another interger: "))
            print(subtract(num1, num2))
            user_choice = int(input("Enter a choice: "))
                       
        if user_choice == 3:
            print("Goodbye!")
        else:
            print("You entered an invalid choice")


#call the main function - starts the program
main()
