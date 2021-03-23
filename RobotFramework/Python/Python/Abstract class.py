############### Abstract classs ############


from abc import ABC, abstractmethod

# abstract class
class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print("Some implementation!")
        pass

# subclass
class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        print("The enrichment from AnotherSubclass")


#obj = AbstractClassExample()  # can't able to create object for Abstract class

x = AnotherSubclass()
x.do_something()