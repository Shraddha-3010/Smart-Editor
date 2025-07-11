

class StudentManager:

    def __init__(self):

        self.records = []

#saved??

    def add_student(self, name, age, subjects):

        student = Student(name, age, subjects)

        self.records.append(student)

        print("student add:")



    def search_student(self, name):

        for student in self.records:

            if student.name == name:

                return student

z

        else:

            print("Student not found")

            return None





def update_student(name):

    student = search_student(name)

    if student:

        new_age = input("new age")

        student["age"] = new_age

        StudentRecords.update(name)

        print("Student Records updated:")

    else:

        print("student record not found")



def delete_student(name):

    student = search_student(name)

    if student:

        student = search_student(name)

        StudentRecords.remove(student)

        print("student record deleted")

    else:

            print("student record not found")

def main():

    while(True):

        choice = input("Enter 'a' to add, 's' to search, to delete 'd', to update 'u' or Enter 'n' to stop, ")

        if choice.lower() =='n':

            break

        elif choice == 'a':

            name = input("Enter Student Name: ")

            age = input("Enter Student age: ")

            subjects = {}

            for i in range(0, 5):

                sbname = input("Enter Subject Name: ")

                sbmarks = input("Enter Subject Marks: ")

                subjects.update({sbname: sbmarks})

            add_student(name, age, subjects)

        elif choice == 's':

            name = input("Enter Student Name to search: ")

            search_student(name)

        elif choice == 'u':

             name = input("Enter Student Name to update: ")

             update_student(name)

        elif choice == 'd':

             name = input("Enter Student Name to delete: ")

             delete_student(name)

        elif choice == 'n':

            print("no further process:")



















main()



""" print(student["name"])



print(student.get("name"))

new_dict = { "age": (23, 40,30)}

student.update(new_dict)



print(student["age"])

print (list(student.get()))  """





"""

Define a Class

Define A Data System

Define Type of Data Structure 

Define a fuuction to add records

Deifne a function to rem

Define a func to update

Define a function to retrive the record

CRUD

"""

#

#

#Main function to do the operation







