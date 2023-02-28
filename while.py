# Proble: Masina merge cat timp are inca benzina
litri_benzina = 10
while litri_benzina > 0:
    # acceleram
    print("Vruum Vruum!")
    # scadem benzina
    litri_benzina = litri_benzina - 1
    # se aprinde martorul rosu!
    if litri_benzina <= 3:
        print('Se aprinde martorul rosu!')
print('Stop! nu mai avem benzina')
