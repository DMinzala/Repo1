# 2.Noteaza in limbajul de programare Python, in cadrul unui comentariu,
# ce este o variabila string – explica cu cuvintele tale
# O variabila String este o insiruire de caractere delimitate de ghilimele simple ''

# 4.Declara si initializeaza in limbajul de programare python cate o variabila din fiecare
# din urmatoarele tipuri: string, integer, float,boolean. Alege valorile dupa preferinta ta.

# Declarare si initializare - String
profesor_materie = 'matematica'
# Declarare si initializare - Integer
profesor_grad = 2
# declarare si initializare - double/float
vechime = 17.50
# Declarare si initializare - boolean
promovat = True
print(f'Profesorul de: {profesor_materie} a promovat examenul de grad {promovat}')
print(f'Are gradul:{profesor_grad} si o vechime {vechime} ani')

# 6. Scrie segmentul de cod de la exercitiul 5 in limbajul de programare Python

for i in range(1, 20, 3):
    print(f'numarul actual este {i}')
