def ft_filter(function, iterable):
    """
    Reproduces the built-in filter function
    only main difference is , I choosed to return list instead of iterator
    """
    if function is None:
        return [x for x in iterable if x]
    return [x for x in iterable if function(x)]
