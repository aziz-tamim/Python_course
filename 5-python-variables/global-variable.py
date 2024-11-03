x = "awesome"
def myfunc():
    print("python is " + x)
myfunc()


x = "awesome"
def myfunction():
    x = "fantastic"
    print("python is " + x)
myfunction()
print("python is " + x)


def thefunc():
    global x
    x = "fantastic"
thefunc()
print("python is " + x)


x = "awesome"
def thisfunc():
    global x
    x = "fantastic"
thisfunc()
print("python is " + x)
