

def validation_check_only_char(user_input):
    # Check for trailing space — not allowed
    if user_input.endswith(" "):
        return False

    # Split by space
    parts = user_input.split(" ")

    for part in parts:
        # Each part must end with a colon
        if not part.endswith(":"):
            return False

        # The part before the colon must be alphabetic
        word = part[:-1]
        if not word.isalpha():
            return False

    return True

      
     

while True:
   user_input = input("Please enter your input only after each value with space and colon separated e.g (Yes: No: Yes:) ")

   if validation_check_only_char(user_input): 
      print("Valid input")
      
   else:
      print("Invalid input")



   
# def validation_check_words_colons(user_input):
#     # Condition 1: All characters must be letters, spaces, or colons
#     if not all(char.isalpha() and char in " :" for char in user_input):
#         return False

#     # Count colons and spaces
#     colon_count = user_input.count(':')
#     space_count = user_input.count(' ')

#     # Condition 2: Check limits
#     return (1 <= colon_count <= 1) and (1 <= space_count <= 1)


# user_input = ""

# while True:
#     user_input = input("Please enter your input (only colons and spaces allowed, e.g., ': :' ): ")

#     if user_input == "exit":
#         break

#     if validation_check_words_colons(user_input):
#        print("Valid input!")
        
#     else:
#           print("Invalid input. Please try again.")

     


