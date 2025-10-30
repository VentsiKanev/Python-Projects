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
       