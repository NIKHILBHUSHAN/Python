#valid variables
name = "Beau"
age = 39
name_1 = "Quincy"
_count = 10
MAX_LIMIT = 100

#Expressions 
1 + 1
"Beau"

#Statements 
name = "Beau"
print(name)

#Multiple statements separated by semicolons
name = "Beau"; print(name)

#Single line comment
name = "Beau"  #Inline comment
age = 20

#Data types
# Type inspection
print(type(name))                
print(isinstance(name,str))     
print(isinstance(age,int))      

# Type conversion (Casting)
age_str="20"
age_int =int(age_str)          
float_val=float(2)             
string_val=str(39)             

print(isinstance(age_int,int))