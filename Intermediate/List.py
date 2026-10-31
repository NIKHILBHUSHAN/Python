my_list=["banana","cherry","apple"]
print(my_list)

empty_list=list()

mixed_list=[5,True,"apple","apple"]

print(my_list[0])
print(my_list[-1])

for item in my_list:
    print(item)

if "banana" in my_list:
    print("Yes, banana is in the list")

print(len(my_list))

my_list.append("lemon")
my_list.insert(1,"blueberry")
popped_item=my_list.pop()
my_list.remove("cherry")
my_list.reverse()

numbers=[4,2,3,1,-5,10]
numbers.sort()
new_sorted_list=sorted(numbers)

my_list.clear()

zeros=[0]*5
combined=[1,2,3]+[4,5,6]

a=[1,2,3,4,5,6,7,8,9]
sub_list=a[1:5]
step_list=a[::2]
reversed_a=a[::-1]

original=["banana","cherry","apple"]

copy1=original.copy()
copy2=list(original)
copy3=original[:]

nums=[1,2,3,4,5,6]
squared=[x*x for x in nums]