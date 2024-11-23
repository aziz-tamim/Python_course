def myfunc():
    x = 300
    print(x)
myfunc()


def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()