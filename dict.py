#emoji converter

message = input(">")
words = message.split(" ")
emojis ={
    ":)" : "😊",
    ":(" : "😒",
    "sunflower": "🌻",
    "dog": "🐶",
    "cat": "😺",
    "cow": "🐮"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)   