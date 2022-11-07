# uuid für Authentifizierung
import uuid

class Reimerei:
    def __init__(self, grundwort, reimwort) -> None:
        self.VOKALE = ["a","e","i","o","u","ä","ö","ü"]
        self.grundwort = grundwort 
        self.reimwort = reimwort

        self.vokalgruppen_gw = self.finde_vokale(grundwort)
        self.vokalgruppen_rw = self.finde_vokale(reimwort)

        self.wortEnde_gw = self.wortEnde(grundwort, self.vokalgruppen_gw)
        self.wortEnde_rw = self.wortEnde(reimwort, self.vokalgruppen_rw)
    
    def finde_vokale(self, wort) -> str:
        "Sucht die Vokalgruppen in einem Wort, return {'ie25283': [3, 4], 'e19900': [6, 6]}"
        vokale_index = dict()
        index = 0

        while index != len(wort):
            buchstabe = wort[index]
            vokalgruppe = ""

            # vokalgruppe: ist der Start Index und der Ende Index
            vokalgruppe_start_ende = []

            # Die ID ist wichtig, weil Wöter mehrmals die gleiche Vokalgruppe haben (z.B. Baumhaus)
            # ohne ID würde sich das Dictionary überschreiben bei Dopplungen
            id = (str(uuid.uuid4().fields[-1])[:5])

            # überprüft ob der  Buchstabe ein Vokal ist
            if buchstabe in self.VOKALE:
                vokalgruppe += buchstabe

                # makiert den Anfang der Vokalgruppen
                vokalgruppe_start_ende.append(index)

                # try, weil Wörter auf einen Vokal enden und somit einen IndexError
                # verursachen würden (z.B. Biene)
                try:
                    index += 1 
                    buchstabe = wort[index]

                    # überprüft ob der nächste Buchstabe auch ein Vokal ist
                    if buchstabe in self.VOKALE:
                        vokalgruppe += buchstabe

                        # makiert das Ende der Vokalgruppen
                        vokalgruppe_start_ende.append(index)
                        vokale_index[vokalgruppe + id] = vokalgruppe_start_ende 
                        index += 1
                    else:
                        # makiert das Ende der Vokalgruppen
                        vokalgruppe_start_ende.append(vokalgruppe_start_ende[0])

                        vokale_index[vokalgruppe + id] = vokalgruppe_start_ende
                except IndexError:
                    # makiert das Ende der Vokalgruppen
                    vokalgruppe_start_ende.append(vokalgruppe_start_ende[0])

                    vokale_index[vokalgruppe + id] = vokalgruppe_start_ende                
            else:    
                index += 1
        
        return vokale_index

    def wortEnde(self, wort, vokaleWort) -> str:
        "gibt das Wort ab der maßgeblichen Vokalgruppe zurück"

        if len(vokaleWort) > 1:
            maßgebliche_vokabelgruppe = list(vokaleWort.values())[-2][0]
            mg_ende = wort[maßgebliche_vokabelgruppe:]
            return mg_ende

        elif len(vokaleWort) == 1:
            maßgebliche_vokabelgruppe = list(vokaleWort.values())[-1][0]
            mg_ende = wort[maßgebliche_vokabelgruppe:]
            return mg_ende

        elif len(vokaleWort) == 0:
            return ""

    def bedingung1(self) -> bool:
        """überprüft, ob die Wörter dieselbe maßgebliche Vokalgruppen, und nach der
            maßgeblichen Vokalgruppe dieselben Buchstaben in derselben Reihenfolge haben"""

        return True if self.wortEnde_gw == self.wortEnde_rw else False

    def bedingung2(self) -> bool:
        'überprüft, ob die maßgebliche Vokalgruppe und was ihr folgt mindestens die Hälfte der Buchstaben hat'

        laenge_ende_gw = len(self.wortEnde_gw)
        erwartete_laenge_gw = len(self.grundwort)/2
        # vergleicht ob das Ende der erwartete
        überHälfte_gw= True if laenge_ende_gw >= erwartete_laenge_gw else False

        laenge_ende_rw = len(self.wortEnde_rw)
        erwartete_laenge_rw = len(self.reimwort)/2
        überHälfte_rw = True if laenge_ende_rw >= erwartete_laenge_rw else False

        if überHälfte_gw == True and überHälfte_rw == True:
            return True
        else:
            return False

    def bedingung3(self) -> bool:
        "überprüft, ob die Wörter ineinander vorkommen"

        if self.grundwort in self.reimwort or self.reimwort in self.grundwort:
            return True
        else:
            return False

if __name__ == "__main__":
    woerter = []

    # liest die Datei ein und speichert die Wörter in "woerter"
    with open(r"BWINF_WETTBEWERB_2022\Reimerei\reimerei0.txt", "r", encoding="utf-8") as f:
        zeile = f.readlines()
        for word in zeile:
            woerter.append(word.strip())

    # Iteriert über jedes Wort 
    for gw in woerter:
        # da es mehrere passende Wörter geben kann, werden sie hier zwischengespeichert
        # reime = ""

        # Iteriert über jedes Wort und vergleicht mit dem Grundwort  
        for rg in woerter:
            grundwort = str(gw).lower()
            reimwort = str(rg).lower()
            
            reim = Reimerei(grundwort, reimwort)

            # überprüft die Bedingungen für ein Reim
            be1 = reim.bedingung1()
            be2 = reim.bedingung2()
            be3 = reim.bedingung3()     

            if be1 == True and be2 == True and be3 == False:
                #reime += rg + "; "
                print(f"{gw} -> {rg}")
        
        # gibt alle passenden Reime zu dem Wort aus, 
        # falls es passende Reime gibt
        # if reime != "":
        #     print(f"{gw} -> {reime}")