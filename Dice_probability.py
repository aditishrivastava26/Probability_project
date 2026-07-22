#=============================integer input===========================================
def user_input(prompt):
    value = input(prompt).strip().replace(" ", "")
    if not value:   # empty after strip/replace
        print("Input cannot be empty. Please re-enter.")    
        return user_input(prompt)   # recursive call instead of while
    try:
        return int(value)
    except ValueError:
        print("Invalid number. Please enter an integer.")
        return user_input(prompt)  # recursive call instead of while

#==============================yes or no==============================================
def yes_no(prompt):
    choice = input(prompt).strip().lower().replace(" ", "")

    if not choice:
        print("Input cannot be empty.\n")
        return yes_no(prompt)

    if choice not in ["yes", "no"]:
        print("Please enter yes or no.\n")
        return yes_no(prompt)

    return choice
    
#=============================die choice===============================================
def get_number_of_dice():
    print("How many dice would you like to throw?\n")
    print("1.One die")
    print("2.two dice")
    number_die = user_input("enter your answer: ")
    if number_die not in [1, 2]:
        print("plz enter from among the options.")
        return get_number_of_dice()
    return number_die
#============================if one die is thrown=======================================
#menu#
def one_die_menu():
    print("1.specific number")
    print("2.even number")
    print("3.odd number")
    print("4.prime numbers")
    print("5.greater than")
    print("6.less than")
    one_die = user_input("enter your choice:\n")
    if one_die <1 or one_die > 6 :
        print("plz enter from among the options.")
        return one_die_menu()
    return one_die
#1.specific number# 
def specific_number():
    values = input("Enter the required numbers (1-6) separated by spaces: ").strip().split()

    if not values:
        print("Input cannot be empty.\n")
        return specific_number()

    try:
        numbers = [int(value) for value in values]
    except ValueError:
        print("Please enter integers only.\n")
        return specific_number()

    for number in numbers:
        if number < 1 or number > 6:
            print("Please enter numbers between 1 and 6.\n")
            return specific_number()

    if len(numbers) != len(set(numbers)):
        print("Duplicate numbers are not allowed.\n")
        return specific_number()

    return numbers

def calculating_specific_numbers(numbers):
    favourable = len(numbers)
    total = 6
    probability = favourable / total

    print("\n========== Result ==========")
    print(f"Selected numbers    : {numbers}")
    print(f"Favourable outcomes : {favourable}")
    print(f"Total outcomes      : {total}")
    print(f"Probability         : {favourable}/{total} = {probability:.4f}")

#2.even number #
def even_number_calculation():
    favourable2 = 3
    total2 = 6
    probability2 = favourable2/total2

    print("\n========== Result ==========")
    print(f"Favourable outcomes  : {favourable2}")
    print(f"Total outcomes       : {total2}")
    print(f"Probability          : {favourable2}/{total2} = {probability2:.2f}")


#3.odd number#
def odd_number_calculation():
    favourable3 = 3
    total3 = 6
    probability3 = favourable3/total3

    print("\n========== Result ==========")
    print(f"Favourable outcomes  : {favourable3}")
    print(f"Total outcomes       : {total3}")
    print(f"Probability          : {favourable3}/{total3} = {probability3:.2f}")

#4.prime numbers#
def prime_number_calculation():
    favourable4 = 3
    total4 = 6
    probability4 = favourable4/total4

    print("\n========== Result ==========")
    print(f"Favourable outcomes  : {favourable4}")
    print(f"Total outcomes       : {total4}")
    print(f"Probability          : {favourable4}/{total4} = {probability4:.2f}")

#5.greater than a specific number#
def greater_than_number():
    greater_than = user_input("Enter the required number (1-6): ")
    if greater_than  < 1 or greater_than > 6 :#checking the range#
        print("plz choose a number from 1 to 6.\n")
        return greater_than_number()
    return greater_than
def greater_than_calculation(greater_than):
    favourable5 = 6 - greater_than
    total5 = 6
    probability5 = favourable5/total5

    print("\n========== Result ==========")
    print(f"Favourable outcomes : {favourable5}")
    print(f"Total outcomes      : {total5}")
    print(f"Probability         : {favourable5}/{total5} = {probability5:.2f}")
    
#less than a specific number#
def less_than_number():
    less_than = user_input("Enter the required number (1-6): ")
    if less_than  < 1 or less_than > 6 :#checking the range#
        print("plz choose a number from 1 to 6.\n")
        return less_than_number()
    return less_than
def less_than_calculation(less_than):
    favourable6 = less_than - 1
    total6 = 6
    probability6 = favourable6/total6

    print("\n========== Result ==========")
    print(f"Favourable outcomes : {favourable6}")
    print(f"Total outcomes      : {total6}")
    print(f"Probability         : {favourable6}/{total6} = {probability6:.2f}")

