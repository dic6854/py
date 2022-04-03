def print_param2(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

    for key, value in kwargs.items():
        print("%s : %s" % (key, value))

print_param2(first = 'a', second = 'b', third = 'c', fourth = 'd')