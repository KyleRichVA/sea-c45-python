def fibonacci(n):
    """
    Returns the nth number from the fibonacci sequence.

    Example: fibonacci(0) == 0
             fibonacci(1) == 1
    """
    # Base values of the sequence, prevents negative number function calls.
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    # Returns the sum of the previous two values in the series.
    return fibonacci(n-1) + fibonacci(n-2)
