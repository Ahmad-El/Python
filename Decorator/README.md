## Reading and tips
The rule "do not assign directly" may seem confusing, so here is what's behind it: in functional programming all objects, including data structures, are generally immutable.
That means, it is considered a bad practice to modify the data inside a container, the new container with new value should be created instead.
E.g., if you have a list `a = [1, 2, 3]` and you want to increase the second element by five, instead of writing `a[1] += 5` you should create another object: `b = [a[0], a[1] + 5, a[2]]`.
This approach seems weird, but sometimes when dealing with larger codebase it helps a lot to know that your data won't be accidentally modified at any time somewhere deep in your code, as nothing is mutable.

Also, Python has some immutable object types out of the box. e.g. [frozensets](https://docs.python.org/3/library/stdtypes.html#frozenset).

As an additional cool feature, Python has a built-in way of modifying the behaviour of functions without directly modifying their code.
It is called a `decorator` and is just a special syntax for a function that accepts a function as an argument and returns a function. You can read [this article](https://realpython.com/primer-on-python-decorators/) for more details and examples.  