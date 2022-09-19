#  Temperature transformation

import random

celsius = random.randint(0, 40)  # Upper/lower bounds can be altered as desired
kelvin = celsius + 275.15
fahrenheit = celsius * 9/5 + 32

print(f'Your temperature was originally {celsius} celsius degrees celsius and is now converted to: {kelvin} degrees Kelvin')
print(f'Your temperature was originally {celsius} degrees celsius and is now converted to: {fahrenheit} degrees '
      f'Fahrenheit.')  # Multiline f string: requires the retyping of the f label with a quote again to continue line