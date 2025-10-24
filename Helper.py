def validation_user_type_int(user_input_element):
    if type(user_input_element) not in (int, float):
        return 
    elif user_input_element > 0:
        calc_result = result(user_input_element)
        print(calc_result)
    elif user_input_element == 0:
        print("Cannot be zero")
    elif user_input_element < 0:
        print("Cannot be negative value")

calc_to_hours = 24
calc_to_minutes = 1440

def result(num_of_days):
    return f"{num_of_days} is {num_of_days * calc_to_hours} hours and {num_of_days * calc_to_minutes} minutes"


def validation_user_type_string(user_input_element):
    if not user_input_element.isalpha():  # NEW: Check if only letters
        print("Error: Input must contain only alphabetical letters")
        return 
    elif len(user_input_element) == 0:
        print("Error: String cannot be empty")
        return 
    elif user_input_element.isspace():
        print("Error: String cannot be only whitespace")
        return 
    else:
        print(f"Valid string: {user_input_element}")
        return user_input_element
    
