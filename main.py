import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):
    t.printMenu()


    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola vuoi aggiungere?")
        parola = str(input())
        parti=parola.split()
        if len(parti)<2:
            print("Errore: inserire parola e traduzioni")
            continue
        #for p in parti:
        #    if not p.isalpha():
        #       print ("Errore: Le parole possono contenere solo lettere")
        #        continue

        t.handleAdd(parola)

    if int(txtIn) == 2:
        print ("Ok, quale parola vuoi cercare?")
        parola=input().lower()
        t.handleTranslate(parola)

    if int(txtIn) == 3:
        txtIn = input("Ok, quale parola vuoi aggiungere?")
        pass

    if int (txtIn)==4:
        pass

    if int(txtIn) == 5:
        break