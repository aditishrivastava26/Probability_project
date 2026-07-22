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
    
#=============================favorable outcome========================================   
def get_favourable():
    favourable = user_input("Enter favourable outcomes: ")

    if favourable < 0:
        print("Favourable outcomes cannot be negative.\n")
        return get_favourable()
    return favourable

#=============================total outcome===========================================
def get_total():
    total = user_input("Enter total outcomes: ")

    if total <= 0:
        print("Total outcomes must be greater than zero.\n")
        return get_total()
    return total

#=============================input validation=========================================
def get_validation():
    favourable = get_favourable()
    total = get_total()

    if favourable > total:
        print("Favourable outcomes cannot exceed total outcomes.\n")
        return get_validation()
    return favourable,total

#=============================calculations==============================================
def calculation(favourable, total):
    probability= favourable / total
    print(f"\nprobability = {favourable}/{total}={probability}")

#=================================main=============================================
def basic_probability():
    favourable, total = get_validation()
    probability = calculation(favourable, total)


