"""Write a TemperaturConversion program, given the temperature in Celsius as input outputs the temperature in Fahrenheit
Hint => 
Create a celsius variable and take the temperature as user input
Use the Formulae Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F and assign to farenheitResult  and print the result
I/P => celcius
O/P =>  The ____ celsius is _____ fahrenheit

celsius=float(input("Enter celsius"))
fahrenheit=(celsius*9/5)+32
print("the ",celsius,"celsius is ",fahrenheit,"fahrenheit") """\

"""Create a program to find the total income of a person by taking salary and bonus from user
Hint => 
Create a variable named salary and take user input.
Create another variable bonus and take user input.
Compute income by adding salary and bonus and print the result
I/P => salary, bonus
O/P => The salary is INR ___ and bonus is INR ___. Hence Total Income is INR ___

salary=float(input("Enter your salary: "))
bonus=float(input("Enter bonus: "))
income=salary+bonus
print("The salary is ",salary," and bonus ",bonus," total income ",income) """



"""a=int(input("Enter a number "))
b=int(input("Enter another number "))
c=a
d=b
print("Swapped numbers are ",d," and ",c)"""


"""An athlete runs in a triangular park with sides provided as input by the user in meters. If the athlete wants to complete a 5 km run, then how many rounds must the athlete complete
Hint => The perimeter of a triangle is the addition of all sides and rounds is distance/perimeter
I/P => side1, side2, side3
O/P => The total number of rounds the athlete will run is ___ to complete 5 km
"""

"""side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))
distance=5000;
perimeter=side1+side2+side3
rounds=distance/perimeter
print("The total number of rounds the athlete will run is ",rounds," ro complete 5km")"""

students = [("Alice", 85),("Bob", 72),("Charlie", 91),("David", 68),("Eva", 91)]
highest_mark=students[0][1]
lowest_mark=students[0][1]
sum=0
for i in students:
    if i[1] > highest_mark:
        highest_mark=i[1]
    if i[1]<lowest_mark:
        lowest_mark=i[1]
    sum+=i[1]
print("Highest Mark:",highest_mark)
print("Lowest Mark:",lowest_mark)
avg_mark=sum//len(students)
print("Average Mark:",avg_mark)
print("Students who scored more than Avgerage Marks:")
for i in students:
    if i[1]>avg_mark:
        print(i[0])


