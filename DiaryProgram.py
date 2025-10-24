import mysql.connector
from Helper import validation_user_type_string



db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root1337434",
    database="DiaryProgram"
)

mycursor = db.cursor()


#mycursor.execute("CREATE TABLE Person (Person_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(20), last_name VARCHAR(20), diary_entry VARCHAR(500))")

# f_name = ""
# l_name = ""
# diary_log = ""
# person_id = int
# y = ""
# check_all_entries = int
# back_option = int


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

def get_validated_input(promt):
    while True:
        user_input = input(promt)
        validated = validation_user_type_string(user_input)
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


menu()
diary_option = int(input("Enter your choice: "))



while diary_option != 4:
    if diary_option == 1:
         
        f_name = get_validated_input("Enter your first name: ")
              
        l_name = get_validated_input("Enter your last name: ")
                 
        diary_log = get_validated_input("How do you feel today?: ")
              
        mycursor.execute(Q1, (f_name, l_name, diary_log))
        db.commit()
        
        y = input("Would you like to make a new diary entry? [yes/no] ")
        
        if y == "yes":
            diary_option = 1  # Keep diary_option as 1 to loop again
        elif y == "no":
            print("Entering the main menu")
            menu()
            diary_option = int(input("Enter your choice: "))
        else:
            print("Apologies, I don't understand your input.")
            # Ask again instead of breaking
            continue



    elif diary_option == 2:
        print("\n1. Check all existing records")
        print("2. Go back to main menu")
        check_all_entries = int(input("Enter your choice: "))
    
        if check_all_entries == 1:
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
                
                     
                   
        elif check_all_entries == 2:
            print("Entering the main menu")
            menu()
            diary_option = int(input("Enter your choice: "))
        
        else:
            print("Invalid choice. Returning to main menu.")
            menu()
            diary_option = int(input("Enter your choice: "))


    elif diary_option == 3:
          print("Delete diary entry record by the ID number ")
          person_id = input("Please enter the ID number of the record: ")
          mycursor.execute(Q3, (person_id))
          db.commit()
          print("Diary entry record is deleting... \nDone. \nEntering the main menu... ")
          menu()
          diary_option = int(input("Enter your choice: "))


    else:
       if diary_option == 4:
        exit(0)