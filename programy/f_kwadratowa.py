import math
def funkcja_kwadratowa():
  while True:
    try:
      print("\nPogram do obliczania funkcji kwadratowej:")
      A = float(input("Podaj współczynnik A: "))
      B = float(input("Podaj współczynnik B: "))
      C = float(input("Podaj współczynnik C: "))
      print ("\nPostać funkcji wygląda następująco:")
      print ("ax² + bx + c = 0")
      delta = (B**2)-(4*A*C)
      if delta > 0:
        x1 = (-B-math.sqrt(delta))/(2*A)
        x2 = (-B+math.sqrt(delta))/(2*A)
        print (f"\nWynik delty: {delta}\nZatem wynik delty jest dodatni, co znaczy że mamy 2 miejsca zerowe:\nx₁ = {round(x1, 2)}\nx₂ = {round(x2, 2)}")
      elif delta == 0:
        x0 = (-B)/(2*A)
        print (f"\nWynik delty: {delta}\nZatem wynik delty wynosi zero, co znaczy że mamy 1 miejsce zerowe:\nx₁ = {round(x0, 2)}")
      elif delta < 0:
        print (f"\nWynik delty: {delta}\nZatem wynik delty jest ujemny, co znaczy że nie mamy miejsc zerowych")
      break
    except ValueError:
      print ("Musisz podać liczbe!")
try: funkcja_kwadratowa()
except KeyboardInterrupt: print('\nZamknieto przez uzytkownika!')