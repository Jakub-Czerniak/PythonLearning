from machine import Pin
import time
import sys

dictionary = {  'A':'.-', 'B':'-...',
			 	'C':'-.-.', 'D':'-..', 'E':'.',
			 	'F':'..-.', 'G':'--.', 'H':'....',
			 	'I':'..', 'J':'.---', 'K':'-.-',
			 	'L':'.-..', 'M':'--', 'N':'-.',
			 	'O':'---', 'P':'.--.', 'Q':'--.-',
			 	'R':'.-.', 'S':'...', 'T':'-',
			 	'U':'..-', 'V':'...-', 'W':'.--',
			 	'X':'-..-', 'Y':'-.--', 'Z':'--..',
				'a':'.-', 'b':'-...',
			 	'c':'-.-.', 'd':'-..', 'e':'.',
			 	'f':'..-.', 'g':'--.', 'h':'....',
			 	'i':'..', 'j':'.---', 'k':'-.-',
			 	'l':'.-..', 'm':'--', 'n':'-.',
			 	'o':'---', 'p':'.--.', 'q':'--.-',
			 	'r':'.-.', 's':'...', 't':'-',
			 	'u':'..-', 'v':'...-', 'w':'.--',
			 	'x':'-..-', 'y':'-.--', 'z':'--..',
			 	'1':'.----', '2':'..---', '3':'...--',
			 	'4':'....-', '5':'.....', '6':'-....',
			 	'7':'--...', '8':'---..', '9':'----.',
			 	'0':'-----', ', ':'--..--', '.':'.-.-.-',
			 	'?':'..--..', '/':'-..-.', '-':'-....-',
			 	'(':'-.--.', ')':'-.--.-'}

led=Pin(2,Pin.OUT)
in_error=False

while(True):
	print("1. Wprowadzenie slowa")
	print("2. Wyjscie")
	try:
		selection=int(input("Wybor: "))
	except:
		print("Not a number")
		selection=99
	if(selection==1):
		temp=input("Podaj zdanie: ")
		words=list(map(str,temp.split(' ')))
		in_error=False
		for word in words:	
			for letter in word:
				try:
					print(dictionary[letter],end=' ')
				except:
					print("Morse code dictionary does not contain used signs.")
					in_error=True
				if(in_error):
					break
				for sign in dictionary[letter]:
					if(sign=='.'):
						led(0)
						time.sleep(0.5)
						led(1)
						time.sleep(1.5)
					elif(sign=='-'):
						led(0)
						time.sleep(1.5)
						led(1)
						time.sleep(1.5)
			if(in_error):
				break
			time.sleep(3.5)
			print('  ',end='')
		print('')
	elif(selection==2):
		sys.exit("All good")
	else:
		print("Brak opcji.")

#space between letters = 3 dots duration
#space between words = 7 dots duration
