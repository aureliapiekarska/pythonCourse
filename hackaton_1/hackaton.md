# python2022
hackaton 1
Gra wisielec

*Opis gry
Gra, w ktorej zadaniem jest odgadniecie przez gracza ukrytego przez nas hasla.
Zmienna przez nas uzyta ma zostac wyswietlona jako nieznane litery, a nastepnie informujemy uzytkownika ile ma mozliwosci odgadniecie hasla.
Po kazdej podanej literze program pokazuje czy uzytkownik odgadl litere.
Jesli minie okreslona liczba rund i uzytkownik nieodgadnie hasla, nastepuje koniec gry.
Jesli uzytkownik odgadnie haslo wygrywa gre.

*Koncepcja rozwiazania
Wybieram hasło.
Oznaczam użyte litery
Witam gracza i informuje go o ilości prób.
Tworzę pętle while o warunku, w którym liczba prób jest większa niż 0.
Liczniki jest równy 0.
Dla litery w haśle, jeśli listera jest jedną z użytych liter pokaż tę literę.
Jeśli litery nie ma to pokaż znak-.
Jeśli licznik równa się 0 to użytkownik odgadł literę.
Definiuje podanie litery przez użytkownika(input do odgadnięcia hasła).
Jeśli podana przez użytkownika litera nie jest równa literze skladajacej sie na haslo i liczba prob zostanie wykorzystana to przekaz graczowi koniec gry(koniec pętli).
Jeśli podane litery są rowne hasłu, poinformuj o tym gracza(koniec pętli).








