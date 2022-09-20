# Variables and Operators
# A variable is a placeholder with
# a certain name, type and value.

# Examples
name0 = 'Franz'
age = 20
shoe_size = 3.5
is_clever = True
diff = age - 18

# Convention: Variable names should be short,
# descriptive and in lower letters. Multiple words
# should be separated by an _ underscore.
# See PEP8 naming conventions

# To remember for now:

# ■ Variable names are only allowed
# to contain alphanumeric
# characters and underscores.

# ■ The first character must not
# be a number!

# ■ There are some reserved
# keywords that can’t be used
# (e.g. if, for, while, return, ...)

# Every variable has a type

# ■ bool: True, False
# ■ int: -45, 0, 58, 0x3A
# ■ float: -0.3, 0.0, 3.1415
# ■ str: 'abc', "car"
# ■ list: [1, 'abc', var_name],

# [[1, 2, 3], [4, 5, 6]]
# ■ dict: {'name': 'Christian', 'age': 33},
# {'Author': 'George R. R. Martin', 'Books': ['The Game of Thrones', 'Winds of Winter']}

# Comments

# ■ Comments are explanation or
# annotation for your code
# ■ Comments will not be executed

# Look at doc strings and PEP8 guidelines

# Compute the sum
# of two numbers.
compute = 10+5 # Add 10 and 5
# 15
add_five_ignore_comment = 10+5#+5
# 15

# ■ Code should be self-explainable. There is no need to comment every line of code.
# ■ Only comment complex stuff or assumption you took.
# ■ Good code needs fewer comments!

# Arithmetic Operators

# ■ Arithmetic operations
# + - * / % // **
# ■ Most of them are binary operators (“two inputs”)
# ■ The integer division just cuts of the decimals
# ■ The modulo operation returns the remainder of an integer division

addition = 14 + 5 # Addition
# 19
subtraction = 14 - 5 # Subtraction
# 9
product = 14 * 5 # Multiplication
# 70
division = 14 / 5 # Division
# 2.8
integer_division = 14 // 5 # Integer division - calculates absolute number of dividends no remainder
# 2
modulo = 14 % 5 # Modulo
# 4
exponent = 2**3 # Raised to a power n
# 8
unary_minus = -14 # Unary minus - less than zero assignment
# -14
concatenation = 'Hello' + ' ' + 'World'
# 'Hello World'
string_multiplication = 'Ah' * 3
# 'AhAhAh'
