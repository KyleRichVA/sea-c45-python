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


def lucas(n):
    """
    returns the nth number from the lucas numbers series
    """
    # Base values of the series
    if (n == 0):
        return 2
    if (n== 1):
        return 1

    # returns the sum of the previous two values in the series.
    return lucas(n-1) + lucas(n-2) 