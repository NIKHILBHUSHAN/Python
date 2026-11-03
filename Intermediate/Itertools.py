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
)
import operator

prod=product([1,2],[3,4])

perm=permutations([1,2,3],2)

comb=combinations([1,2,3,4],2)
comb_wr=combinations_with_replacement([1,2,3,4],2)

nums=[1,2,5,3,4]
acc_sum=accumulate(nums)
acc_mul=accumulate(nums,func=operator.mul)
acc_max=accumulate(nums,func=max)

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
    pass