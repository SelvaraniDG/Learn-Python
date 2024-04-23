
shopping_list = []


shopping_list.append("Apples")
shopping_list.append("Bananas")
shopping_list.append("Oranges")

shopping_list.insert(0, "Grapes")
shopping_list.insert(3, "Pineapple")

shopping_list.pop()

shopping_list.remove("Apples")

shopping_list.sort()

shopping_list.reverse()

print("Shopping List:")
for item in shopping_list:
    print(item)
