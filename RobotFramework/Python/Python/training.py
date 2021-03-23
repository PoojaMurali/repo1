#Decorators

# def my_decorator(func):
#     def inner_func():
#         print("Before function call")
#         func()
#         print("after function call")
#     return inner_func
#
# def say_hello():
#     print("hello")
#
# decorator_function = my_decorator(say_hello)
# print(decorator_function)
# decorator_function()

def upper_case(func):
    def inner_func():
        print("Before inner function call")
        value = func()
        upper = value.upper()
        print("after inner function call")
        return upper
    return inner_func

@upper_case
def say_hello():
    return "hello world"

out = say_hello()
print(out)