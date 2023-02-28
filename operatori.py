'''
Operatori:
-aritmetici: +, -, *, /, %(aflarea restului imprtirii; ex: 10/3 = 3 rest 1)
-de comparare: <, >, ==, != (diferit), <=,>=
-logici: and (masina sa aiba si schimbator si pilot automat); or (sau schimbator sau pilot automat), !
'''


a = 3
b = 5
# operatori aritmetici
print(a + b) # 3+5 => 8

# operatori de comparare

print(a == b) # 3 = 5 => false

# operatori logici
print(a < b and a < 4) # 3<5 si 3<4? => True si True=> True
print(a < b or a < 2) # 3<5 sau 3<2? => True sau False=> True
# cu mama sau tata sau (cu bunica si bunicul)
mama = True
tata = True
bunicul =  False
bunica = False
print(mama or tata or(bunicul and bunica))
# modific False si True pt fiecare si vedem ce rezulta


