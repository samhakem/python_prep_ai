# Max four values
a = float(input('Value a: '))
b = float(input('Value b: '))
c = float(input('Value c: '))
d = float(input('Value d: '))

if a > b:
    maximum = a
elif b > a:
    maximum = b
else:
    maximum = c
if d > c:
    maximum = d

print('Maximum: ', maximum)

# Leap Year
# Iteration 1
year = int(input('Enter Year: '))

if year % 4 == 0 and year % 400 != 0 or year % 400 == 0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year')

# Iteration 2
if year % 4 != 0:
    print(f'{year} is not a leap year.')
elif year % 400 == 0:
    print(f'{year} is a leap year.')
elif year % 100 == 0:
    print(f'{year} is not a leap year.')
else:
    print(f'{year} is a leap year.')
