my_list = [1, 2, 3, 4, 5]

# Accessing the first element of the list
first_element = my_list[0]

# Accessing the last element of the list
last_element = my_list[-1]

# Accessing a slice of the list
slice_of_list = my_list[1:4]  # Returns [2, 3, 4]

# Changing an element in the list
my_list[2] = 6

# Adding an element to the end of the list
my_list.append(7)

# Inserting an element at a specific index
my_list.insert(2, 8)

# Removing an element from the list
my_list.remove(5)

# Removing the last element from the list
last_element = my_list.pop()

for element in my_list:
    print(element)
    
# Sorting a list in ascending order
my_list.sort()

# Sorting a list in descending order
my_list.sort(reverse=True)
