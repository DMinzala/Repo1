'''
Flow control - if else
Evaluaza conditii si bifurca codul in functie de rezultat
'''

# if
piesa_faina = True

print('pornim radoiul')
if piesa_faina == True:
    print('dau radioul mai tare')
    print('fredonez piesa')
print('inchid radioul')

# if else
# daca numarul este par atunci printez acest lucru
# altfel printez impar
nr = 4
# ce inseamna par? se imparte la 2
# ce inseamna ca se imparte la 2? restul este 0
if nr % 2 == 0:
    print('numar par')
else:
    print('impar')

# este un nr pozitiv?
if (nr > 0):
    print('pozitiv')
else:
    print('nr-ul nu este pozitiv')

# if, else if, else
# cum ne salutarobotelul in functie de ora?
# luam date de la tastatura
# ne asiguram ca sunt transformate din string in integer
# ora = int(input('Introdu ora'))
# if ora < 0:
#     print('ora invalida. ora negativa') # daca aleg ora 19 care nu este < 0, Python va ignora
# elif ora <= 11:
#     print('Buna dimineata!') # testez pentru fiecare interval in parte pana gasesc iesirea true
# elif ora <= 18:
#     print('Buna ziua!')
# elif ora <= 21:
#     print('Buna seara!')
# elif ora <= 24:
#     print('Noapte buna!')
# else:
#     print('ora invalida ora mai mare de 24') # In orice alta situatie se va afisa aceasta
# CTRL = / liniile de code selectate devin comenteriu -cand nu reu sa ruleze / si viceversa

optiune = int(input('Alege o optiune'))
if optiune == 0:
    print('meniu anterior')
elif optiune == 1:
    print('ati ales romana')
elif optiune == 2:
    print('ati ales engleza')
else:
    print('nu am identificat optiune, mai incearca')





