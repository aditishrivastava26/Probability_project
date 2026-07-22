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
    
#=============================Event A================================================
#favourable count; 
def get_favourable_A():
    print("=================Event A========================\n")
    favourable_A = user_input("Enter favourable outcomes for event A: ")

    if favourable_A < 0:
        print("Favourable outcomes cannot be negative.\n")
        return get_favourable_A()
    return favourable_A
#total count;
def get_total_A():
    total_A = user_input("enter total outcomes for event A: ")

    if total_A <= 0:
        print("Total outcomes cannot be negative.\n")
        return get_total_A()
    return total_A
#Validation;
def get_validation_A():
    favourable_A = get_favourable_A()
    total_A = get_total_A()

    if favourable_A > total_A:
        print("Favourable outcomes cannot exceed total outcomes.\n")
        return get_validation_A()
    return favourable_A, total_A

#=============================Event B=================================================
#favourable count;
def get_favourable_B():
    print("=================Event B========================\n")
    favourable_B = user_input("Enter favourable outcomes for event B: ")

    if favourable_B < 0:
        print("Favourable outcomes cannot be negative.\n")
        return get_favourable_B()
    return favourable_B
#total count;
def get_total_B():
    total_B = user_input("enter total outcomes for event B: ")

    if total_B <= 0:
        print("Total outcomes cannot be negative.\n")
        return get_total_B()
    return total_B
#validation;
def get_validation_B():
    favourable_B= get_favourable_B()
    total_B = get_total_B()

    if favourable_B > total_B:
        print("Favourable outcomes cannot exceed total outcomes.\n")
        return get_validation_B()
    return favourable_B, total_B

#=============================calculation======================================
#probability of event A;
def calculate_probability_A(favourable_A, total_A):
    probability_A= favourable_A / total_A
    print(f"\nprobability of P(A)= {favourable_A}/{total_A}={probability_A}")
    return probability_A
#probability of event B;
def calculate_probability_B(favourable_B, total_B):
    probability_B= favourable_B / total_B
    print(f"\nprobability of P(B) = {favourable_B}/{total_B}={probability_B}")
    return probability_B
#independent probability;
def calculate_independent(probability_A, probability_B):
    independent = probability_A * probability_B
    print(f"\nindependent probability P(A ∩ B) = {probability_A} * {probability_B} = {independent}")

#================================main============================================
def independent_probability():
    #running the validation;
    favourable_A, total_A = get_validation_A()
    favourable_B, total_B = get_validation_B()
    #running the calculation for probabilities of events;
    probability_A = calculate_probability_A(favourable_A, total_A)
    probability_B = calculate_probability_B(favourable_B, total_B)
    #running the final calculation for probability of independent events;
    independent = calculate_independent(probability_A, probability_B)

#===============================================================================

