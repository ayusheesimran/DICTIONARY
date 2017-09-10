import json
from difflib import get_close_matches
data=json.load(open("data.json.txt"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        op=input(("Did you mean %s instead? Enter 'y'/'n.'" % get_close_matches(w,data.keys())[0]))
        if op ==("y"or"Y"):
            return translate(get_close_matches(w,data.keys())[0])
        elif op==("n"or"N"):
            return "The word doesn't exist! Please Check Again!"
        else:
            return "Please insert correct option!"
    else:
        return "Word doesn't exist!"
word=input("Input a word:")
output=translate(word)
f=1
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
