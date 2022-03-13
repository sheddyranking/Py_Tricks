# Py_Tricks
Write Better Python Code With These Tricks
### Negative Indexing
People like to work with sequences because we know the order of the elements, and we can operate these elements order-wise. In Python, strings, tuples, and lists are the most common sequence data types. We can access individual items using indexing. Like other mainstream programming languages, Python supports 0-based indexing, where we access the first element using zero within a pair of square brackets. Besides, we can also use slice objects to retrieve particular elements of the sequence, as shown in the code examples below.

### Positive Indexing
However, Python takes a step further by supporting negative indexing. Specifically, we can use -1 to refer to the last element in the sequence and count the items backward. For example, the last but one element has an index of -2 and so on. Importantly, the negative indexing can also work with the positive index in the slice object.

### Check Emptiness of Containers
Containers refer to those container data types that can store other data. Some frequently used built-in containers are tuples, lists, dictionaries, and sets. When we deal with these containers, we often need to check if they contain any elements before we perform additional operations. Indeed, we can check the length of these containers, which corresponds to the number of stored items. When the length is zero, the container is empty. The below shows you a trivial example.

However, it’s not the most Pythonic way. Instead, we can simply check the container itself, which will evaluate `True` when it contains elements. Although the following code shows you major container data types, such usage can also apply to strings too (i.e., any non-empty strings are `True`).

### Create List of Strings With Split()

We often use strings as identifiers for particular objects. For example, we can use strings for the keys in a dictionary. In a data science project, strings are often column names for the data. When we select multiple columns, we’ll inevitably need to create a list of strings. Indeed, we can create strings using literals in a list. However, we’ll have to write pairs of quotes to enclose each of the strings, which is kind of tedious for us “lazyish” people. Thus, I’d prefer to create a list of strings by taking advantage of the string’s `split()` method, as shown in the code snippet below.


###  Ternary Expression

In many use cases, we need to define variables with particular values based on the conditions, and we can simply use the if…else statement to check the condition. However, it requires several lines of code. If we’re only dealing with just the assignment of one variable, we may want to use the ternary expression, which checks the condition and completes the assignment with just one line of code. Besides, it has a shorter form, which makes the code even more concise. Consider the following example.

### With Statement For File Object

We often need to read data from files and write data to files. The most common way is to simply open a file using the built-in open() function, which creates a file object that we can operate. Have you encountered the following problem before?

 we can explicitly call the `close()` method on the file object. However, we can do this using the `“with”` statement, which will close the file object for us automatically, as shown below. When we’re done with the operation with the file, we can verify that the file is closed by accessing the file object’s `closed `attribute.

### Evaluate Multiple Conditions

Oftentimes we need to evaluate multiple conditions. There are several possible scenarios. For numeric values, we can have multiple comparisons for the same variable. In this case, we can chain these comparisons.

In some other scenarios, we can have multiple equality comparisons, and we can take advantage of the following technique using the in keyword for membership testing.

Another technique is the use of the built-in `all()` and `any()` functions for evaluating multiple conditions. Specifically, the `all()` function will evaluate to be `True` when the elements in the iterable are all `True`, and thus this function is suitable to replace a series of `AND` logical comparisons. On the other hand, the `any()` function will evaluate to be `True` when any element in the iterable is `True`, and thus it’s suitable to replace a series of `OR` logical operations. Pertinent examples are shown below.


### Use Default Values in Function Declarations

In almost all Python projects, most of the code involves creating and calling functions. In other words, we continuously deal with function declarations and refactorings. In many scenarios, we need to call a function multiple times. Depending on varied sets of parameters, the function will operate slightly differently. However, sometimes one set of parameters may be often used than others, in which case, we should consider setting default values when we declare the functions.

One thing to note is that if you’re dealing with mutable data types (e.g., lists, sets) when you set the default value, make sure that you use `None` instead of the constructor (e.g., arg_name=[]). Because Python creates the function object where it’s defined, providing the empty list will be “stuck” with the function object. In other words, the function object won’t be created on the fly when you’re calling it. Instead, you’ll be dealing with the same function object, including its initially created default mutable object, in the memory, which may lead to unexpected behavior.


## Use Counter for Element Counting

When we have multiple items in a list, tuple, or string (e.g., multiple characters), we often want to count how many there are for each item. To do that, it’s possible to write some tedious code for this functionality.

we first had to create a set that includes only unique words. We then iterated the word set and used the `count()` method to find out the occurrences of each word. However, there is a better way to do it — using the `Counter` class, which is designed to fulfill this counting task.

The Counter class is available in the `collections`module. To use the class, we simply created a generator:` x.lower() for x in words`, and each of the items will be counted. As you can see, the Counter object is a dict-like mapping object with each key corresponding to the unique item of the word list, while the values are the counts for these items. Pretty concise, right?

Moreover, if you’re interested in finding out the most frequently occurring items of the word list, we can take advantage of the `most_common()` method of the Counter object. The following code shows you this usage. You just need to specify an integer (N), which will find out the most frequent N items from the list. As a side note, the `Counter` object will also work with other sequence data, such as strings and tuples.


### Sorting With Different Order Requirements
Sorting items in a list is a prevalent task in many projects. The most basic sorting is based on the numeric or alphabetic order, and we can use the built-in `sorted()` function. By default, the `sorted()` function will sort the list (actually, it can be any iterable) in the ascending order. If we specify the `reverse` argument to be `True`, we can get the items in the descending order. 

Besides these basic usages, we can specify the `key` argument such that complicated items can be sorted, such as a list of tuples

further more you can uses a trick of negative reverse order to sort combine elements. in this case `sort by name initial ascending, and by grades, descending`
we set the value of grades to `-x[1]`, that is  `lambda x: x[0][0] -x[1]` for the combine.


### defaultdict

Dictionaries are a potent data type that allows us to store data in the form of key-value pairs. It’s required that all the keys are hashable such that under the hood, storing these data can involve the use of a hash table. Such implementation allows an O(1) efficiency for data retrieving and insertion. However, it should be noted that besides the `built-in dict` type, we have alternative dictionaries that we can use. Among them, I’d like to discuss the `defaultdict` type. Unlike the `built-in dict` type, the `defaultdict` allows us to set a default factory function that creates an element when the key doesn’t exist.

Suppose that we’re dealing with words, and we want to group the same characters as a list, and these lists are associated with the characters being the keys. Here’s a naive implementation using the `built-in dict` type. Notably, it’s critical to check if the dict object has the `letter` key, because calling the `append()` method can raise a `KeyError` exception if the key doesn’t exist


