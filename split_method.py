# List of strings
 # The typical way
columns = ['name', 'age', 'gender', 'address', 'account_type']
print("* Literals:", columns)

# Do this instead
columns = 'name age gender address account_type'.split()
print("* Split with spaces:", columns)

# If the strings contain spaces, you can use commas instead
columns = 'name, age, gender, address, account type'.split(', ')
print("* Split with commas:", columns)


#OUTPUT
#* Literals: ['name', 'age', 'gender', 'address', 'account_type']
#* Split with spaces: ['name', 'age', 'gender', 'address', 'account_type']
#* Split with commas: ['name', 'age', 'gender', 'address', 'account type']