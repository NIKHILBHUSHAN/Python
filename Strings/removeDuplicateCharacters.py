text=input("Enter a string:")
new_text=""
for ch in text:
    if ch not in new_text:
        new_text+=ch
print(new_text)