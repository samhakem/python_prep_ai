# Loops

# ■ It is often the case that we want to repeatedly execute a piece of code
# ■ We might not know how often this is necessary, so one cannot just copy it
# (which would also be bad regarding coding style)
# ■ Loops allow us to do this
# ■ There are two kind of loops in Python: while loops and for loops

while condition:
# do something
for element in list:
# do something

i = 0
while i < 50:
    print(i)
    i = i + 1

# While Loop

# ■ Loop Condition
# ■ Can be arbitrarily complex
# (e.g., compound statements)
# ■ If the condition never holds the loop is not entered
# ■ If the condition is always true the loop is never left

# ■ Loop Body
# ■ Can contain an arbitrary sequence of statements
# (e.g., more loops, if statements, ...)
# ■ Often contains a statement that affects the loop
# condition (e.g., increasing an index)

# ■ The body of the loop will be repeatedly executed
# until the loop condition is not fulfilled anymore

while condition:
statement
statement
statement
...

i = 0
while i < 20:
    print(i)
    i = i + i  # Must increment the temporary variable i or the loop will be infinite

i = 0
while i < 5:
    i = i + 1

i = 0
while i < 5:
    print(i)
    i += 1


# Factorial calcualtor
n = int(input('Enter factorial: '))

i = 1  # All positive integers less than or equal to n
factorial = 1

while i <= n:
    factorial = factorial * i
    i += 1

print(f'{n}! = {factorial}')

# Digit counter
n = int(input('Number: '))

n_digits = 1  # Assign variable
while n >= 10:  # Set
    n = n // 10
    n_digits += 1

# Sum of all numbers
n = int(input('Enter number to sum: '))

digits_sum = 0

while n > 0:
    digits_sum += n % 10
    n //= 10
print('Digit Sum', digits_sum)

# FizzBuzz
# TODO Write a loop that counts from 1 to 30(3o should be included)
i = 1  # Loop index to be incremented

# TODO for each number check for the rules above and print the result (use if, elif, else - module 7)
while i <= 30:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz!')
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# TODO increment loop index

# 3n + 1 / Ulam conjecture
# TODO Let the user input a number
n = int(input('Ulam Number: '))
# TODO While the number is greater than 1 you have to modify the number according to the rules above

while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
# TODO in each iteration should print the number
    print(n)

