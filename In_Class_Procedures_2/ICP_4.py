def unique_list(lst):
    unique_items = []
    for item in lst:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


# Sample list
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

# Get unique items
unique_items = unique_list(sample_list)

# Print unique list
print("Unique List:", unique_items)
