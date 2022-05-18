from machine import Pin
import time
import sys

led=Pin(2,Pin.OUT)

while(True):
	print("Przekaznik czasowy PCU-520")
	print("1.Tryb AUTO")
	print("2.Tryb MANUAL_BI")
	print("3.Tryb MANUAL_MONO")
	print("4.Wyjdz")
	try:
		selection=int(input("Wybor: "))
	except:
		print("Brak opcji")
		continue
	if(selection==1):
		print("1.Opoznione wylaczenie")
		print("#####______###")
		print(" t1    t2")
		print("2.Opoznione zalaczenie")
		print("_____#####___")
		print(" t1   t2")
		print("3.Opoznione wylaczenie - cykliczne")
		print("###___###___###")
		print("t1 t2  t1 t2 t1 ")
		print("4.Opoznione zalaczenie - cykliczne")
		print("___###___###___")
		print("t1 t2  t1 t2 t1")
		print("")
		try:
			selectionAuto=int(input("Wybor: "))
		except:
			print("Brak opcji")
			continue
		print("Podaj całkowity czas w sekundach")
		try:	
			t1=int(input("t1= "))
			t2=int(input("t2= "))
		except:
			print("Blad danych")
			continue
		if(t1<0 or t2<0):
			print("Czas nie moze byc ujemny")
			continue
		if(selectionAuto==1):
			led(0)
			time.sleep(t1)
			led(1)
			time.sleep(t2)
			led(0)
		if(selectionAuto==2):
			led(1)
			time.sleep(t1)
			led(0)
			time.sleep(t2)
			led(1)
		if(selectionAuto==3):
			while(True):
				led(0)
				time.sleep(t1)
				led(1)
				time.sleep(t2)
		if(selectionAuto==4):
			while(True):
				led(1)
				time.sleep(t1)
				led(0)
				time.sleep(t2)
		else:
			print("Brak opcji")
	if(selection==2):
		print("Man bi")
	if(selection==3):
		print("Man mono")
	if(selection==4):
		sys.exit()