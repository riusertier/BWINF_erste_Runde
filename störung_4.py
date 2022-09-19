text = "BWINF_WETTBEWERB_2022\Stoerung\Alice_im_Wunderland.txt"
text = "Hallo ich bin Lars"

stoerung = "BWINF_WETTBEWERB_2022\Stoerung\stoerung1.txt"
stoerung = "hallo _ _"


def filter_text(zeile):
    # alle Zeilenumbrüche entfernen, die seperat sind
    for i in range(len(zeile)):
            if zeile[i] == '\n':
                zeile[i] = ' '

    # alle Zeilenumbrüche entfernen, die mit string verbunden sind
    text = ""
    verbotene_zeichen = ["?", "!", ",", "»", "«", ";", "*",".", "[", "]", "(", ")"]
    for phrase in zeile:
        phrase.strip()
        for zeichen in verbotene_zeichen:
            phrase = phrase.replace(zeichen, "")
        text += phrase
    return text

def read_file(dateipfad):
    # encoding="utf-8", damit Umlaute richtig konvertiert werden
    with open(dateipfad, 'r', encoding="utf-8") as f:
        zeile = f.readlines()
        text = filter_text(zeile)
        
            
        # lower, weil die textstellen kleingeschrieben werden
        # split, damit jedes Wort einzeln ist
        text = text.lower().split()
        return text


if text[-4:(len(text))] == ".txt":
    text = read_file(text)
else:
    text = filter_text(text)
    text = text.lower().split()


if stoerung[-4:(len(stoerung))] == ".txt":
    stoerung = read_file(stoerung)
else:
    stoerung = stoerung.split()

txtstelle_dict = {}
# Nachdem Anfangswort wird im Text gesucht, ist also ein Schlüsselwort
anfangswort = stoerung[0]
# Anfangswort_index gibt an bei welchem Index das Anfangswort auftritt
anfangswort_index = []

for index, wort in enumerate(stoerung):
    txtstelle_dict[index] = wort
# print(txtstelle_dict)

# sucht nachden Anfangswort im Text und speichert es in anfangswort_index
for index, wort in enumerate(text):
    if anfangswort == wort:
        anfangswort_index.append(index)

# filtert die Unterstriche raus 
stoerung_woerter = stoerung
for x in range(stoerung_woerter.count("_")):
    stoerung_woerter.remove("_")

for index in range(len(anfangswort_index)):
    # ende_index gibt an, wie viele Wörter im Text gesucht werdern sollen nachdem Schlüsselwort
    ende_index = anfangswort_index[index] + len(txtstelle_dict)
    # Der Zähler gibt
    zaehler = 0
    # Wörter die richig sein könnte
    erwartete_woerter = []
    # die komplete Wortgruppe ohne Störung
    komplete_wortgruppe = ""

    for item in text[anfangswort_index[index]:ende_index]:

        if item == txtstelle_dict[zaehler]:
            erwartete_woerter.append(item)
        zaehler += 1

        komplete_wortgruppe += (item + " ")

    if erwartete_woerter == stoerung_woerter:
        print(komplete_wortgruppe)