hexa_table={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
new=True
while(True):
    if(new==True):
        try: 
            number=int(input("Podaj liczbę z zakresu 1 do 1024: "))
        except:
            print("Błąd. Zmienna nie jest numerem.")
            quit()

        temp_number=number
        i=0
        new_number=0
        print("1.Przelicz na system dwojkowy")
        print("2.Przelicz na system szesnastkowy")
        print("3.Wyjdź")
        try:
            selection=int(input("Wybór: "))
        except:
            print("Błąd. Wpisana zmienna nie jest numerem.")
            selection=99
    else:
        temp_number=number
    if(selection==1):
        while(temp_number>0):
            remainder=temp_number%2
            temp_number=temp_number//2
            new_number=new_number+remainder*pow(10,i)
            i=i+1
        else:
            print("Liczba ",number, " w systemie dwójkowym wynosi: ",new_number)
            print("Co dalej:")
            print("1.Przelicz inną liczbę")
            print("2.Przelicz na system szesnastkowy")
            print("3.Wyjdź")
            try:
                selection=int(input("Wybór: "))
            except:
                print("Błąd. Wpisana zmienna nie jest numerem")
                selection=99
            if(selection==1):
                new=True
            else:
                new=False

    elif(selection==2):
        hexa=''
        while(temp_number>0):
            remainder=temp_number%16
            temp_number=temp_number//16
            hexa=hexa_table[remainder]+hexa
        else:
            print("Liczba ",number, " w systemie szesnastkowym wynosi: ",hexa)
            print("Co dalej:")
            print("1.Przelicz na system dwójkowy")
            print("2.Przelicz inną liczbę")
            print("3.Wyjdź")
            try:
                selection=int(input("Wybór: "))
            except:
                print("Błąd. Zmienna nie jest numerem.")
                selection=4
            if(selection==2):
                new=True
            else:
                new=False
    elif(selection==3):
        quit()
    else:
        print("Brak opcji. Spróbuj jeszcze raz.")
        new=True