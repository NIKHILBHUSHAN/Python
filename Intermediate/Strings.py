str1="Hello World"
str2='I\'m a programmer'
multi_line="This is a\nmulti-line string"

char=str1[0]
substring=str1[0:5]
reversed_str=str1[::-1]

s=" Hello World "
s_clean=s.strip()

print(s_clean.upper())
print(s_clean.lower())
print(s_clean.startswith("Hello"))
print(s_clean.endswith("World"))
print(s_clean.find("o"))
print(s_clean.count("l"))

replaced=s_clean.replace("World","Universe")

sentence="how are you doing"
words=sentence.split()
rejoined=" ".join(words)

large_list=["a"]*1000000

fast_string="".join(large_list)

# bad_string=""
# for char in large_list:
#     bad_string+=char

name="Tom"
age=3
val=3.14159265

str_percent="The var is %s, age is %d, float is %.2f"%(name,age,val)

str_format="The var is {}, age is {}, float is {:.2f}".format(name,age,val)

f_string=f"The var is {name}, age is {age}, product is {age*2}, float is {val:.2f}"