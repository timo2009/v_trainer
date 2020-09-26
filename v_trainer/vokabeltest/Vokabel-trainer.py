# Bauanleitung für ein englisches Wort in der VokabelApp
class EnglischesWort:

    # Hier wird definiert was bei der Erstellung eines Objektes vom Typ EnglischesWort benötigt wird.
    def __init__(self, englisches_wort):
        self.englisches_wort = englisches_wort
        self.deutsche_woerter = []

    def get_enlisches_wort(self):
        return self.englisches_wort

    # Diese Funktion hängt der Liste deutsche_woerter ein deutsche Wort an
    def set_deutsche_woerter(self, deutsches_wort):
        self.deutsche_woerter.append(deutsches_wort)

    # Diese Funktion gibt die Liste aller deuschen Wörter zurück mit denen man das englische Wort übersetzen kann.
    def get_deutsche_woerter(self):
        return self.deutsche_woerter


# Wenn das Programm mit python hello_world gestartet wird dann ist der Name des Programms = dem Namen der Datei
if __name__ == "__main__":

    ew_1 = EnglischesWort("happy")
    ew_1.set_deutsche_woerter("fröhlich")
    ew_1.set_deutsche_woerter("glücklich")
    ew_1.set_deutsche_woerter("erfreut")
    ew_1.set_deutsche_woerter("zufrieden")
    ew_1.set_deutsche_woerter("freuen")
    ew_1.set_deutsche_woerter("frohe")
    ew_1.set_deutsche_woerter("froh")
    ew_1.set_deutsche_woerter("freudevoll")
    ew_1.set_deutsche_woerter("freut")
    ew_1.set_deutsche_woerter("freudig")
    ew_1.set_deutsche_woerter("freudiges")
    ew_1.set_deutsche_woerter("frohes")

    ew_2 = EnglischesWort("house")
    ew_2.set_deutsche_woerter("Haus")
    ew_2.set_deutsche_woerter("Gebäude")
    ew_2.set_deutsche_woerter("Hause")
    ew_2.set_deutsche_woerter("Wohnung")
    ew_2.set_deutsche_woerter("Wohnhaus")
    ew_2.set_deutsche_woerter("Haushalt")
    ew_2.set_deutsche_woerter("Häuschen")
    ew_2.set_deutsche_woerter("Tagungshaus")
    ew_2.set_deutsche_woerter("Firma")

    ew_3 = EnglischesWort("sad")
    ew_3.set_deutsche_woerter("traurig")
    ew_3.set_deutsche_woerter("traurige")
    ew_3.set_deutsche_woerter("leider")
    ew_3.set_deutsche_woerter("bedauerlich")
    ew_3.set_deutsche_woerter("betrübt")
    ew_3.set_deutsche_woerter("trist")
    ew_3.set_deutsche_woerter("Trauer")
    ew_3.set_deutsche_woerter("trübseeligkeit")
    ew_3.set_deutsche_woerter("bedauerlicherweise")

    ew_4 = EnglischesWort("tree")
    ew_4.set_deutsche_woerter("Baum")
    ew_4.set_deutsche_woerter("der Baum")
    ew_4.set_deutsche_woerter("Stammbaum")
    ew_4.set_deutsche_woerter("Struktur")
    ew_4.set_deutsche_woerter("Verzeichnisbaum")
    ew_4.set_deutsche_woerter("Bäume")
    ew_4.set_deutsche_woerter("Stamm")
    ew_4.set_deutsche_woerter("Die Baumansicht")
    ew_4.set_deutsche_woerter("Verzechnisstruktur")

    ew_5 = EnglischesWort("love")
    ew_5.set_deutsche_woerter("Liebe")
    ew_5.set_deutsche_woerter("sehr mögen")
    ew_5.set_deutsche_woerter("lieben")
    ew_5.set_deutsche_woerter("verliebt")

    # Ausgabe des englischen Wortes
    import random

    deutsches_wort = 'Start'
    richtige_woerter = 0
    falsche_woerter = 0
    while deutsches_wort != 'Verlassen':

        englische_worter = [ew_1, ew_2, ew_3, ew_4, ew_5]

        zufallszahl_ew = random.randint(0, 4)

        englische_wort = englische_worter[zufallszahl_ew].get_enlisches_wort()
        woerterliste = englische_worter[zufallszahl_ew].get_deutsche_woerter()

        print(englische_wort)

        # Ausgabe aller deutschen Wörte

        # print(ew_1.get_deutsche_woerter())

        # Eingabe einer Antwort (deutsches Wort)

        deutsches_wort = input("Wie lautet das deutsche Wort: ")

        if deutsches_wort == "Verlassen":
            print("Sie haben: " + str(richtige_woerter) + " richtige Wörter")
            print("Sie haben: " + str(falsche_woerter) + " falsche Wörter")
        # Kontrolle ob das deutsche Wort richtig ist
        # wenn wort in List

        if deutsches_wort in woerterliste:
            # Ausgabe an den Nutzer, ob er recht hatte
            print("richtig")
            richtige_woerter = richtige_woerter + 1
        # andernfalls
        elif deutsches_wort == 'Verlassen':
            pass
        else:

            # Ausgabe an den Nutzer, ob er recht hatte
            print("falsch")
            falsche_woerter = falsche_woerter + 1
