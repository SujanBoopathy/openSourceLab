class AgeError(Exception):
	pass

while True:
	try:
		age=int(input("Enter age:"))
		if(age>=100 or age<=18):
			raise (AgeError())
		else:
			print("you are eligible for voting")
	except AgeError as error:
		print("Error! you are not eligible")
	exit=raw_input("TRY AGAIN? (y/n) :")
	if exit not in ['y','Y']:
		break

