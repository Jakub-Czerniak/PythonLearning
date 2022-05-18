import network
import socket
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

ssid='AcessPoint57'
password='12345678'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid,password=password)

while ap.active() == False:
	pass
print('Polaczono')
apconfig=ap.ifconfig()
print('Konfiguracja ' + apconfig[0])

s=socket.socket()
s.bind((apconfig[0],23))
s.listen(0)
conn,addr=s.accept()
print('Polaczono z adresu: ' + addr[0])
conn.recv(512)

while(True):
	print("1. Wprowadzenie slowa")
	print("2. Wyjscie")
	try:
		selection=int(input("Wybor: "))
	except:
		print("Not a number")
		selection=99
	if(selection==1):
		text=conn.recv(512)
		text1=conn.recv(512)		
		temp=str(text,'utf-8')
		print(temp)
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
		conn.close()
		sys.exit("All good")
	else:
		print("Brak opcji.")

