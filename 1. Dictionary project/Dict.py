import json
from difflib import get_close_matches

# loads data.json (json file with all dictionary values stored as a dict datatype) file in data variable
data = json.load(open("data.json"))

# Same function with different way of displaying the output
"""
def meaning(w):
    w = w.lower()

    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        print("      The word doesn't match anything")
        for i in get_close_matches(w, data.keys()):               #for loop prints out all similar words
            print("\t",i)

        resp = int(input("      IF the word is one of these enter its serial no:   "))
        #gets the serial no. of the word user wants from the given option

        return data[get_close_matches(w, data.keys())[resp-1]]
        #returns the meaning of that word, user has selected from given options

    else:
        return "No such word exist"
"""
def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        #asks for each similar word individually and takes input Y or N from user
        for i in get_close_matches(w, data.keys()):
            yn = input("Did you mean -->  {}  <-- instead? Enter Y if yes, or N if no:  (CASE-SENSITIVE) \n \t".format(i))
            if yn == "Y":
                return (data[i])
            elif yn == "N":
                continue
            else:
                return "No such word exists"
    else:
        return "No such word exist"


word = input("Enter the Word:  \n \t")
out = meaning(word)

# Prints out in a list format if word has more than 1 meaning
if type(out) == list:
    for b in out:
        print("\n --->",b)
else:
    print("\n --->",out)