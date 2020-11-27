def logged(func):
    def inside(*args, **kwargs):
        print("you called ", func.__name__, *kwargs, args)
        print("it returned", func(*args))

    return inside


@logged
def some_func(*args):
    return 3 + len(args)


some_func(4, 4, 4)
