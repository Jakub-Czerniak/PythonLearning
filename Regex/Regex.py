import re
import sys

while(True):
	txt = input('Podaj zdanie:')
	x = re.sub("\s","_",txt)
	while(True):
		camel = input('Konwersja do camel(y/n):')
		if (camel == 'y'):
			x = txt
			while(True):
				replace = re.search(r"\b[a-z]",x)
				if(replace == None):
					break
				letter = replace.group().upper()
				x = re.sub(r"\b[a-z]",letter,x,1)
			x = re.sub("\s","",x)
		elif (camel != 'n'):
			print('y - dokonaj konwersji, n - nie')
			continue
		break
	print(x)
	while(True):
		newString = input('Nowe zdanie?(y/n):')
		if(newString == 'y'):
			break
		elif(newString == 'n'):
			sys.exit()
		else:
			print('y - wpisz nowe słowo, n - nie')