a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

print("\nThe largest among three number is :")

if(a>b and a>c):
	print(a)
elif(b>a and b>c):
	print(b)
else:
 	print(c)
