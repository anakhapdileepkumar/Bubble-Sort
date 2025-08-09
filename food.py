# bubble_sort_foods.py
# Bubble Sort: Sorting favorite foods by length of name

foods = ["Pizza", "Burger", "Ice Cream", "Pasta", "Biryani"]

# Bubble sort algorithm
for i in range(len(foods)):
    for j in range(0, len(foods)-i-1):
        if len(foods[j]) > len(foods[j+1]):  # Compare by name length
            foods[j], foods[j+1] = foods[j+1], foods[j]

print("Foods sorted by name length:", foods)

# One line description:
# Sorted my favorite foods by name length using Bubble Sort.
