import re

'''word = input('enter a string: ')

found = re.search(r'e',word)

if(found):
    print("found e in",word)
else:
    print("not found e in",word)'''

#To say “any character at all”, you use a dot.

def matchdotChar(pattern, _word):
    for w in _word:
        found = re.search(pattern, w)

        if found:
            print(w, "contains the pattern")
        else:
            print(w, "doesn't contain the pattern")


matchdotChar(r'e.t', ["eat","beast",'best'])
matchdotChar(r'b.t', ['bot','bit','bom','bab','bat'])