

class Student:

    ## class attributes
    COLLEGENAME = "XYZ Engg College"

    # Constructor
    def __init__(self, name, email):
        # instance attributes
        self.name = name
        self.email = email
        # private attributes
        self.__place = "Chennai"
        print("constructor called")

    # instance methods
    def get_details(self):  #SELF=STUD
        return f'{self.name} -- {self.email}'

    # private method
    def __sample_private_method(self):
        print("Private methods")

    # static method (helper methods)
    @staticmethod
    def call_static_method():
       print("calling static method")

    # class methods
    @classmethod
    def call_class_method(cls):
        print("calling Class method", cls.COLLEGENAME)
        print(cls)

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Student deleted.')


stud = Student("abc", "abc@gmail.com")
print(stud.get_details())
print(stud.COLLEGENAME)
stud.COLLEGENAME = "Arts and science"
print(stud.COLLEGENAME)
#stud.__sample_private_method()
# stud.name = 'xyz'
# print(stud.name)
# print(Student.COLLEGENAME)
#
# # static method
# stud.call_static_method()
# Student.call_static_method()
#
# # class method
# stud.call_class_method()
# Student.call_class_method()
# del stud

stud._Student__sample_private_method()