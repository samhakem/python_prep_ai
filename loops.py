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
