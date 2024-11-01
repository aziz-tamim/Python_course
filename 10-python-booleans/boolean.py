print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
    def __len__(self):
        return 0
myobject = myclass() 
print(bool(myobject))

def myFunction():
    return True
print(myFunction())


def myFunction():
    return True
if myFunction():
    print("YES!")
else:
    print("No!")
    
x = 200
print(isinstance(x, int))