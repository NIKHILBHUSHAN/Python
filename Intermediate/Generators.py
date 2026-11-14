import sys
def getnumber():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 50
result=getnumber()
print(result)
"""for num in result:
    print(num)"""
print(next(result))
print(next(result))
print(next(result))

nums=(x*x for x in range(1,6))
print(nums)

lst=[x for x in range(1000000)]
gen=(x for x in range(1000000))

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))

def infinitenumber():
    num=1
    while True:
        yield num
        num+=1
gen=infinitenumber()
print(next(gen))
print(next(gen))
print(next(gen))