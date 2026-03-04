class Dictionary:
    def __init__(self):
        self.dizionario={}  #DIZIONARIO -> chiave: parola aliena, valore: lista tradizioni

    def addWord(self, aliena, traduzioni):
        aliena=aliena.lower()
        if aliena not in self.dizionario:
            self.dizionario[aliena]=[]
        else:
            for t in traduzioni:
                self.dizionario[aliena]=traduzioni
    def translate(self, parola):
        parola_min=parola.lower()
        if parola_min in self.dizionario:
            return self.dizionario[parola_min]
        else:
            return "Parola non trovata"
#ic
    def translateWordWildCard(self):
        pass