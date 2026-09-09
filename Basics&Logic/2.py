def choose_chocolate(n, m):
    dairy_milk = m * 5
    shots = m * 2
    eclairs = m * 1

    if n >= dairy_milk:
        print("Dairy Milk")
    elif n >= shots:
        print("Shots")
    elif n >= eclairs:
        print("Eclairs")
    else:
        print("No Chocolates")

n=int(input("Enter Amount: "))
m=int(input("enter no of students: "))
choose_chocolate(n,m)