

### Negative Indexing
People like to work with sequences because we know the order of the elements, and we can operate these elements order-wise. In Python, strings, tuples, and lists are the most common sequence data types. We can access individual items using indexing. Like other mainstream programming languages, Python supports 0-based indexing, where we access the first element using zero within a pair of square brackets. Besides, we can also use slice objects to retrieve particular elements of the sequence, as shown in the code examples below.

### Positive Indexing
However, Python takes a step further by supporting negative indexing. Specifically, we can use -1 to refer to the last element in the sequence and count the items backward. For example, the last but one element has an index of -2 and so on. Importantly, the negative indexing can also work with the positive index in the slice object.

### Check Emptiness of Containers
Containers refer to those container data types that can store other data. Some frequently used built-in containers are tuples, lists, dictionaries, and sets. When we deal with these containers, we often need to check if they contain any elements before we perform additional operations. Indeed, we can check the length of these containers, which corresponds to the number of stored items. When the length is zero, the container is empty. The below shows you a trivial example.

However, it’s not the most Pythonic way. Instead, we can simply check the container itself, which will evaluate `True` when it contains elements. Although the following code shows you major container data types, such usage can also apply to strings too (i.e., any non-empty strings are `True`).