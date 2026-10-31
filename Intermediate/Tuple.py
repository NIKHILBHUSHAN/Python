import sys
import timeit

my_tuple=("Max",28,"Boston")
tuple_no_parens="Max",28,"Boston"

not_a_tuple=("Max")
single_tuple=("Max",)

list_to_tuple=tuple(["a","b","c"])

print(my_tuple[0])
print(my_tuple[-1])

letters=('a','p','p','l','e')
print(len(letters))
print(letters.count('p'))
print(letters.index('l'))

num_tuple=(1,2,3,4,5,6)
sub_tuple=num_tuple[1:4]

name,age,city=my_tuple

tup=(1,2,3,4,5,6)
i1,*i2,i3=tup

my_list=[0,1,2,"hello",True]
my_tup=(0,1,2,"hello",True)

print("List size (bytes):",sys.getsizeof(my_list))
print("Tuple size (bytes):",sys.getsizeof(my_tup))