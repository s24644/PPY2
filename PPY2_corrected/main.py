#zadanie 1

a = "Python 2023"
b = "Python 2023"
c = "Python 2023"

print("zad 1a")
print(a==b)
print("zad 1b")
print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

print("zmiana trzeciej zmiennej")
c = "Java 11"
print("ponowne wykonanie a i b")
print(a==b)
print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

#zadanie 2

liczba1 = input("podaj pierwsza liczbe")
liczba2 = input("podaj druga liczbe")
operator = input("podaj operator")

if operator == '+':
    print(int(liczba1)+int(liczba2))
elif operator == '-':
    print(int(liczba1)-int(liczba2))
elif operator == '*':
    print(int(liczba1)*int(liczba2))
elif operator == '/':
    print(int(liczba1)/int(liczba2))

#zadanie 3

imie_nazwisko = input("podaj swoje imie i nazwisko")

dictionary1 = {
    "a" : "oglądanie TV, seriali",
    "b" : "czytanie książki",
    "c" : "słuchanie muzyki",
    "d" : "spotkania z rodziną"
}

answer1 = input("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: " + str(dictionary1))

dictionary2 = {
    "a" : "podczas podróży",
    "b" : "w czasie wolnym",
    "c" : "podczas pracy/nauki (to ich element)",
    "d" : "w ogóle nie czytam"
}

answer2 = input("W jakich okolicznościach czytasz książki najczęściej? " + str(dictionary2))


dictionary3 = {
    "a" : "chęć poszerzenia rzeczy",
    "b" : "czytanie mnie relaksuje",
    "c" : "fakt, że czytanie jest mądre",
    "d" : "czytanie to moje hobby"
}

answer3 = input("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? " + str(dictionary3))


dictionary4 = {
    "a" : "papierowej (tradycyjnej)",
    "b" : "e-booki na komputerze",
    "c" : "e-booki na tablecie/telefonie",
    "d" : "e-booki na specjalnym czytniku"
}

answer4 = input("Po książki w jakiej formie sięgasz najczęściej? " + str(dictionary4))

print("\n-------ODPOWIEDZI----------\n")

print("Imie i nazwisko: \t" + imie_nazwisko.title())
print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: \n odpowiedz: " + dictionary1[answer1])
print("pytanie: W jakich okolicznościach czytasz książki najczęściej? \n odpowiedz: " + dictionary2[answer2])
print("pytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? \n odpowiedz: " + dictionary3[answer3])
print("pytanie: Po książki w jakiej formie sięgasz najczęściej? \n odpowiedz: " + dictionary4[answer4])
