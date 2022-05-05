with open('input.txt','r') as f , open ('output.txt','w') as s:
	for line in f:
		s.write(line)
	print("File copied successfully")