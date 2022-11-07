import uuid
# list(vokale_index.values())[-1]
# list(vokale_index.keys())[-1]
vokale = ["a","e","i","o","u","ä","ö","ü"]

def finde_vokale(wort):
    "Sucht die Vokalgruppen in einem Wort, return {'ie25283': [3, 4], 'e19900': [6, 6]}"
    vokale_index = dict()
    index = 0
    while index != len(wort):
        buchstabe = wort[index]
        vokalgruppe = ""
        vokal_s_e = []
        # Es wird eine Id gebraucht, weil gleiche Vokale mehrmals vorkommen können und sie somit überschrieben werden können
        id = (str(uuid.uuid4().fields[-1])[:5])

        if buchstabe in vokale:
            vokalgruppe += buchstabe
            vokal_s_e.append(index)

            # zb Biene -> e am ende -> sucht nach vokalen hinter dem ersten Vokal aber Wort ist zu ende -> IndexError
            try:
                index += 1 
                buchstabe = wort[index]

                if buchstabe in vokale:
                    vokalgruppe += buchstabe
                    vokal_s_e.append(index)
                    vokale_index[vokalgruppe + id] = vokal_s_e 
                    index += 1
                else:
                    vokal_s_e.append(vokal_s_e[0])
                    vokale_index[vokalgruppe + id] = vokal_s_e
            except IndexError:
                vokal_s_e.append(vokal_s_e[0])
                vokale_index[vokalgruppe + id] = vokal_s_e

                
        else:    
            index += 1
    return vokale_index

def m_gEnde(wort, vokaleWort):
    "gibt das Wort ab der maßgeblichen Vokalgruppe zurück"

    #print(vokaleWort)

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
    

# -------------------------------------------------------------------------------------------


def bedingung1(grundwort, mglWort):
    vokaleWort_gw = finde_vokale(grundwort)
    vokaleWort_mglw = finde_vokale(mglWort)

    endeWort_gw = m_gEnde(grundwort, vokaleWort_gw)
    endeWort__mglw = m_gEnde(mglWort, vokaleWort_mglw)
    if endeWort_gw == endeWort__mglw:
        return True
    else:
        return False

def bedingung2(grundwort, mglWort):
    # {'au21423': [1, 2]} {'au23835': [1, 2]}
    vokaleWort_gw = finde_vokale(grundwort) 
    vokaleWort_mglw = finde_vokale(mglWort)

    # aummm aum
    endeWort_gw = m_gEnde(grundwort, vokaleWort_gw)
    endeWort__mglw = m_gEnde(mglWort, vokaleWort_mglw)

    # Bsp Baum Haelfte=2, ab maß. Vokalgruppe = 3 -> True
    laenge_gw = len(grundwort)
    laenge_ende_gw = len(endeWort_gw)
    erwartete_laenge_gw = laenge_gw/2
    gw_bool = True if laenge_ende_gw >= erwartete_laenge_gw else False

    laenge_mglw = len(mglWort)
    laenge_ende_mglw = len(endeWort__mglw)
    erwartete_laenge_mglw = laenge_mglw/2
    mglw_bool = True if laenge_ende_mglw >= erwartete_laenge_mglw else False

    if gw_bool == True and mglw_bool == True:
        return True
    else:
        return False

def bedingung3(grundword, wort):
    if grundword in wort or wort in grundword:
        return True
    else:
        return False

# -----------------------------------------------------------------------------------------------------
woerter = []

# liest die Textdatei ein und speichert die Wörte in einer Liste
with open(r"BWINF_WETTBEWERB_2022\Reimerei\reimerei0.txt", "r", encoding="utf-8") as f:
    zeile = f.readlines()
    for word in zeile:
        woerter.append(word.strip())

#  für jedes Wort in der Liste werden dann alle Wörter überprüft 
for grundwort in woerter:
    # da es mehrere passende Wörter geben kann, werden sie hier zwischengespeichert
    all_pass = ""
    for moeglichesWort in woerter:
        moeglichesWortc = str(moeglichesWort).lower()
        grundwortc = str(grundwort).lower()

        #print(grundwort, moeglichesWort)

        be1 = bedingung1(grundwortc, moeglichesWortc)
        be2 = bedingung2(grundwortc, moeglichesWortc)
        be3 = bedingung3(grundwortc, moeglichesWortc)     

        if be1 == True and be2 == True and be3 == False:
            all_pass += moeglichesWort + "; "
    
    print(f"Wort: {grundwort} / Reime: {all_pass}")

    