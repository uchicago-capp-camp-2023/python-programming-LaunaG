# python-programming-lab-exercises

### Instructions

Complete each function in `practice.py` so it returns the expected value. You'll need to replace the comment ```#YOUR LOGIC HERE``` and the keyword `pass` with your own logic. As an example, given the following function:

```python
def example_function_sum(a, b):
    """Given two integers, computes their sum.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        (int): The sum of a and b.
    """
    # YOUR LOGIC HERE
    pass
```

You would update the code with your logic and return the correct value using the `return` keyword:

```python
def example_function_sum(a, b):
    """Given two integers, computes their sum.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        (int): The sum of a and b.
    """
    return a + b
```

You can use manual testing with IPython as well as automated tests to determine if your functions have any errors.

To run all of the automated tests at once, enter the command `pytest tests` in the terminal. If you'd only like to run tests for one function, run `pytest -k` followed by the name of the corresponding test file, such as `pytest -k test_fizzbuzz.py`. You can also pass in a keyword, and `pytest` will run all tests whose file name or function name matches that keyword. For example, the previous command could be run as `pytest -k fizz` instead. If you'd like `pytest` to stop running tests upon encountering the first error, you can add the flag `-x` to the command, as in `pytest -xk test_fizzbuzz.py` or `pytest -xk fizz`.

After you have finished the cycle of writing and testing your code, check your style by running a linter configured specifically for this assignment: `pylint practice.py`. You will receive a score ranging from 0 to 10 indicating how much your code matches expected syntax and style conventions. Finally, if all looks good, you can submit your assignment to GradeScope, as detailed in the lab instructions.
