
class Person:
    def __init__(self, name, email, password, current_job):
        self.name = name
        self.email = email
        self.password = password
        self.current_job = current_job


    def change_password(self, new_password):
        self.password = new_password     

    def change_job(self, new_job):
        self.current_job = new_job
    
    def get_person_info(self):
        print(f"\n{self.name} currently works as {self.current_job}. You can contact {self.name} at email: {self.email}\n")


user1 = Person("Ventsi", "vk@mail.bg", "blabla", "jobless")

#get user information
#user1.get_person_info()

#change password
user1.change_job("Technical Support")
user1.get_person_info()