text=input("Enter a string: ")

left=0
right=0
substring=""
size=0

while right<len(text):
    if text[right] not in substring:
        substring += text[right]
        if len(substring) > size:
            size=len(substring)
        right += 1
    else:
        substring=substring[1:]
        left += 1
print(size)