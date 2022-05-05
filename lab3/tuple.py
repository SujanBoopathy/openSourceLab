tuple_A=(1,2,3,4,5,6,7,8,9,10)

Even=()
Odd=()

print("The initial tuple is :")
print(tuple_A)

for i in tuple_A:
	Even.insert(i) if i%2==0 else Odd.insert(i)

print("The odd tuples :")
print(tuple(Odd))

print("The even tuples : ")
print(tuple(Even))

