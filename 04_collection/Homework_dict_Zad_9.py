#5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach. Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)
print("Podaj dane uzykowniku 1: ")
inp1 = list(input().split())
print(inp1)
print("Podaj dane uzykowniku 2: ")
inp2 = list(input().split())
print(inp2)
print("Podaj dane uzykowniku 3: ")
inp3 = list(input().split())
print(inp3)
print("Podaj dane uzykowniku 4: ")
inp4 = list(input().split())
print(inp4)
print("Podaj dane uzykowniku 5: ")
inp5 = list(input().split())
print(inp5)
inp_ul=inp1+inp2+inp3+inp4+inp5
print('Polaczone listy', inp_ul)
print('Najpopularniejsze przedmioty',set([x for x in inp_ul if inp_ul.count(x)>1]))






