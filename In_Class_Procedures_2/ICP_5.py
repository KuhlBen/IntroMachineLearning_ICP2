# Input string
input_string = 'The quick Brow Fox'

# Calculate counts
upper_count = 0
lower_count = 0

for char in input_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

# Print counts
print("No. of Upper-case characters:", upper_count)
print("No. of Lower-case Characters:", lower_count)