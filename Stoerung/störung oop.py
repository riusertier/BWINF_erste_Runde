class Stoerung:
    def __init__(self, text_dateipfad=None, text=None, textstelle_dateipfad=None, textstelle=None):
        self.text = None
        self.textstelle=None
        self.txtstelle_dict = dict()
        self.anfangswort_index = list()
        self.vollständige_textstelle = str()
        self.verbotene_zeichen = ["?", "!", ",", "»", "«", ";", "*",".", "[", "]", "(", ")"]

        if text_dateipfad != None:
            self.text = self.textdatei_lesen(text_dateipfad)
        else:
            self.text = self.filter_text(text)

        if textstelle_dateipfad != None:
            self.textstelle= self.textdatei_lesen(textstelle_dateipfad)
        else:
            self.textstelle = textstelle.lower().split()
        
        self.erwartete_woerter = self.textstelle


    def filter_text(self, zeile):
        
        # alle Zeilenumbrüche entfernen, die seperat sind
        for i in range(len(zeile)):
                if zeile[i] == '\n':
                    zeile[i] = ' '

        # alle Zeilenumbrüche entfernen, die mit string verbunden sind
        text = ""
        for stelle in zeile:
            stelle.strip()
            for zeichen in self.verbotene_zeichen:
                stelle = stelle.replace(zeichen, "")
            text += stelle
        text= text.lower().split()
        return text

    def textdatei_lesen(self, dateipfad):
        with open(dateipfad, 'r', encoding="utf-8") as f:
            zeile = f.readlines()
            text_zeile = self.filter_text(zeile)
            return text_zeile

    def indexierung(self):
        for index, wort in enumerate(self.textstelle):
            self.txtstelle_dict[index] = wort

    def anfangswoerter_text(self):
        for index, wort in enumerate(self.text):
            anfangswort = self.textstelle[0]
            if anfangswort == wort:
                self.anfangswort_index.append(index)

    def erwartungswert(self):

        for _ in range(self.erwartete_woerter.count("_")):
            self.erwartete_woerter.remove("_")

    def algorithmus(self):
        for index in range(len(self.anfangswort_index)):
            ende_index = self.anfangswort_index[index] + len(self.txtstelle_dict)

            algo_output = []
            komplete_wortgruppe = ""
             
            zaehler = 0
            for item in self.text[self.anfangswort_index[index]:ende_index]:
                if item == self.txtstelle_dict[zaehler]:
                    algo_output.append(item)
                zaehler += 1

                komplete_wortgruppe += (item + " ")
            if algo_output == self.erwartete_woerter:
                self.vollständige_textstelle += komplete_wortgruppe + "\n"


if __name__ == "__main__":
    text = r"BWINF_WETTBEWERB_2022\Stoerung\Alice_im_Wunderland.txt"
    stoerung = "fressen _ gern _"

    textstelle = Stoerung(text_dateipfad=text, textstelle=stoerung)

    textstelle.indexierung()
    textstelle.anfangswoerter_text()
    textstelle.erwartungswert()
    textstelle.algorithmus()

    print(textstelle.vollständige_textstelle)