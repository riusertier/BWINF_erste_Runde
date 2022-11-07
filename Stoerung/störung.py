text = "BWINF_WETTBEWERB_2022\Stoerung\Alice_im_Wunderland.txt"
# text = "Hallo, ich bin Lars Wisotzky. Ich komme aus Deutschland."

stoerung = "BWINF_WETTBEWERB_2022\Stoerung\stoerung1.txt"
stoerung = "wollen _ so _ sein"


def filter_text(zeile):
    # alle Zeilenumbrüche entfernen, die seperat sind
    for i in range(len(zeile)):
            if zeile[i] == '\n':
                zeile[i] = ' '

    # alle Zeilenumbrüche entfernen, die mit string verbunden sind
    text = ""
    verbotene_zeichen = ["?", "!", ",", "»", "«", ";", "*",".", "[", "]", "(", ")"]
    for stelle in zeile:
        print(stelle)
        stelle.strip()
        for zeichen in verbotene_zeichen:
            stelle = stelle.replace(zeichen, "")
        text += stelle
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
    stoerung = read_file(stoerung.lower())
else:
    stoerung = stoerung.lower().split()

txtstelle_dict = {}
# Nachdem Anfangswort wird im Text gesucht, ist also ein Schlüsselwort
anfangswort = stoerung[0]
# Anfangswort_index gibt an bei welchem Index das Anfangswort auftritt
anfangswort_index = []

for index, wort in enumerate(stoerung):
    txtstelle_dict[index] = wort

# sucht nachden Anfangswort im Text und speichert es in anfangswort_index
for index, wort in enumerate(text):
    if anfangswort == wort:
        anfangswort_index.append(index)

# filtert die Unterstriche raus 
erwartete_woerter = stoerung
for x in range(erwartete_woerter.count("_")):
    erwartete_woerter.remove("_")

# Wiederholt so oft wie es das Anfangswörter im Text gibt
for index in range(len(anfangswort_index)):
    # Ende der Wortgruppe bezogen auf dem Text 
    ende_index = anfangswort_index[index] + len(txtstelle_dict)

    # möglicherweise komplette  Wortgruppe (zum Vergleichen der Ergebnisse) 
    algo_output = []
    # möglicherweise komplette  Wortgruppe (für Ausgabe) 
    komplete_wortgruppe = ""

    zaehler = 0
    # Jedes Wort was sich im Bereich des Anfangswortes (Index) und dem Ende Index befindet
    for item in text[anfangswort_index[index]:ende_index]:
        if item == txtstelle_dict[zaehler]:
            algo_output.append(item)
        zaehler += 1

        komplete_wortgruppe += (item + " ")
    # hier wird das Ergebnis des Algorithmusses mit der Störung ohne Unterstriche verglichen
    if algo_output == erwartete_woerter:
        print(komplete_wortgruppe)
