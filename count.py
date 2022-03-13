#traditional way.

words = ['an', 'boy', 'girl', 'an', 'boy', 'dog', 'cat', 'Dog', 'CAT', 'an','GIRL', 'AN', 'dog', 'cat', 'cat', 'bag', 'BAG', 'BOY', 'boy', 'an']

#create a generator.
unique_words = {x.lower() for x in set(words)}

for word in unique_words:
    print(f"* Count of {word}: {words.count(word)}")

#OUTPUT
#* Count of cat: 3
#* Count of bag: 1
#* Count of boy: 3
#* Count of dog: 2
#* Count of an: 5
#* Count of girl: 1


#USING THE COLLECTION MODUle

from collections import Counter

word_counter = Counter(x.lower() for x in words)
print("Word Counts:", word_counter)

#output
#Counter({'an': 5, 'boy': 4, 'cat': 4, 'dog': 3, 'girl': 2, 'bag': 2})


# FIND OUT THE MOST COMMON ITEM.

print("Most Frequent:", word_counter.most_common(1))
#Most Frequent: [('an', 5)]

 # Find out the most common 2 items
print("Most Frequent:", word_counter.most_common(2))
#Most Frequent: [('an', 5), ('boy', 4)]
