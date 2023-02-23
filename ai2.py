import turtle
import random

# Definiujemy funkcję do generowania kształtów
def generuj_ksztalt():
    turtle.clear() # Wyczyszczamy poprzedni kształt
    turtle.color(random.choice(kolory))
    turtle.begin_fill() # Wypełniamy kształt kolorem
    
    # Losujemy parametry kształtu
    rozmiar_ksztaltu = random.randint(25, 50)
    liczba_bokow = random.randint(4, 20)
    kat = 360 / liczba_bokow
    krzywizna = random.uniform(1, 50)
    
    # Rysujemy kształt
    turtle.right(random.uniform(0, 360))
    for j in range(liczba_bokow):
        turtle.forward(rozmiar_ksztaltu)
        turtle.right(kat + krzywizna)
        krzywizna *= -1
    
    turtle.end_fill() # Kończymy wypełnianie kształtu kolorem

# Konfigurujemy żółwia
turtle.speed('fastest')
turtle.pensize(2)
turtle.colormode(255)

# Definiujemy kolory
kolory = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Generujemy początkowy kształt
generuj_ksztalt()

# Podpinamy funkcję do zdarzenia wciśnięcia klawisza "q"
turtle.listen()
turtle.onkey(generuj_ksztalt, 'q')

# Zamykamy okno po wciśnięciu klawisza "Escape"
turtle.onkey(turtle.bye, 'Escape')
turtle.mainloop()
