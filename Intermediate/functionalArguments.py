def print_name(name):
    print(name)
print_name("Alex")

def foo(a,b,c,d=4):
    print(a,b,c,d)
foo(1,2,3)
foo(a=1,c=3,b=2)
foo(1,b=2,c=3)

def var_args(a,b,*args,**kwargs):
    print("Positional:",a,b)
    print("*args (tuple):",args)
    print("**kwargs (dict):",kwargs)
var_args(1,2,3,4,5,six=6,seven=7)

def keyword_only(a,b,*,c,d):
    print(a,b,c,d)
keyword_only(1,2,c=3,d=4)

number=0
def modify_global():
    global number
    number=5

modify_global()
def mutate_list(a_list):
    a_list.append(4)

def rebind_list(a_list):
    a_list=[100,200]