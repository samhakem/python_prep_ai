# Cruising range

import random

fuel = random.randint(1, 50)
kpl = 8  # Km per litre on average
distance_per_litre = 100

trip_computer = distance_per_litre * fuel / kpl

print(f'Your current fuel in litres is {fuel} therefore you have {trip_computer} kms remaining')