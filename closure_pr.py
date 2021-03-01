def outer():
    print('outer')
    def inner():
        print('inner')
    return inner

b=outer()
b()
del outer
b()
b()
b()