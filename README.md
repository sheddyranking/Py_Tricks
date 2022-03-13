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


