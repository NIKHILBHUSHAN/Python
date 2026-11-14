my_set={1,2,3,1,2}
set_from_iter=set([1,2,3,4])
set_from_str=set("Hello")

empty_set=set()
print(my_set)
print(set_from_iter)
print(set_from_str)

my_set.add(4)
my_set.add(5)
my_set.remove(3)
my_set.discard(10)
print(my_set)
popped=my_set.pop()
my_set.clear()
print(my_set)
odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}

u=odds.union(evens)
print("Union:",u)
i=odds.intersection(primes)
print("Intersection:",i)

set_a={1,2,3,4,5,6,7,8,9}
set_b={1,2,3,10,11,12}

diff=set_a.difference(set_b)
print("difference:",diff)
sym_diff=set_a.symmetric_difference(set_b)
print("Symmetric Differnence:",sym_diff)

set_a.update(set_b)
print(set_a)
set_a.intersection_update(set_b)
print(set_a)
set_a.difference_update(set_b)
print(set_a)
set_a.symmetric_difference_update(set_b)
print(set_a)

set_x={1,2,3,4,5,6}
set_y={1,2,3}

print(set_y.issubset(set_x))
print(set_x.issuperset(set_y))
print(set_x.isdisjoint({7,8}))

a_frozen=frozenset([1,2,3,4])
print(a_frozen)
#a_frozen.add(5)