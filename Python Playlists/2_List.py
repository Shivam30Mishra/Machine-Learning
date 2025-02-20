# mutable vs immutable
# mutable: list, dict, set
# immutable: int, float, str, tuple
# list: []
# tuple: ()
# dict: {}
# set: {}
# list: ordered, changeable, duplicates allowed
# tuple: ordered, unchangeable, duplicates allowed
# dict: unordered, changeable, indexed, no duplicates
# set: unordered, unindexed, no duplicates

# mutable meaning that you can change the value of the item in that data type
# immutable meaning that you can't change the value of the item in that data type

# string
str1 = "Hello"
print(str1)
print(type(str1))
# str1[0] = "h" # error : str object does not support item assignment
print(str1)

# list
lst = ["Hello", "World"]
print(lst)
print(type(lst))
lst[0] = "hello"
print(lst)

lst.append("Python")
print(lst)

lst.insert(1, "Java")
print(lst)

lst.remove("Java")
print(lst)

lst.pop()
print(lst)

lst.pop(1)
print(lst)

lst.clear()
print(lst)