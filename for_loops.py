# For loops
# No loop condition
# Index variable not needed
# Nothing to increment

for i in range(0,30):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz!')
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

numbers = [1, -10, 20, 11, 19, 0, -5, -1000, 100, 7]

for i in numbers:
    if i > numbers:
        numbers = i
print(i)
