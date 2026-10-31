my_set={1,2,3,1,2}
set_from_iter=set([1,2,3,4])
set_from_str=set("Hello")

empty_set=set()

my_set.add(4)
my_set.add(5)
my_set.remove(3)
my_set.discard(10)
popped=my_set.pop()
my_set.clear()

odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}

u=odds.union(evens)
i=odds.intersection(primes)

set_a={1,2,3,4,5,6,7,8,9}
set_b={1,2,3,10,11,12}

diff=set_a.difference(set_b)
sym_diff=set_a.symmetric_difference(set_b)

set_a.update(set_b)
set_a.intersection_update(set_b)
set_a.difference_update(set_b)
set_a.symmetric_difference_update(set_b)

set_x={1,2,3,4,5,6}
set_y={1,2,3}

print(set_y.issubset(set_x))
print(set_x.issuperset(set_y))
print(set_x.isdisjoint({7,8}))

a_frozen=frozenset([1,2,3,4])

# a_frozen.add(5)