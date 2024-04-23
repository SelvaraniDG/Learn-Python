my_string = "Hello, World!"

print("Original String:", my_string)

print("Length of String:", len(my_string))

print("Sliced String (first 5 characters):", my_string[:5])

new_string = my_string + " Welcome"
print("Concatenated String:", new_string)

repeated_string = my_string * 3
print("Repeated String:", repeated_string)

print("Uppercase String:", my_string.upper())
print("Lowercase String:", my_string.lower())

replaced_string = my_string.replace("World", "Python")
print("Replaced String:", replaced_string)

words = my_string.split(", ")
print("Split String:", words)

joined_string = "-".join(words)
print("Joined String:", joined_string)

name = "Alice"
age = 30
formatted_string = f"Hello, my name is {name} and I am {age} years old."
print("Formatted String:", formatted_string)
