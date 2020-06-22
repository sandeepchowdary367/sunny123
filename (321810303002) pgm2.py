a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
all=a==b and b== c and c==a
print("All are equal:",all)
any=a==b or b == c or c== a
print("Any of three are equal:",any)