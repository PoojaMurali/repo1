# # INHERITANCE
#
# # Base class
# class Parent():
#     def __init__(self):
#         print("Parent class __init__ method called")
#     def first(self):
#         print('first function')
#
#     def test_method(self):
#         print(".....Parent test method......")
#
#
#
# # Derived Class
# class Child(Parent):
#     # child's __init__ method overrides Parent class __init__method
#     def __init__(self):
#         print("Child class __init__ method called")
#         #  Parent.__init__(self)
#         super().__init__()   # Super class
#
#     def second(self):
#         print('second function')
#     def test_method(self):
#         print("..........Child test method.........")
#
#
#
# ob = Child()
# ob.first()
# ob.second()
# ob.test_method()



##### Polymorphism ###########

class Bird:
    def intro(self):
        print("There are different types of birds")

    def flight(self):
        print("Most of the birds can fly but some cannot")

class parrot(Bird):
    def flight(self):
        print("Parrots can fly")
    def intro(self):
        print("scns")

class penguin(Bird):
    def flight(self):
        print("Penguins do not fly")


obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()

obj_bird.intro()
obj_bird.flight()

obj_parr.intro()
obj_parr.flight()

obj_peng.intro()
obj_peng.flight()