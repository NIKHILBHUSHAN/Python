from functools import reduce

add10=lambda x:x+10
mult=lambda x,y:x*y

points2D=[(1,2),(15,1),(5,-1),(10,4)]

sorted_by_y=sorted(points2D,key=lambda x:x[1])
sorted_by_sum=sorted(points2D,key=lambda x:x[0]+x[1])

a=[1,2,3,4,5]
b=list(map(lambda x:x*2,a))
b_comp=[x*2 for x in a]

c=list(filter(lambda x:x%2==0,a))
c_comp=[x for x in a if x%2==0]

prod=reduce(lambda x,y:x*y,a)