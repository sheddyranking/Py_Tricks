# Multiple Comparisons


# The typical way
if a < 4 and a > 1:
    # do something here

# Do this instead
if 1 < a < 4:
    # do somerthing here


#ANOTHER SCENARIO

# The typical way
if b == "Mon" or b == "Wed" or b == "Fri" or b == "Sun":
    # do something here

# Do this instead, you can also specify a tuple ("Mon", "Wed", "Fri", "Sun")
if b in "Mon Wed Fri Sun".split():
    # do something here


#ANOTHER SCENARIO

# The typical ways
if a < 10 and b > 5 and c == 4:
    # do something
    
if a < 10 or b > 5 or c == 4:
    # do something


## using all() and any() to solve the AND and OR logical operators problem.

# Do these instead
if all([a < 10, b > 5, c == 4]):
    # do something

if any([a < 10, b > 5, c == 4]):
    # do something
