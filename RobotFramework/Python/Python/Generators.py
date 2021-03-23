#Generators..

# Normal Function with return statement

# def cube_numbers(nums):
#     cube_list =[]
#     for i in nums:
#         cube_list.append(i**3)
#     return cube_list
#
# cubes = cube_numbers([1, 2, 3, 4, 5])
#
# print(cubes)


# # generator
#
def cube_numbers(nums):
    for i in nums:
        yield(i**3)
        print("Iteration")

cubes = cube_numbers([1, 2, 3, 4, 5])
print(cubes)
#print(next(cubes))
#print(next(cubes))
#print(list(cubes))

for value in cubes:
    print(value)

