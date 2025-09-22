browsing_session = []
browsing_session.append(1)
browsing_session.append(23)
browsing_session.append(88)
print(browsing_session)
last = browsing_session.pop()
print(browsing_session)

print("redirect", browsing_session[-1])

#problem - 1
#Problem: Undo Feature in a Text Editor

Text_Editor = []

def type_word(word):
    Text_Editor.append(word)
    print("Current Text: ", " ".join(Text_Editor))

def undo():
    removed = Text_Editor.pop()
    print(f"Undo last word ({removed}) → Current text:", " ".join(Text_Editor))


type_word("Hello")
undo()
