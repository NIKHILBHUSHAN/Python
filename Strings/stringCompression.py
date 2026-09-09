text=input("enter a string:")
result=""
count=1
current=text[0]
print(len(text))
for i in range(1,len(text)):        
     if current==text[i]:
          count+=1
     else:
          result+=current+str(count)
          current=text[i]
          count=1
result+=current+str(count)
print(result)


     