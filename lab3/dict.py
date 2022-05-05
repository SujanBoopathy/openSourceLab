student={
	'name':'sujan',
	'dept':'IT',
	'regNo':'1918139',
	'CGPA':'8.7',
	'gender':'male'
}

print("The initial dictionary is :")
print(student)
while True:

	print("1.SEARCH  \t 2.MODIFY  \t 3.DELETE")
	choice=int(raw_input("Enter choice:"))
	
	if 	choice == 1:
		search=raw_input("Enter key :")
		if search not in student:
			continue

		print(student[search])

	if choice ==2:
		key1=raw_input("Enter key :")
		if key1 not in student:
			continue
		val1=raw_input("Enter value:")

		student[key1]=val1

		print(student)

	if choice ==3:
		key2=raw_input("Enter key :")
		if key2 not in student:
			continue
		del student[key2]

		print(student)

	exit=raw_input("try again? (y|n):")
	if exit not in ['Y','y']:
		break


