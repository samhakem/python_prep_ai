# Time conversion
# h = hours, m = minutes, s = seconds

duration = 54384
h = duration // 3600  # Hours - compute hours fully contained in duration, no remainder using integer division //

print(h)  # Should be 15

total_minutes = duration // 60

m = total_minutes % 60  # Minutes
s = duration % 60  # Seconds

print(total_minutes)
print(m)

# Validation
print((h * 60 * 60) + (m * 60) + s)
