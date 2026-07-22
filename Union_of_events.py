#================================user input======================================================
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

#===============================total outcomes=========================================
def get_total():
    total = user_input("enter the number of total outcomes: ")
     
    if total <= 0 :
        print("total outcome cannot be negative.\n")
        return get_total()
    return total

#=============================Event A================================================
#favourable count; 
def get_favourable_A():
    print("=================Event A========================\n")
    favourable_A = user_input("Enter favourable outcomes for event A: ")

    if favourable_A < 0:
        print("Favourable outcomes cannot be negative.\n")
        return get_favourable_A()
    return favourable_A

#=============================Event B=================================================
#favourable count;
def get_favourable_B():
    print("=================Event B========================\n")
    favourable_B = user_input("Enter favourable outcomes for event B: ")

    if favourable_B < 0:
        print("Favourable outcomes cannot be negative.\n")
        return get_favourable_B()
    return favourable_B
 
#===============================intersection value=====================================
def get_intersection():
    intersection = user_input("enter outcomes of A ∩ B : ")

    if intersection <= 0 :
        print("intersection outcome cannot be negative.\n")
        return get_intersection()
    return intersection

#==============================validation the user input===============================
#Event A validation;
def get_validation_A(total):
    favourable_A = get_favourable_A()
    
    if favourable_A > total :
        print("Favourable outcomes cannot exceed total outcomes.\n")
        return get_validation_A(total)
    return favourable_A

#Event B validation;
def get_validation_B(total):
    favourable_B = get_favourable_B()

    if favourable_B > total :
        print("Favourable outcomes cannot exceed total outcomes.\n")
        return get_validation_B(total)
    return favourable_B

#intersection validation;
def get_validation(favourable_A, favourable_B):
    intersection = get_intersection()

    if intersection > favourable_A or intersection > favourable_B:
        print("Intersection outcomes cannot exceed favourable outcomes of Event A.\n")
        return get_validation(favourable_A, favourable_B)
    return intersection
#============================calculations========================================
#region calculations
#probability of A;
def get_probability_A(favourable_A, total):
    probability_A= favourable_A / total
    print(f"\nprobability of P(A)= {favourable_A}/{total}={probability_A}")
    return probability_A

#probability of B;
def get_probability_B(favourable_B, total):
    probability_B= favourable_B / total
    print(f"\nprobability of P(B)= {favourable_B}/{total}={probability_B}")
    return probability_B

#intersection probability;
def probability_intersection(intersection, total):
    intersection_prob = intersection/total
    print(f"\nprobability of P(A ∩ B)= {intersection}/{total}={intersection_prob}")
    return intersection_prob

#probability of union of events;
def probability_union_events(probability_A, probability_B, intersection_prob):
    union_events = probability_A + probability_B - intersection_prob
    print(f"\nprobability of P(A U B)= {probability_A}+{probability_B}-{intersection_prob}={union_events}")
    return union_events

#=====================================main================================================================ 
#running the validation;
def uoe_probability():
    
    total = get_total()
    favourable_A= get_validation_A(total)
    favourable_B= get_validation_B(total )
    intersection = get_validation(favourable_A,favourable_B)

    #running the calculation for probabilities of events and intersection;
    probability_A = get_probability_A(favourable_A, total)
    probability_B = get_probability_B(favourable_B, total)
    intersection_prob = probability_intersection(intersection, total)

    #running the final calculation for probability of union of events;
    union_events = probability_union_events(probability_A, probability_B, intersection_prob)

#===========================================================================================================

    
