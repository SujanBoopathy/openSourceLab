s=raw_input("Enter a string: ")
res=""
list1=[]

for i in range(len(s)):
	if s[i] not in list1:
		list1.append(s[i])
		res+=s[i]
	else:
		res+='$'
print(res)