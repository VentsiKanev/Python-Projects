import mysql.connector
from Helper import validation_user_type_string
from Helper import validation_user_type_int as validation_int



db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root1337434",
    database="DiaryProgram"
)

mycursor = db.cursor()


#mycursor.execute("CREATE TABLE Person (Person_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(20), last_name VARCHAR(20), diary_entry VARCHAR(500))")


def menu():
     print("1.Enter new diary entry record: ")
     print("2.Check existing diary records: ")
     print("3.Delete existing diary records: ")
     print("4.Exit diary")
     


def diary():
    f_name = (input("Enter your first name: "))
    l_name = (input("Enter your last name: "))
    diary_log = (input("How do you feel today?: "))
    mycursor.execute(Q1, (f_name, l_name, diary_log))
    db.commit()

def get_validated_input(promt, allow_special_chars=False):
    while True:
        user_input = input(promt)
        validated = validation_user_type_string(user_input, allow_special_chars)
        if validated is not None:
            return validated

# def repeat():
#     y = input("Would you like to go back? [yes/no] ")
#     if y == "yes":
#         diary()
#     elif y == "no":
#         print("Entering the main menu")
#         menu()
        
#     else:
#         print("Apologies, however I don't understand your input, please refer to the question.")


Q1 = "INSERT INTO Person (first_name, last_name, diary_entry) VALUES (%s,%s,%s)"
Q2 = "SELECT * FROM Person ORDER BY Person_id DESC"
Q3 = "DELETE FROM Person WHERE Person_id = %s"




while True:
    menu()
   
    try:
        diary_option = int(input("Enter your choice: "))
        if diary_option <= 4 and diary_option >= 1:
           validation_int(diary_option)
           break
        else:
            print("\nPlease enter only numbers between 1 to 4!\n")
    except ValueError:
            print("\nPlease Enter only numbers!\n")
            continue
    




while diary_option != 4:
    if diary_option == 1:
         
        f_name = get_validated_input("Enter your first name: ")
              
        l_name = get_validated_input("Enter your last name: ")
                 
        diary_log = get_validated_input("How do you feel today?: ", allow_special_chars=True)
              
        mycursor.execute(Q1, (f_name, l_name, diary_log))
        db.commit()
        while True:
           y = input("Would you like to make a new diary entry? [yes/no] ").lower()
        
           if y == "yes":
              break
           elif y == "no":
              print("Entering the main menu")
              menu()
              diary_option = int(input("Enter your choice: "))
              break
           else:
              print("Apologies, I don't understand your input.")
              # Ask again instead of breaking
              continue



    elif diary_option == 2:
        print("\n1. Check all existing records")
        print("2. Go back to main menu")
        try:
        
           check_all_entries = int(input("Enter your choice: "))
           valid_user_input = validation_int(check_all_entries)

        except ValueError:
           print("\nPlease enter only numbers!")
           continue
                  
        if valid_user_input == 1:
          while True:
            print("\nAll existing diary records (most recent first):")
            mycursor.execute(Q2)
            for x in mycursor:
                print(x)
            back_button = input("Would you like to go back? [Yes/No]").lower()
            if back_button == "yes":
                break
              
            elif back_button == "no":
                 continue
              
                                   
                   
        elif valid_user_input == 2:
            print("Entering the main menu")
            menu()
            diary_option = int(input("Enter your choice: "))
        
        else:
            print("Please enter 1 or 2")
            continue
            


    elif diary_option == 3:
          print("Delete diary entry record by the ID number ")
          person_id = input("Please enter the ID number of the record: ")
           
          try:
              person_id = int(person_id)
              if person_id > 0:
                 mycursor.execute(Q3, (person_id,))
                 db.commit()
                 print("Diary entry record is deleting... \nDone. \nEntering the main menu... ")
              else:
               print("Enter a valid positive number")
          except ValueError:
               menu()
               diary_option = int(input("Enter your choice: "))
    
        


    elif diary_option == 4:
        exit(0)
    else:
        print("Please enter only numbers between 1 to 4!")
        validation_menu()
      