#============================if 2 dices are thrown====================================
#menu#
def two_dice_menu():
    print("1.specific sum")
    print("2.even sum")
    print("3.odd sum")
    print("4.prime sum")
    print("5.greater than sum")
    print("6.less than sum")
    print("7.same numbers on both die")
    two_dice = user_input("enter your choice: ")
    if two_dice <1 or two_dice > 7 :
        print("plz enter from among the options.")
        return two_dice_menu()
    return two_dice
# Number of favourable outcomes for each possible sum of two dice
sum_dictionary = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1
}
#1.specific sum #
def specific_sum():
    spec_sum = user_input("Enter the specific sum (2-12): ")

    if spec_sum < 2 or spec_sum > 12:#range check#
        print("Please enter a sum between 2 and 12.\n")
        return specific_sum()

    favourable = sum_dictionary[spec_sum]
    total = 36
    probability = favourable / total

    print("\n========== Result ==========")
    print(f"Required sum        : {spec_sum}")
    print(f"Favourable outcomes : {favourable}")
    print(f"Total outcomes      : {total}")
    print(f"Probability         : {favourable}/{total} = {probability:.4f}")

#2.even sum#
def even_sum():
    favourable = 18
    total = 36
    probability = favourable / total

    print("\n========== Result ==========")
    print(f"Favourable outcomes : {favourable}")
    print(f"Total outcomes      : {total}")
    print(f"Probability         : {favourable}/{total} = {probability:.4f}")

#3.odd sum#
def odd_sum():
    favourable = 18
    total = 36
    probability = favourable / total

    print("\n========== Result ==========")
    print(f"Favourable outcomes : {favourable}")
    print(f"Total outcomes      : {total}")
    print(f"Probability         : {favourable}/{total} = {probability:.4f}")

#4.prime sum#
def prime_sum():
    favourable = (
        sum_dictionary[2]
        + sum_dictionary[3]
        + sum_dictionary[5]
        + sum_dictionary[7]
        + sum_dictionary[11]
    )

    total = 36
    probability = favourable / total

    print("\n========== Result ==========")
    print(f"Favourable outcomes : {favourable}")
    print(f"Total outcomes      : {total}")
    print(f"Probability         : {favourable}/{total} = {probability:.4f}")

#5.greater than a numer#
def greater_than_sum():
    required_sum = user_input("Enter the required sum (2-12): ")

    if required_sum < 2 or required_sum > 12:#range check#
        print("Please enter a sum between 2 and 12.\n")
        return greater_than_sum()

    favourable = 0

    for total_sum, count in sum_dictionary.items():
        if total_sum > required_sum:
            favourable += count

    total = 36
    probability = favourable / total

    print("\n========== Result ==========")
    print(f"Favourable outcomes : {favourable}")
    print(f"Total outcomes      : {total}")
    print(f"Probability         : {favourable}/{total} = {probability:.4f}")

#less than a number#
def less_than_sum():
    required_sum = user_input("Enter the required sum (2-12): ")

    if required_sum < 2 or required_sum > 12:#range check#
        print("Please enter a sum between 2 and 12.\n")
        return less_than_sum()

    favourable = 0

    for total_sum, count in sum_dictionary.items():
        if total_sum < required_sum:
            favourable += count

    total = 36
    probability = favourable / total

    print("\n========== Result ==========")
    print(f"Favourable outcomes : {favourable}")
    print(f"Total outcomes      : {total}")
    print(f"Probability         : {favourable}/{total} = {probability:.4f}")

#same numbers on both dice#
def same_numbers():
    favourable = 6
    total = 36
    probability = favourable / total

    print("\n========== Result ==========")
    print(f"Favourable outcomes : {favourable}")
    print(f"Total outcomes      : {total}")
    print(f"Probability         : {favourable}/{total} = {probability:.4f}")

#======================================main============================================
def dice_probability():

    number_die = get_number_of_dice()

    #====================== ONE DIE ======================

    if number_die == 1:

        choice = one_die_menu()

        if choice == 1:
            numbers = specific_number()
            calculating_specific_numbers(numbers)

        elif choice == 2:
            even_number_calculation()

        elif choice == 3:
            odd_number_calculation()

        elif choice == 4:
            prime_number_calculation()

        elif choice == 5:
            greater_than = greater_than_number()
            greater_than_calculation(greater_than)

        elif choice == 6:
            less_than = less_than_number()
            less_than_calculation(less_than)

    #====================== TWO DICE ======================

    elif number_die == 2:

        choice = two_dice_menu()

        if choice == 1:
            specific_sum()

        elif choice == 2:
            even_sum()

        elif choice == 3:
            odd_sum()

        elif choice == 4:
            prime_sum()

        elif choice == 5:
            greater_than_sum()

        elif choice == 6:
            less_than_sum()

        elif choice == 7:
            same_numbers()

    #====================== REPEAT ======================

    choice = yes_no("\nWould you like to perform another calculation? (yes/no): ")

    if choice == "yes":
        print()
        return dice_probability()      # Recursive call
    else:
        print("\nThank you for using the Dice Probability Calculator!")
        return
if __name__ == "__main__":
    dice_probability()