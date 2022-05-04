stack=[]

while True:


	print("choose the operation to implement :")
	print("\t1.push \n\t2.pop \n\t3.peek")
	choice = int(input("Enter your choice : "))

	
	
	if(choice==1):
		a=int(input("Enter the element to be pushed: "))
		stack.append(a)
	elif(choice==2):
		stack.pop()
	elif(choice==3):
		print("Top of stack :"+str(stack[len(stack)-1]))
	else:
		print("Invalid choice")

	exit=raw_input("Do you want to continue(y/n):")
	if exit not in ['Y','y']:
		break