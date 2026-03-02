# With using third variable 'temp'
a1 = 10
b1 = 20
temp = a1
a1 = b1
b1 = temp
print ("a1 =",a1)
print ("b1 =",b1)

# Without using third variable
a2 = 10
b2 = 20
a2 = a2 + b2
b2 = a2 - b2
a2 = a2 - b2
print()
print ("a2 =",a2)
print ("b2 =",b2)

# Another method 
a3 = 10
b3 = 20
a3,b3 = b3,a3
print()
print("a3 =",a3)
print("b3 =",b3)
