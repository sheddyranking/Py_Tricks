#creating the dict from scratch

letters = ["a", "a", "c", "d", "d", "c", "a", "b"]

final_dict = {}

for letter in letters:
    if letter not in final_dict:
        final_dict[letter] = []
    final_dict[letter].append(letter)

print("Final Dict:", final_dict)

#output
#Final Dict: {'a': ['a', 'a', 'a'], 'c': ['c', 'c'], 'd': ['d', 'd'], 'b': ['b']}


#USING THE FINAL DICT.

from collections import defaultdict


final_defaultdict = defaultdict(list)

for letter in letters:
    final_defaultdict[letter].append(letter)
print("Final Default Dict:", final_defaultdict)

#Final Default Dict: defaultdict(<class 'list'>, {'a': ['a', 'a', 'a'], 'c': ['c', 'c'], 'd': ['d', 'd'], 'b': ['b']})

