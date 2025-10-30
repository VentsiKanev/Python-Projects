def validation_user_type_int(user_input_element):
    # Check type
    if not isinstance(user_input_element, (int, float)):
        return "Invalid type"
    
    # Try to convert to integer
    try:
        value = int(user_input_element)
    except (ValueError, TypeError):
        return "Must be a valid number"
    
    # Validate value
    if value < 0:
        return "Cannot be negative value"
    
    if value == 0:
        return  "Cannot be zero"
    
    if value > 4:
        return  "The only acceptable numbers are between 1 to 4"
    
    # Valid (1-4)
    return  value


def validate_ID_int(user_input_ID):
    """Validate any positive integer"""
    try:
        value = int(user_input_ID)
    except (ValueError, TypeError):
        return "Must be a valid number"
    
    if value <= 0:
        return "Must be a positive number"
    
    return value


calc_to_hours = 24
calc_to_minutes = 1440

def result(num_of_days):
    return f"{num_of_days} is {num_of_days * calc_to_hours} hours and {num_of_days * calc_to_minutes} minutes"


def validation_user_type_string(user_input_element, allow_special_chars=False):
    #adding a switch to turn ON (True) and OFF (False) to allow_special_characters
   
    if not allow_special_chars and not user_input_element.isalpha():
        print("Error: Input must contain only alphabetical letters")
        return 
    elif len(user_input_element) == 0:
        print("Error: String cannot be empty")
        return 
    elif user_input_element.isspace():
        print("Error: String cannot be only whitespace")
        return 
    else:
        return user_input_element
    
