i = 1
while i != 5:
    print(i)
    i += 1

i = 1
while i < 10:
    print(i)
    i += 2

# a=1  b=2  c=3  ->  maximum=3
# a=1  b=3  c=2  ->  maximum=3
# a=1  b=1  c=3  ->  maximum=3
# a=1  b=1  c=1  ->  maximum=1

a = 10

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if (a >= b and a >= c):
    maximum = a

if (b >= a and b >= c):
    maximum = b

if (c >= a and c >= b):
    maximum = c

print('Maximum:', maximum)
