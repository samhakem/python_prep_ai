# Advanced operators

# Estimate cost exercise

# l = float(input('Please input wall length:\n'))
# w = float(input('Please input wall width:\n'))
# h = float(input('Please input wall height:\n'))
# n_doors = input('How many doors do you have?:\n')
# n_windows = input('How many windows do you have?\n')

l = 10.5
w = 20
h = 2.8
door_size = 2
n_doors = 1
window_size = 1.5
n_windows = 2

wall_area = (l + w) * h * 2
ceiling_area = l * w

# door_width = 91.44
# door_height = 203.2
# door_area = door_width * door_height
#
# window_width = 60.96
# window_height = 121.92
# window_area = window_width * window_height

# wall_area_calc = wall_area - door_size * float(n_doors) - window_size * float(n_windows)
wall_area -= (door_size * n_doors + window_size * n_windows)

cost = wall_area * 4.99 + ceiling_area * 5.49
print(cost)
