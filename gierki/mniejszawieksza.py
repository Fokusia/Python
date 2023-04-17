import random
print("\nPodaj zakres liczb do wygenerowania przez program.\n")
while True:
  liczba1 = input("Zakres liczb od: ")
  if liczba1.isdigit():
    liczba1 = int(liczba1)
    pass
  else:
    print ("Podany znak nie jest liczbą naturalną!")
  liczba2 = input("Zakres liczb do: ")
  if liczba2.isdigit():
    liczba2 = int(liczba2)
    if liczba1 > liczba2:
      print ("Ej gościu nie możesz tak zrobić, ustaw normalny zakres")
    else:
      answer = random.randint(liczba1, liczba2)
      break
  else:
    print ("Podany znak nie jest liczbą naturalną!")
iloscProb = 0
while True:
  print (f"\nZakres jaki wybrałeś to: {liczba1}-{liczba2}")
  guess = input("Wpisz taką liczbe którą uważasz za wygenerowaną przez program: ")
  if guess.isdigit():
    guess = int(guess)
    if guess == answer:
      print(f"\nGratulacje, odgadłeś wygenerowaną liczbę {answer}!")
      iloscProb += 1
      print(f"Twoja ilość prób: {iloscProb}")
      break
    elif guess not in range(liczba1, liczba2):
      print("\nWyszedłeś poza zakres!")
      iloscProb += 1
    elif guess > answer:
      print ("\nPodana liczba jest większa od liczby wygenerowanej!")
      iloscProb += 1
      continue
    elif guess < answer:
      print ("\nPodana liczba jest mniejsza od liczby wygenerowanej!")
      iloscProb += 1
      continue
  else:
    print ("\nPodaj jakąś liczbe gościu!")