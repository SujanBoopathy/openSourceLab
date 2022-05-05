list1=[]
list2=[]
list3=[]
list4=[]
size=int(input("Enter size:"))

for i in range(0,size):
	list1.append(input())
	if type(list1[i]) is int:
		list2.append(list1[i])
	if type(list1[i]) is float:
		list3.append(list1[i])
	if type(list1[i]) is str:
		list4.append(list1[i])


print("Base List :\t"),
print(list1)
print("Int List:\t"),
print(list2)
print("Float List :\t"),
print(list3)
print("String List:\t"),
print(list4)
		

