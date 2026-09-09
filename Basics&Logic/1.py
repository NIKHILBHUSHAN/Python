'''location=int(input("Enter Coordinates:"))
rk=location-1
ru=49-location

if rk<ru:
    print("RKBeach")
elif ru<rk:
    print("RUBeach")
else:
    print("Go Anywhere!")'''

'''def findcloser(x):
    rk=x-1
    ru=49-x
    if rk<ru:
        print("RK Beach")
    elif ru<rk:
        print("RU Beach")
    else:
        print("Go Anywhere!")

location=int(input())
findcloser(location)'''

def find_closer_beach(x):
  rkbeach=1
  rubeach=49
  dist_rk=abs(x-1)
  dist_ru=abs(49-x)
  
  if dist_rk < dist_ru:
    return "RK Beach"
  elif dist_ru < dist_rk:
    return "RU Beach"
  else:
    return "Go anyWhere"
  
x=int(input())
print(find_closer_beach(x))