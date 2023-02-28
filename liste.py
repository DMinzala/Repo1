# Listele in Pithon pot sa cuprinda elemente de tipuri diferite
# au dimensiune mdinamica, adica nu sunt imutabile

fructe = ['mar', "banana","portocala", 3, True, 3]
# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'

# afisam lista
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scote si ne returneaza ultimul element
last = fructe.pop()
print('Ultimul element: ', last)
print('Lista: ', fructe)

# de cate ori apare un element?
print(fructe.count(3))

# extindem lista
fructe_exotice = ["ananas", "Kiwi"]
fructe.extend(fructe_exotice)
print(fructe)

