from collections import Counter,namedtuple,OrderedDict,defaultdict,deque

a_str="aaaaabbbbccc"
my_counter=Counter(a_str)
print(my_counter)
print(my_counter.most_common(1))
print(list(my_counter.elements()))

nums=[1,1,1,2,2,2,3,3,4,4,5,5]
freq=Counter(nums)
print(freq)
print(freq.most_common(1))
print(list(freq.elements()))

Point=namedtuple("Point","x,y")
pt=Point(1,-4)
print(pt.x,pt.y)

student=namedtuple("student",["name","age","city"])
s1=student("Nikhil",20,"guntur")
print(s1)

ordered_d=OrderedDict()
ordered_d['a']=1
ordered_d['b']=2
ordered_d['c']=3
print(ordered_d)
ordered_d.move_to_end("a")
print(ordered_d)

d_int=defaultdict(int)
print(d_int)
d_int['a']=1
print(d_int['b'])

d_list=defaultdict(list)

d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop()
d.popleft()
d.extend([4,5,6])
d.extendleft([7,8])
d.rotate(1)
d.rotate(-2)