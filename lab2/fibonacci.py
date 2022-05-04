n=int(input("Enter n value :"))

a=0
b=1

for i in range(n):
	if(i==0):
		print(a)
		continue
	if(i==1):
		print(b)
		continue

	c=a+b
	a=b
	b=c

	print(c)