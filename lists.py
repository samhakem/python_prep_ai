# Loops

# List count
names = ['Franz', 'Hans', 'Herbert', 'Peter']

i = 0
while i < 4:  # Hot to count any list?
    print([i])
    i += 1

# Maximum number
numbers = [1, -10, 20, 11, 19, 0, -5, -1000, 100, 7]

maximum = numbers[0]  # Why 0? Does this put the whole list in here?

for i in numbers:
    if i > maximum:
        maximum = i
print(maximum)

# Prime number checker
# TODO let the user input a number
n = int(input('Prime Number: '))
# TODO Check for a valid input (number has to be larger than 1)

if n <= 1:
    print('Invalid number')
else:
    is_prime_number = True
    for i in range(2, n):
        if n % i == 0:  # therefore n is not a prime number
            is_prime_number = False
# TODO check whether the input is a prime or not

    print(f'Your number {n} is a prime!')
# TODO print the result
if is_prime_number = False:
    print(n, ' Is a prime')
else:
    print(n, 'Is not a prime')
