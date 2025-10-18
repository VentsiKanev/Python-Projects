calc_to_hours = 24
calc_to_minutes = 1440

def result(num_of_days):
    return f"{num_of_days} is {num_of_days * calc_to_hours} hours and {num_of_days * calc_to_minutes} minutes"

def validation_user_type(user_input_element):
    if user_input_element > 0:
        calc_result = result(user_input_element)
        print(calc_result)
    elif user_input_element == 0:
        print("Cannot be zero")
    else:
        print("Cannot be negative value")
        
user_input = ""

while user_input != "exit":
    user_input = input("Please enter numbers separated by colons (or 'exit' to quit): ")
    
    if user_input == "exit":
        print("Exiting the program..")
        break
    elif user_input.isspace():
        print("Program does not accepts empty space") 
              
    elif ":" not in user_input:
        print("Please add colons : after each number (e.g., 1:2:3)")

    elif not user_input.replace(":", "").strip():
        print("Program does not accept empty spaces with colon")
                
    else:
       for user_input_element in user_input.split(":"):
           user_input_element = user_input_element.strip()
           if not user_input_element:
              continue
             
           try:
                    num = int(user_input_element)
                    validation_user_type(num)
           except ValueError:
                    print(f"Please enter a valid number")

    

