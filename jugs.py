jug_three = 0
jug_five = 0
abi = """
Selles mängus on antud üks 3-liitrine ja üks 5-liitrine anum.
Ülesandeks on üks neist anumaist täita täpselt nelja liitri veega.
Anumate täitmiseks või tühjendamiseks kasuta käske:
"täida 3": täidab 3-liitrise anuma ääreni
"täida 5": täidab 5-liitrise anuma ääreni
"tühjenda 3": tühjendab 3-liitrise anuma
"tühjenda 5": tühjendab 5-liitrise anuma
"vaheta 3 5": valab 3-liitrisest anumast 5-liitrisesse anumasse
kuni 3-liitrine anum saab tühjaks või 5-liitrine saab täis
"vaheta 5 3": valab 5-liitrisest anumast 3-liitrisesse anumasse
kuni 5-liitrine anum saab tühjaks või 3-liitrine saab täis
"abi": näitab seda sõnumit uuesti
Edu!
"""
print(abi)
while jug_five != 4:
    print("3-liitrises anumas on: " + str(jug_three) + " liitrit.")
    print("5-liitrises anumas on: " + str(jug_five) + " liitrit.")
    command = input().split(' ')
    if command[0] == 'abi':
        print(abi)
    elif command[0] == 'täida':
        if command[1] == '3': jug_three = 3
        elif command[1] == '5': jug_five = 5
        else: print("ERROR")
    elif command[0] == 'tühjenda':
        if command[1] == '3': jug_three = 0
        elif command[1] == '5': jug_five = 0
        else: print("ERROR")
    elif command[0] == 'vaheta':
        if command[1] == '3' and command[2] == '5':
            while jug_three != 0 and jug_five < 5:
                jug_three -= 1
                jug_five += 1
        elif command[1] == '5' and command[2] == '3':
            while jug_three < 3 and jug_five != 0:
                jug_three += 1
                jug_five -= 1
        else:
            print("ERROR")
    else:
        print("ERROR")
print("3-liitrises anumas on: " + str(jug_three) + " liitrit.")
print("5-liitrises anumas on: " + str(jug_five) + " liitrit.")
print("Palju õnne! Täitsid edukalt ühe anumaist täpselt nelja liitri veega!")
print("Mängust väljumiseks vajuta ENTER.")
input()
