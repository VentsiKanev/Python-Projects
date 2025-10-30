from db_config import db_execute # Execute from db_config.py
from models_classes import Person  # reflected Person table
from Helper import validation_user_type_string as validation_str
from Helper import validate_ID_int as validation_int





def menu():
     print(" ========== Diary Menu =========")
     print("1.Enter new diary entry record: ")
     print("2.Check existing diary records: ")
     print("3.Delete existing diary records: ")
     print("4.Exit diary")


def get_validated_input(promt, allow_special_chars=False):
    while True:
        user_input = input(promt).strip()
        validated = validation_str(user_input, allow_special_chars)
        if validated is not None:
            return validated
        
def main_menu_option():
  while True:
    menu()
    try:
         diary_option = int(input("Enter your choice: "))
         if diary_option <= 4 and diary_option >= 1:
            return diary_option
         else:
             print("\nPlease enter only numbers between 1 to 4!\n")
    except ValueError:
            print("\nPlease enter whole numbers!\n")

           


def add_entry():
    while True:
      print("========= Adding New Person To The Diary Program =========")
      f_name = get_validated_input("Enter your first name: ")
      l_name = get_validated_input("Enter your last name: ")
      d_entry = get_validated_input("How do you feel today?: ", allow_special_chars=True)

    # Add entry to database
      new_person = Person(first_name=f_name, last_name=l_name, diary_entry=d_entry)
      db_execute.add(new_person)
      db_execute.commit()
      print("\nDiary entry added successfully!\n")
      back_button = input("Would you like to go back to the main menu? Yes/no: ").lower().strip()
      if back_button == "yes":
        return
      elif back_button == "no":
        continue
      else:
          print("Please enter only Yes or No! ")

def check_diary_entries():
    while True:
      print("\n--- All Existing Diary Records (most recent first) ---")
      entries = db_execute.query(Person).order_by(Person.person_id.desc()).all()
      if not entries:
          print("No diary records found.")
          return
      for entry in entries:
          print(f"\nID: {entry.person_id}") 
          print(f"Name: {entry.first_name} {entry.last_name}")
          print(f"Entry: {entry.diary_entry}")
      return_button = input("These are all existing records. Would you like to return to the main menu? Yes/No: ").lower().strip()
      if return_button == "yes":
         return
      if return_button == "no":
         continue


def delete_diary_entry():
    while True:
        person_id = input("Enter the ID number of the record to delete: ")
        person_id = validation_int(person_id)

        if not isinstance(person_id, int):
            print(f"Error: {person_id}")
            continue       

        # Fetch entry
        entry = db_execute.query(Person).filter_by(person_id=person_id).first()
        if entry is None:
            print("Nothing found for this ID in the records, please try again.")
            continue

        # Show entry details
        print(f"\n--- Found Entry ---")
        print(f"ID: {entry.person_id}")
        print(f"Name: {entry.first_name} {entry.last_name}")
        print(f"Diary Entry: {entry.diary_entry}\n")

        # Confirm deletion
        delete_entry = input("Would you like to delete this entry record? Yes/No ").lower().strip()
        if delete_entry == "yes":
            db_execute.delete(entry)
            db_execute.commit()
            print("\nDeleting entry record...")

            # Ask if user wants to delete another
            new_entry = input("Would you like to delete another diary entry? Yes/No ").lower().strip()
            if new_entry == "yes":
                continue  # restart outer loop
            else:
                print("Entering the main menu...\n")
                main_menu_option()  # go to menu
                return  # exit this function

        elif delete_entry == "no":
            print("\n--- Entry Not Deleted ---")
            print(f"ID: {entry.person_id}")
            print(f"Name: {entry.first_name} {entry.last_name}")
            print(f"Diary Entry: {entry.diary_entry}\n")

            # Ask if they want to delete another entry
            back_button = input("Would you like to delete a new diary entry? Yes/No ").lower().strip()
            if back_button == "yes":
                continue
            elif back_button == "no":
                print("\nEntering the main menu..\n")
                break  # exit loop
            else:
                print("Invalid input: Please enter only Yes or No!")
                continue

        else:
            print("Invalid input: Please enter only Yes or No!")
            continue

               

            #   
               
            #    if not entry:
            #      print(f"No entry record found with ID: {person_id}")
            #      retry = input("Would you like to try another ID? Yes/No: ").lower().strip()
            #    elif retry == "yes":
            #      continue
            #    elif retry == "no":
            #        print("\nEntering the main menu...\m")
            #        break
            #    else:
            #        print("\nPlease enter Yes or No!\n")
            #        continue
                                  
                    
            #    delete_entry = input("Would you like to delete this entry record? Yes/No ").lower().strip()
            #    if delete_entry == "yes":
            #       db_execute.delete(entry)
            #       db_execute.commit()
            #       print("\nDeleting entry record...")
            #       back_button = input("Would you like to delete new diary entry? Yes/No ").lower().strip()
            #    if back_button == "yes":
            #      break
            #    if back_button == "no":
            #      print("Returning to the main menu...")
            #      menu()

            #    elif delete_entry == "no":
            #       continue
            #    else:
            #       print("Invalid input: Please enter only Yes or No!")
            #       continue

