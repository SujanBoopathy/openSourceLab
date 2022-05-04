while True:
	

	print("1.ADD \t 2.SUBTRACT \t 3.MULTIPLICATION \t 4.DIVISION ")
	choice = int(input("Enter your choice :"))

	a = int(input("Enter first number : "))
	b = int(input("Enter second number: "))

	if(choice==1):
		print("The result of "+str(a)+ " + "+str(b) +"=" + str(a + b))
	elif(choice==2):
		print("The result of "+str(a)+ " - "+str(b) +"=" + str(a - b))
	elif(choice==3):
		print("The result of "+str(a)+ " * "+str(b )+"=" + str(a * b))
	elif(choice==4):
		print("The result of "+str(a)+ " / "+str(b) +"=" + str(a / b))
	else:
		print("Invalid error")
	
	exit= int(input("Do you want to continue(1|0): "))
	if exit != 1:
		break




	

	

