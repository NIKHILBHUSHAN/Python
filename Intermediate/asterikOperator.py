product=5*7
power=2**4

zeros_list=[0]*5
repeated_str="AB"*3

def func(*args,**kwargs):
    pass

def print_three(a,b,c):
    print(a,b,c)

my_list=[1,2,3]
print_three(*my_list)

my_dict={'a':1,'b':2,'c':3}
print_three(**my_dict)

numbers=[1,2,3,4,5,6]
first,*middle,last=numbers
print(first,middle,last)

tuple1=(1,2)
list1=[3,4]
merged_list=[*tuple1,*list1]

dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
merged_dict={**dict1,**dict2}