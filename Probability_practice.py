import Conditional_probability
import Basic_probability
import Independent_probability
import Union_of_events
import Dice_probability
# region user input
#function for looping the user input until the input given is valid
def user_input(prompt):
    """
    for input of user rows ad columns    
    """
    value = input(prompt).strip().replace(" ", "")
    if not value:   # empty after strip/replace
        print("Input cannot be empty. Please re-enter.")    
        return user_input(prompt)   # recursive call instead of while
    try:
        return int(value)
    except ValueError:
        print("Invalid number. Please enter an integer.")
        return user_input(prompt)  # recursive call instead of while
    
# region Yes or no 
#function for looping the user input until the user enters yes/no
def yes_no(prompt):
    """
    for input of user for yes/no
    """
    value = input(prompt).strip().lower().replace(" ","")
    if not value: #empty after strip/replace
        print("Input cannot be empty.Please re-enter.")
        return yes_no(prompt) 
    if value in ["yes","no"]:
        return value
    else:
        print("Invalid input. Please enter yes or no.")
        return yes_no(prompt)   # recursive call


def probability_menu():
    print("\nWelcome to Probability Calculator")
    print("Please choose what calculations you would like to perform:")
    print("1. Basic probability")
    print("2. Conditional probability")
    print("3. Independent events")
    print("4. Union of events")
    print("5. Dice probability")

    operation = user_input("Please enter the number of your choice: ")

    print(f"OPERATION: {operation}")

    if operation == 1:
        print("Now performing basic probability\n")
        Basic_probability.basic_probability()

    elif operation == 2:
        print("Now performing conditional probability\n")
        Conditional_probability.conditional_probability()

    elif operation == 3:
        print("Now performing independent probability\n")
        Independent_probability.independent_probability()

    elif operation == 4:
        print("Now performing calculations for union of events\n")
        Union_of_events.uoe_probability()

    elif operation == 5:
        print("Now performing dice probability\n")
        Dice_probability.dice_probability()

    else:
        print("Invalid choice.")
        probability_menu()
        return

    choice = yes_no("\nWould you like to do another calculation? (yes/no): ")
    if choice == "yes":
        probability_menu()
    else:
        print("Thank you for using the Probability Calculator!")


#============================Main Function==================================

def main():
    probability_menu()


#============================Run Program====================================

if __name__ == "__main__":
    main()
 
