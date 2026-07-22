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

#===============================intersection value================================================
def get_intersection():
    intersection = user_input("enter outcomes of A ∩ B : ")

    if intersection <= 0 :
        print("intersection outcome cannot be negative.\n")
        return get_intersection()
    return intersection

#===============================event B value=====================================================
def get_event_B():
    event_B = user_input("enter outcomes of event B : ")

    if event_B < 0:
        print("event B outcome cannot be nagative.\n")
        return get_event_B()
    return event_B

#==============================validating the user input==========================================
def get_validation():
    print(f"=========================================")
    intersection = get_intersection()
    event_B = get_event_B()

    if intersection > event_B:
        print("outcome of intersection cannot be greater than outcome of event B.\n") 
        return get_validation()
    return intersection, event_B

#==============================calculations=======================================================
def calculation(intersection, event_B):
    probability = intersection / event_B
    print(f"\nprobability = {intersection}/{event_B}={probability}")

#================================main=============================================================
def conditional_probability():
    intersection, event_B = get_validation()
    calculation(intersection, event_B)