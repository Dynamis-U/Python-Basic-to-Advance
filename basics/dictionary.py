capitals = {"USA": "Wastington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan")) #return none

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.popitem()
# capitals.clear()

keys = capitals.keys();

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

# items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

print(capitals)