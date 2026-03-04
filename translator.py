from dictionary import Dictionary
class Translator:

    def __init__(self):
        self.dictionary=Dictionary()  #Creto l'oggetto dizionario


    def printMenu(self):
        print ("--------------------------")
        print("Translator Alien-Italian")
        print("--------------------------")
        # 1. Aggiungi nuova parola
        print ("1. Aggiungi nuova parola:")
        # 2. Cerca una traduzione
        print ("2. Cerca una traduzione")
        # 3. Cerca con wildcard
        print ("3. Cerca con wildcard")
        # 4. Exit
        print ("4. Stampa tutto il Dizionario")
        print ("5.Exit")
        print("--------------------------")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open (dict, "r", encoding="utf-8") as file:
            for riga in file:
                campi=riga.strip().split()
                aliena=campi[0]
                traduzioni= campi[1:]
                self.dictionary.addWord(aliena, traduzioni)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        aliena=entry[0]
        traduzioni=entry[1:]
        #if aliena.isalpha() and (t.isalpha() for t in traduzioni):
        self.dictionary.addWord(aliena, traduzioni)
        #else:
          #  print("Errore")
        print("dopo aggiunta:", self.dictionary)
        print ("Aggiunta!")


    def handleTranslate(self, query):
        risultato=self.dictionary.translate(query)
        if risultato:
            print (f"Traduzione: {risultato}")
        else:
            print ("Parola non trovata")


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass