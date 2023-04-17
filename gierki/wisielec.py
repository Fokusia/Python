import string, random

def get_random_word():
    words = []
    with open('slowa.txt', encoding="UTF8") as of:
        lines = of.readlines()
        for line in lines:
            line = line.split('\n')[0]
            words.append(line)
    words = tuple(words)
    return random.choice(words)

def wisielec():
    def form():
        print(f"Slowo do odgadnięcia: {(' '.join(pusto)).upper()}")
        print(f"Lista użytych liter: {', '.join(lista_liter)}")
        print(f"Ilość prób: {proba}")
    pusto = "_"*len(slowo)
    proba = 11
    print(f"\nSlowo do odgadnięcia: {(' '.join(pusto))}\n")
    while "_" in pusto:
        if proba > 0:
            guess = input("Zgadnij litere: ").lower()[0]
            if guess in lista_znakow:
                if guess not in lista_liter:
                    if guess in slowo:
                        print(f"\n:) Zgadłeś literę: {guess.upper()}")
                        lista_liter.append(guess)
                        for i in range(len(slowo)):
                            if guess in slowo[i]:
                                pusto = pusto[:i] + guess + pusto[i+1:]
                            if "_" not in pusto:
                                print(f"Gratulacje! Odgadłeś słowo: {slowo.upper()}")
                                quit()
                        form()
                    else:
                        print(f"\n:( Nie zgadłeś litery: {guess.upper()}")
                        lista_liter.append(guess)
                        proba -= 1
                        form()
                else:
                    print(f"\n:( Litera: {guess.upper()} została już przez ciebie odgadnięta!")
                    form()
            else:
                print(f"\n:( Litery: {guess.upper()} nie ma w bazie!")
                form()
        else:
            print("\n:( Ilość twoich prób dobiegła końca, przegrałeś!")
            print(f":( Szukanym słowem było słowo {slowo.upper()}\n")
            break
            
lista_liter = []
lista_znakow = ["ę", "ó", "ą", "ś", "ł", "ż", "ź", "ć", "ń"]
for i in string.ascii_lowercase:
    lista_znakow.append(i)
print("\n=-=-=-=-=-= WITAJ W WISIELCU =-=-=-=-=-= \nGra polega na odgadnięciu słowa zgadując litera po literce!\nNa odgadnięcie słowa masz 11 prób!\n\nMasz do wyboru 2 opcje gry:\nOpcja 1: Słowo wybiera jedna osoba, druga zgaduje.\nOpcja 2: Słowo jest losowo wybierane z listy.\n")
wybor = input("Wybieram opcje: ")
if wybor == "1":
    slowo = (input("\nWprowadź słowo do odgadnięcia przez 2 osobę: ")).lower()
    for i in slowo:
        if i not in lista_znakow:
            print(":( Słowo musi składać się z samych liter!\n")
            quit()
    for i in range(0,101):
        print(" ")
    wisielec()
elif wybor == "2":
    slowo = get_random_word()
    wisielec()
else:
    print(":( Nie ma takiej opcji!\n")