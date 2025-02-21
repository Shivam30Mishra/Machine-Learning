# set 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(type(set1))

set1.remove(5)
set1.add(6)
print(set1)

# checking ordered collection in set
set3 = set({6,5,4,3,2,1})
set4 = set({"Avengers","Hulk","Tron","Ironman","Hulk"})
set4.add("Zor")
print("Type of set4 is ",type(set4))
print(set3)
print(set4)

set5 = {10, 20, 30, 5, 1, 3, 7, 8, 25, 15, 50, 40}
print(set5)

set6 = set([7,5464,345,332,8976,2546,246532,65432,345,643])
print(set6)

my_dict = {"name"="Max", "age"=28, "city"="New York"}
my_dict = dict(name="Max", age=28, city="New York")
dict1 = {"name":"Anna", "age":25, "city":"New York"}
print(dict1)
print(my_dict)