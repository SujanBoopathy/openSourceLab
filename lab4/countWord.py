sentence = raw_input("Enter a sentence :")

x=sentence.split()
setofWord=set(x)

dictionary={}

for i in setofWord:
	dictionary[i]=x.count(i)

for i in dictionary:
	print(str(i)+"-"+str(dictionary[i]))


