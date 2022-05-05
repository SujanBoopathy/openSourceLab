list1=[]
n=int(input("Enter n :"))
for i in range(0,n):
	list1.append(int(input()))


for i in range(len(list1)):
	for j in range(len(list1)):
		if(list1[i]<list1[j]):
			list1[i],list1[j]=list1[j],list1[i]


print(list1)
