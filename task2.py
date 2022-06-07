# a
print("\nTask A:")

a = ["I", "like", "cookiees"]
b = a

b[-1] = "apples"
print("a:", a)
print("b:", b)

#####################################################

# b
print("\nTask B:")

a = ["I", "like", "cookiees"]
b = a[:]

b[-1] = "apples"
print("a:", a)
print("b:", b)

#####################################################

# c
print("\nTask C:")

a = ["I", "like", ["chocolate", "cookies"]]
b = a[:]
b[-1][-1] = "apples"

print("a:", a)
print("b:", b)

#####################################################

# d
print("\nTask D:")

from copy import deepcopy

a = ["I", "like", ["chocolate", "cookiees"]]
b = deepcopy(a)

b[-1][-1] = "apples"

print("a:", a)
print("b:", b)

#####################################################

# e
print("\nTask E:")

n = int(input("Enter a number: "))

result_dict = {x: x**2 for x in range(n)}
print(result_dict)

#####################################################

# f
print("\nTask F:")

keys_of_dict = [x for x in result_dict]
print(keys_of_dict)
