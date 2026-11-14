from functools import reduce

add10=lambda x:x+10
mult=lambda x,y:x*y

points2D=[(1,2),(15,1),(5,-1),(10,4)]

sorted_by_y=sorted(points2D,key=lambda x:x[1])
print(sorted_by_y)
sorted_by_sum=sorted(points2D,key=lambda x:x[0]+x[1])
print(sorted_by_sum)

a=[1,2,3,4,5]
b=list(map(lambda x:x*2,a))
b_comp=[x*2 for x in a]
print(b)
print(b_comp)

c=list(filter(lambda x:x%2==0,a))
c_comp=[x for x in a if x%2==0]
print(c)
print(c_comp)

prod=reduce(lambda x,y:x*y,a)
print(prod)

nums=[2,4,6,8,10]
result=map(lambda x:x*3,nums)
print(list(result))

nums=[12,5,17,8,21,4,30,9]
f=filter(lambda x:x>10,nums)
result=map(lambda x:x*x,f)
print(list(result))

nums=[2,3,4,5,6]
result=reduce(lambda x,y:x*y,nums)
print(result)