a=input("Символ: ")
b=input("Строка: ")
c=''
for i in range(len(b)):
	if b[i] == a:
		c=c+(a*2)
	else:
		c=c+b[i]
print(c)