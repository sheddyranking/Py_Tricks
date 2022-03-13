# The typical way
score = 90

if score > 90:
    reward = "1000 dollars"
    print(reward)
else:
    reward = "500 dollars"
    print(reward)

# Do this instead
reward = "1000 dollars" if score > 90 else "500 dollars"
print(reward)


# Another possible scenario
# You got a reward amount from somewhere else, but don't know if None/0 or not
reward_known = 0
reward = reward_known or "500 dollars"

# The above line of code is equivalent to below
reward = reward_known if reward_known else "500 dollars"

