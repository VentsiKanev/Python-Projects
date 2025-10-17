calc_to_hours = 24
calc_to_minutes = 1440


def result(num_of_days):
    return f"{num_of_days} is {num_of_days * calc_to_hours} hours and {num_of_days * calc_to_minutes} minutes"


def validation_user_type(user_input_element):
    if type(user_input_element) not in (int, float):
        return
    elif user_input_element > 0:
        calc_result = result(user_input_element)
        print(calc_result)
    elif user_input_element == 0:
        print("Cannot be zero")
    elif user_input_element < 0:
        print("Cannot be negative value")


user_input = int()

while user_input != "exit":
    user_input = input(
        "Please enter your numbers to be calculated separeted by commas: "
    )
    if " " in user_input and ":" not in user_input:
        print("Please add two dots : after each number (e.g., 1: 2: 3)")

    else:
        for user_input_element in user_input.split(":"):
            try:
                num = int(user_input_element)
                validation_user_type(num)

            except ValueError:
                print("Please enter a valid number")

    if user_input == "exit":
        print("exiting the program..")
        break
