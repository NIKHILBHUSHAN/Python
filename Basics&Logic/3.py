def check_feel_good(n,s):
    count=0
    for i in s:
       if i in "aeiou":
            count+=1
    if count>=n/2 :
        print("Feel Good")
    else:
        print("Feel Bad")

n=int(input("Enter size of string"))
s=input("Enter string: ").strip()
check_feel_good(n,s)