# In Python, an iterator is an object that allows you to traverse or loop through collections (such as lists, tuples, or strings) one element at a time. 
# The enumerate() function, which we discussed earlier, is a specific type of iterator. Now, let’s focus on general iterators:

# Purpose: Iterators provide a way to access elements sequentially without needing to know the underlying data structure.
# Usage: To create an iterator, you can use the iter() function on any iterable (e.g., a list).
# The next() method retrieves the next element from the iterator.
# When there are no more elements, next() raises a StopIteration exception.

# Creating an iterator for a list
my_list = [10, 20, 30]
my_iterator = iter(my_list)

# Accessing elements using next()
print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30
