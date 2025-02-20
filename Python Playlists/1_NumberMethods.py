# abs() used to return the abs value of the number
print(abs(-7.25))
print(abs(7.25))

# all() used to return True if all items in an iterable are true  
# or if the iterable is empty
mylist = [True, True, True]
print(all(mylist))
mylist = [True, False, True]

# math.ceil() used to return the smallest integer greater than or equal to a number
import math
print(math.ceil(1.4))
print(math.ceil(-1.6))

# math.floor() used to return the largest integer less than or equal to a number
print(math.floor(1.4))
print(math.floor(-1.6))

# math.exp() used to return the value of e raised to the power of a number
print(math.exp(1))
print(math.exp(5))

# math.fabs() used to return the absolute value of a number
print(math.fabs(-7.25))
print(math.fabs(7.25))

# math.log() used to return the natural logarithm of a number
print(math.log(1))
print(math.log(100))
print(math.log(10,10))
print(math.log10(100))

# max() used to return the largest number in an iterable
print(max(5, 10, 25))
print(max([5, 10, 25]))

# min() used to return the smallest number in an iterable
print(min(5, 10, 25))
print(min([5, 10, 25]))

# math.pow() used to return the value of x to the power of y
print(math.pow(4, 3))
print(math.pow(2, 3))

# sqrt() used to return the square root of a number
print(math.sqrt(64))
print(math.sqrt(81))

# trignometic functions
print(math.sin(90))
print(math.cos(0))
print(math.tan(45))
print(math.asin(1))
print(math.acos(1))
print(math.atan(1))
print(math.degrees(1.57))
print(math.radians(90))

# math.hypot() used to return the Euclidean norm
print(math.hypot(3, 4))
print(math.hypot(5, 12))

# math.modf() used to return the fractional and integer parts of a number
print(math.modf(1.25))
print(math.modf(5.0))

