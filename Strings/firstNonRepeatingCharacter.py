text=input("enter a string:")
isfound=False
for ch in text:
    if text.count(ch)==1 :
        print(ch)
        isfound=True
        break
if(not isfound):
    print("No non repeating characters")
    
        