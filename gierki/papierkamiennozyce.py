import random
opcje = ("kamień", "papier", "nożyce")
wynik_komputer = 0
wynik_czlowiek = 0
punkty = 3
ruchy = [[], []]

while True:
  if wynik_czlowiek == punkty or wynik_komputer == punkty:
    break
  wybor_czlowiek = input("\nDostępne opcje: papier, kamień, nożyce\n\nTwój ruch: ")
  if wybor_czlowiek in opcje:
    wybor_komputer = random.choice(opcje)
    ruchy[0].append(wybor_czlowiek)
    ruchy[1].append(wybor_komputer)
    if wybor_czlowiek == wybor_komputer:
      print (f"Ruch komputera: {wybor_komputer}\n")
      print ("Remis!")
    if wybor_czlowiek == "kamień":
      if wybor_komputer == "nożyce":
        print (f"Ruch komputera: {wybor_komputer}\n")
        print("Wygrałeś!")
        wynik_czlowiek += 1
      elif wybor_komputer == "papier":
        print (f"Ruch komputera: {wybor_komputer}\n")
        print("Przegrałeś!")
        wynik_komputer +=1
    elif wybor_czlowiek == "papier": 
      if wybor_komputer == "kamień":
        print (f"Ruch komputera: {wybor_komputer}\n")
        print("Wygrałeś!")
        wynik_czlowiek += 1
      elif wybor_komputer == "nożyce":
        print (f"Ruch komputera: {wybor_komputer}\n")
        print("Przegrałeś!")
        wynik_komputer += 1
    elif wybor_czlowiek == "nożyce": 
      if wybor_komputer == "kamień":
        print (f"Ruch komputera: {wybor_komputer}\n")
        print("Przegrałeś!")
        wynik_komputer += 1
      elif wybor_komputer == "papier":
        print (f"Ruch komputera: {wybor_komputer}\n")
        print("Wygrałeś!")
        wynik_czlowiek +=1
    print(f"Wynik: {wynik_czlowiek} : {wynik_komputer}")
  else:
    print("Wybrałeś złą opcje debilu!")  
for i in ruchy:
  print(', '.join(i))