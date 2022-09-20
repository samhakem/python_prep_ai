# Logical Operators

# and or not
# These operations require boolean operands
# (true or False) and return a boolean value

# | a b and or |
# |------------|
# | T T  T  T  |
# | T F  F  T  |
# | F T  F  T  |
# | F F  F  F  |

# | a not |
# |-------|
# | T  F  |
# | F  T  |

a = True
b = not a # Negation
print(b)  # Should return False

_and = a and b  # Should return False
_and_not = a and not b  # Should return True
_or = a or b  # Should return True
_not_or = not a or b  # Should return False

# Combining several operators
# ■ Logical operations can be combined in many ways.
# Consider the following expression:
combination = ((a and b) or (b or not c) and (a or c))

# The full expression looks quite complicated,
# but, we can easily split it up into its three parts:
# ■ (a and b)
# ■ (b or not c)
# ■ (a or c)

