# List unpacking allows you to assign elements of a list to multiple variables in one line.
# The first few elements can be assigned directly to variables (e.g., first, second).
# Using *other collects all remaining elements into a new list.

numbers = [1, 2, 3, 44, 4, 5, 6, 7]
first, second, *other = numbers
print(first)
print(other)
