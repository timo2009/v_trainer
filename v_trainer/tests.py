from django.test import TestCase
from v_trainer.models import DeutschesWort, EnglischesWort, DeutschTestEineVokalel


# Diese Test soll den Deutschtest simulieren
# Bei der Testdefinition wird ein deutsches Wort ausgewählt
# Die Eingabe(Antwort) ist dann ein englisches Wort

class DeutschTestEineVokalelTestCase(TestCase):
    def setUp(self):
        deutsches_wort = DeutschesWort.objects.create(wort="Hallo")

        englisches_wort_1 = EnglischesWort.objects.create(wort="Hello")
        englisches_wort_2 = EnglischesWort.objects.create(wort="Hi")

        englisches_wort_1.dwort.add(deutsches_wort)
        englisches_wort_2.dwort.add(deutsches_wort)

    def test_deutsch_test_eine_vokabel(self):
        d_wort = DeutschesWort.objects.get(wort="Hallo")
        antwort_des_users = "Hello"
        ergebnis = 'falsch'

        # Beispiel: Publication.objects.get(id=4).article_set.all()
        # Wenn ein related_name vergeben wurde muss dieser verwendet werden
        # Der weg über das set klappt dann nicht mehr
        moeglische_englischen_antworten = d_wort.list_of_dwords.all()

        print("Mögliche englische Wörter für das deutsch Wort: " + d_wort.wort)
        print("-------------------------------------------------------------")
        for englische_antwort in moeglische_englischen_antworten:
            print("Antwort: " + englische_antwort.wort)

            if antwort_des_users == englische_antwort.wort:
                print(antwort_des_users + '==' + englische_antwort.wort)
                ergebnis = 'richtig'
            else:
                print(antwort_des_users + '!=' + englische_antwort.wort)

        self.assertEqual(ergebnis, "richtig")
