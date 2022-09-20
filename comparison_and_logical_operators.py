# Comparison and logical operators
# Comparison operations

# > >= < <= == !=

# ■ These are always binary (“two inputs”) and
# return a boolean value (True or False)
# ■ Be cautious when comparing floating point
# values for equality (or not-equality)

small = 0.00001
big = 10. ** 20
comparison_floats = (big - big + small) == (small + big - big)  # True expected, returns False
print(comparison_floats)

# Define two variables a and b
a = 14
b = 5

greater =  14 > 5 # Greater - True
print(greater)
less = 14 < 5 # Less - False
print(less)
greater_or_equal = 14 >= 5 # Greater or equal - True
print(greater_or_equal)
less_or_equal = 14 <= 5 # Less or equal - False
print(less_or_equal)
equals = 14 == 5 # Equals - False
print(equals)
not_equals = 14 != 5 # Not equals - True
print(not_equals)