if __name__ == "__main__":
    while True:
        diary_option = main_menu_option()

        if diary_option == 1:
            add_entry()
        elif diary_option == 2:
            check_diary_entries()
        elif diary_option == 3:
            delete_diary_entry()
        elif diary_option == 4:
            print("Exiting diary. Goodbye!")
            db_execute.close()
            break
              
      
               
      
      
    
       
          

            
            
                
        
      



        




     


# def diary():
#     f_name = (input("Enter your first name: "))
#     l_name = (input("Enter your last name: "))
#     diary_log = (input("How do you feel today?: "))
    



  
# diary_option = main_menu_option()


# while diary_option != 4:
#     if diary_option == 1:
         
#         f_name = get_validated_input("Enter your first name: ")
              
#         l_name = get_validated_input("Enter your last name: ")
                 
#         diary_log = get_validated_input("How do you feel today?: ", allow_special_chars=True)
              
#         while True:
#            y = input("Would you like to make a new diary entry? [yes/no] ").lower()
        
#            if y == "yes":
#               break
#            elif y == "no":
#               print("Entering the main menu")
#               menu()
#               diary_option = int(input("Enter your choice: "))
#               break
#            else:
#               print("Apologies, I don't understand your input.")
#               # Ask again instead of breaking
#               continue



#     elif diary_option == 2:
#         print("\n1. Check all existing records")
#         print("2. Go back to main menu")
#         try:
        
#            check_all_entries = int(input("Enter your choice: "))
#            valid_user_input = validation_int(check_all_entries)

#         except ValueError:
#            print("\nPlease enter only numbers!")
#            continue
                  
#         if valid_user_input == 1:
#           while True:
#             print("\nAll existing diary records (most recent first):")
#             mycursor.execute(Q2)
#             for x in mycursor:
#                 print(x)
#             back_button = input("Would you like to go back? [Yes/No]").lower()
#             if back_button == "yes":
#                 break
              
#             elif back_button == "no":
#                  continue
              
                                   
                   
#         elif valid_user_input == 2:
#             print("Entering the main menu")
#             menu()
#             diary_option = int(input("Enter your choice: "))
        
#         else:
#             print("Please enter 1 or 2")
#             continue
            


#     elif diary_option == 3:
#           print("\nDelete diary entry record by the ID number ")
#           person_id = input("Please enter the ID number of the record: ")
           
#           try:
#               person_id = int(person_id)
#               if person_id > 0:
#                  mycursor.execute(Q3, (person_id,))
#                  db.commit()
#                  print("Diary entry record is deleting... \nDone.")
#               else:
#                   print("\nPlease enter a positive number!\n")
#                   continue
                                         
#           except ValueError:
#                print("\nPlease enter only numbers without special characters!\n ")
#                continue
              
         
#           new_entry_ask = get_validated_input("\nWould you like to delete another entry? [Yes/No]: ").lower()
#           if new_entry_ask == "yes":
#              continue
#           elif new_entry_ask == "no":
#             print("Entering the main menu..\n")
#             main_menu_option()
            
    

    
        


#     elif  diary_option == 4:
#         exit(0)
# else:
#     print("Please enter only numbers between 1 to 4!")
#     menu()
    
    
    
        



      