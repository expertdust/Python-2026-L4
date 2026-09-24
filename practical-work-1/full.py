# ==========================================
# LAB SESSION 1: PYTHON BASICS
# ==========================================


# ==========================================
# EXERCISE 1
# Calculate the area of a circle
# ==========================================

radius = float(input("Enter circle radius? "))

area = 3.14 * radius ** 2

print("Circle area =", area)


# ==========================================
# EXERCISE 2
# Convert Celsius to Fahrenheit
# ==========================================

celsius = float(input("Enter the temperature in Celsius? "))

fahrenheit = celsius * 9 / 5 + 32

print(celsius, "(C) =", fahrenheit, "(F)")


# ==========================================
# EXERCISE 3
# Check whether a number is prime
# ==========================================

n = int(input("Enter a number? "))

if n <= 1:
    print(n, "is a NOT prime number")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is a NOT prime number")


# ==========================================
# EXERCISE 4
# Check whether a number is perfect
# ==========================================

n = int(input("Enter a number? "))

if n <= 1:
    print(n, "is a NOT perfect number")
else:
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n:
        print(n, "is a perfect number")
    else:
        print(n, "is a NOT perfect number")


# ==========================================
# EXERCISE 5
# Find favorite color
# ==========================================

colors = ["Blue", "Yellow", "Black", "Red", "White"]

favorite_color = input("What is your favorite color? ")

if favorite_color in colors:
    index = colors.index(favorite_color)
    print("Your color is at index", index, "in my list")
else:
    print("Sorry, I could not find your color")


# ==========================================
# EXERCISE 6
# Using range()
# ==========================================

print("range1:")
for i in range(7):
    print(i, end=" ")
print()

print("range2:")
for i in range(1, 11, 3):
    print(i, end=" ")
print()

print("range3:")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

print("range4:")
for i in range(6, -3, -2):
    print(i, end=" ")
print()


# ==========================================
# EXERCISE 7
# Remove dollar sign
# ==========================================

def remove_dollar_sign(s):
    return s.replace("$", "")


print(remove_dollar_sign("$100"))


# ==========================================
# EXERCISE 8
# Extract even numbers
# ==========================================

def extract_even(l):
    even_numbers = []

    for number in l:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


numbers = [1, 4, 5, -1, 10]

print(extract_even(numbers))


# ==========================================
# EXERCISE 9
# Factorial
# ==========================================

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


n = int(input("Enter a non-negative integer? "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(n, "! =", factorial(n))


# ==========================================
# EXERCISE 10
# Get all divisors
# ==========================================

def get_divisors(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors


n = int(input("Enter a number? "))

if n > 0:
    print("Divisors:", get_divisors(n))
else:
    print("Please enter a positive integer")


# ==========================================
# EXERCISE 11
# Distance between two points
# ==========================================

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Distance =", distance)


# ==========================================
# EXERCISE 12
# Print hollow rectangle
# ==========================================

def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()


m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

print_pattern(m, n)
