import json

data = json.load(open("data.json"))

def translate(word):
    return data[word]

word= input("enter the word:")

print(translate(word))
