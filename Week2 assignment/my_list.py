#Creating an empty list
my_list = []

print(my_list)

#Appending elements into the empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#Inserting a value 15 at index 1 which is the 2nd position
my_list.insert(1, 15)

print(my_list)

#Extending my list with another list

my_list.extend([50,60,70])

print(my_list)

#Removing the last element from my_list

my_list.pop()

print(my_list)

#Sorting my_list in ascending order

my_list.sort()

print(my_list)

#Finding and printing the index of the value 30 in my_list.

index_of_30 = my_list.index(30)

print("Index of 30:", index_of_30)