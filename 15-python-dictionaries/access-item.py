thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.get("model")
print(x)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "Year": 1964
}
x = thisdict.keys()
print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.values()
print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)
car["color"] = "red"
print(x)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
car["color"] = "red"
print(x)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
