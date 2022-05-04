while True:
	celsius=int (input("Enter the celsius value :"))

	print("Fahrenheit value for "+str(celsius)+" is :"+str(celsius*1.8+32))

	exit = raw_input("Do u want to continue(y|n) :")
	if exit not in ['Y','y']:
		break