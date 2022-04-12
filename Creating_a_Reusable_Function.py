#Creating a Reusable Function
def Emoji_convert(message):
    words = message.split(' ')
    emojis = {
        ":)" : "😊",
        ":(" : "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
message = input(">")
result = Emoji_convert(message)
print(result)