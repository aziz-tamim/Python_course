thisdic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdic.pop("model")
print(thisdic)


thisdic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdic.popitem()
print(thisdic)


thisdic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdic["model"]
print(thisdic)


thisdic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdic.clear()
print(thisdic)
