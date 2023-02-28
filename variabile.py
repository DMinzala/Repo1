# variabila = zona din memoria unui PC care tine un anumit tip de date
# variablia = o cutiuta in care punem valori

# am declarat si initializar variabila marca_masina
marca_masina = 'Volvo'
model_masina = 'XC 60'

# nu putem sa punem spatiu in numele variabilei
# o variabila incepe cu litera mica

# loosly typed - nu trebuie sa specificam tipul de date al variabilelor cu care lucram

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

# suprascriere = inlocuieste vechea valoare cu cea noua - overwrite
model_masina  = 'XC 60 facelift'

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

nume = 'Sinpetrean'
prenume  = 'Andy'
varsta = 34
# print(nume + ' ' + prenume + varsta) va da eroarept ca nu aduna caractere cu numere
print(f'{prenume} {nume} in varsta de {varsta} ani')