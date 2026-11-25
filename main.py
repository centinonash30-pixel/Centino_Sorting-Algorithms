
# Assessment 3.7: Sorting Algorithms
# Name: NASH CENTINO
# Sorting Method: Bubble Sort

name = "NASH CENTINO"

# Create an empty array
unsorted_array = []

# Remove duplicate letters and spaces
for letter in name.upper():
    if letter.isalpha() and letter not in unsorted_array:
        unsorted_array.append(letter)

# Display Unsorted Array
print("UNSORTED ARRAY:")
print(unsorted_array)

# Copy array for sorting
sorted_array = unsorted_array.copy()

# Bubble Sort
n = len(sorted_array)

for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_array[j] > sorted_array[j + 1]:
            sorted_array[j], sorted_array[j + 1] = (
                sorted_array[j + 1],
                sorted_array[j]
            )

# Display Sorted Array
print("\nSORTED ARRAY:")
print(sorted_array)
    