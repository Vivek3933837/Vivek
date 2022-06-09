Fruits1 = ("Apple", "Banana", "Cherry")
print(Fruits1)
print(Fruits1[1])
# Adding items in tuple as list
Fruits2=list(Fruits1)
Fruits2.append("Orange")
print(Fruits2)
# Changing values in tuple as list
Fruits2=list(Fruits1)
Fruits2[1]="Kiwi"
Fruits1=tuple(Fruits2)
print(Fruits1)
# Removing item from tuple as list
Fruits2=list(Fruits1)
Fruits2.remove("Cherry")
if "Apple" in Fruits1:
    print("Yes, Apple is in fruit tuple")
for x in Fruits1:
    print(x)
