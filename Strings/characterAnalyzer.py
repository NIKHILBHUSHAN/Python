text=input("Enter a string")
uppercase=0
lowercase=0
digits=0
spaces=0
specialcharacters=0
for i in text:
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
    else:
        specialcharacters+=1
print("Uppercase:",uppercase)
print("Lowercase:",lowercase)
print("Digits:",digits)
print("Spaces:",spaces)
print("specialcharacters:",specialcharacters)