items = [
    ["Apple", "Banana", "Orange"],
    ["Carrot", "Spinach", "Broccoli"],
    ["Almond", "Peanut", "Walnut"]
]

print(items[0][1]) 
print(items[1][2])
print(items[2][0]) 

print("Iterating over rows:")
for row in items:
    print(row)

print("Iterating over all elements:")
for row in items:
    for item in row:
        print(item, end=" ")
    print()
