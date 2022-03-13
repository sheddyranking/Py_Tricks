 # A list of numbers and strings
numbers = [1, 3, 7, 2, 5, 4]
words = ['yay', 'bill', 'zen', 'del']

# Sort them
print(sorted(numbers))
print(sorted(words))
 
#output
#[1, 2, 3, 4, 5, 7]
#['bill', 'del', 'yay', 'zen']

# Sort them in descending order
print(sorted(numbers, reverse=True))
print(sorted(words, reverse=True))

#ouput
#[7, 5, 4, 3, 2, 1]
#['zen', 'yay', 'del', 'bill']



#SORTING COMPLICATED ITEMS

# Create a list of tuples
grades = [('John', 95), ('Aaron', 99), ('Zack', 97), ('Don', 92), ('Jennifer', 100), ('Abby', 94), ('Zoe', 99), ('Dee', 93)]

# 1.Sort by the grades, descending
sorted(grades, key=lambda x: x[1], reverse=True)

#ouput
#[('Jennifer', 100), ('Aaron', 99), ('Zoe', 99), ('Zack', 97), ('John', 95), #('Abby', 94), ('Dee', 93), ('Don', 92)]

# 2.Sort by the name's initial letter, ascending
sorted(grades, key=lambda x: x[0][0])

#output
#[('Aaron', 99), ('Abby', 94), ('Don', 92), ('Dee', 93), ('John', 95), ('Jennifer', 100), ('Zack', 97), ('Zoe', 99)]


# Requirement: sort by name initial ascending, and by grades, descending
sorted(grades, key=lambda x: (x[0][0], -x[1]))

#output
#[('Aaron', 99), ('Abby', 94), ('Dee', 93), ('Don', 92), ('Jennifer', 100), ('John', 95), ('Zoe', 99), ('Zack', 97)]

