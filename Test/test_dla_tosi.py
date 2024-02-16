

def przycinanie(tdp) -> str:
    tdp = tdp.replace("CHIRON","").replace("MR BRUNNER","").lower().replace(".","").replace("'","").replace(",","").replace("!","").replace("?","").replace("-","").replace(" ","").replace("[","").replace("]","").replace("\n","")
    return tdp

def obliczanie_wyniku(dobre,zle) -> None:
    wynik = 100*dobre/(dobre+zle)
    if wynik == 100:
        print("\n//Twój wynik to 100%!//\n")
    elif wynik >= 90:
        print(f"\n//Gratulacje! Osiągnąłeś wynik równy {wynik:0.2f}%. Bardzo dobrze znasz swój tekst!//\n")
    elif wynik >= 60:
        print(f"\n//Twój wynik to {wynik:0.2f}%. To dużo, ale może być lepiej//\n")
    else:
        print(f"\n//Twój wynik to {wynik:0.2f}%, nie przychodź na próbę dopóki nie osiągniesz przynajmniej 60%//\n")



def setup_text() -> list[str]:
    try:
        f = open("tekst_tosi.txt",'r',encoding='utf-8')
    except FileNotFoundError:
        wewe = input("//Nie znaleziono pliku z tekstem.//\n//Zapisz tekst w pliku o nazwie \"tekst.txt\"//")
        quit()
    
    tekst = f.read()
    tekst = tekst.split('[')
    for i in range(len(tekst)):
        tekst[i] = tekst[i].split(']')
    for j in range(len(tekst)):
        convlist = map(str,tekst[j])
        tekst[j] = ''.join(convlist)

    
    f.close()
    return tekst

def main() -> None:
    
    
    tekst = setup_text()
    
    while True:

        dobre = 0
        zle = 0
        
        for j in range(len(tekst)):
            if ("MR BRUNNER" or "CHIRON") in tekst[j]:

                print(f"\n{tekst[j-1]}\n")
                odpowiedz = input("//Wpisz swoją odpowiedz (lub q aby wyjść)// \n\n")
                praw_odp = przycinanie(tekst[j])
                odp = przycinanie(odpowiedz)
                if odp == "q":
                    quit()
                elif praw_odp in odp:
                    print("\n//Dobrze!//\n")
                    aa = input("//Kliknij enter aby przejść dalej lub q aby wyjść//")
                    if aa.lower() == "q":
                        quit()
                    
                    dobre += 1
                else:
                    print("\n//Źle!//\n")
                    print(f"//Twoja odpowiedź// \n{odpowiedz}\n\n//Prawidłowa odpowiedź// \n{tekst[j]}\n")
                    zle += 1
                    aa = input("//Kliknij enter aby przejść dalej lub q aby wyjść//")
                    if aa.lower() == "q":
                        quit()
                    
        obliczanie_wyniku(dobre,zle)
        asd = ""
        while asd == "":
            asd = input("//Jeszcze raz? (T/N)//\n")
            if asd.lower() != "n" and asd.lower() != "t":
                print("//Nieprawidłowy wybór//")
                asd = ""
            elif asd.lower() == "n": 
                quit()

if __name__ == '__main__':
    main()