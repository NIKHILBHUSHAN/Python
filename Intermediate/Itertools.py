from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
    count,
    cycle,
    repeat,
    chain,
)
import operator

for i in count(2):
    print(i)
    if i==5:
        break

colors=["red","green"]
c=cycle(colors)
for i in range(7):
    print(next(c))

for i in repeat("hello",3):
    print(i)

prod=product([1,2],[3,4])
print(list(prod))

perm=permutations([1,2,3],2)
print(list(perm))

comb=combinations([1,2,3,4],2)
print(list(comb))
comb_wr=combinations_with_replacement([1,2,3,4],2)
print(list(comb_wr))

nums=[1,2,5,3,4]
acc_sum=accumulate(nums)
print(list(acc_sum))
acc_mul=accumulate(nums,func=operator.mul)
print(list(acc_mul))
acc_max=accumulate(nums,func=max)
print(list(acc_max))
      

def smaller_than_3(x):
    return x<3

data=[1,2,3,4]
group_obj=groupby(data,key=smaller_than_3)

for key,group in group_obj:
    print(key,list(group))

persons=[
    {'name':'Tim','age':25},
    {'name':'Dan','age':25},
    {'name':'Lisa','age':27}
]

for age,group in groupby(persons,key=lambda x:x['age']):
    print(age,list(group))

for i in count(10):
    if i==13:
        break

for i in repeat(1,4):
    print(i)

a=[1,2,3]
b=[5,6,7]
print(list(chain(a,b)))