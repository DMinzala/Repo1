# declaram si initializam un dict

note_elevi = {'Gigel':10, 'Costel':9, 'Ana':10}

# adaug elemenete
note_elevi['Sebi'] = 7
#print dict
print(note_elevi)

# aflam elementele dupa key
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

# actualizare valori (suprascriere)
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea  (cu len)
print(len(note_elevi))

# stergem si returnam valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'Nu mai avem acest elev'))
print(note_elevi)

# returneaza doar cheile
print(note_elevi.keys())




