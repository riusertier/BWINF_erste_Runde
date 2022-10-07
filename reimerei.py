import uuid
# list(vokale_index.values())[-1]
# list(vokale_index.keys())[-1]

grundwort = "Bmmmmaum"
moeglichesWort  = "Bmmmmaum"
vokale = ["a","e","i","o","u","ä","ö","ü"]

def finde_vokale(wort):
    vokale_index = dict()
    index = 0
    while index != len(wort):
        buchstabe = wort[index]
        vokal_gruppe = ""
        vokal_s_e = []
        id = (str(uuid.uuid4().fields[-1])[:5])

        if buchstabe in vokale:
            vokal_gruppe += buchstabe
            vokal_s_e.append(index)
            index += 1
            buchstabe = wort[index]

            if buchstabe in vokale:
                vokal_gruppe += buchstabe
                vokal_s_e.append(index)
                vokale_index[vokal_gruppe + id] = vokal_s_e 
                index += 1
            else:
                vokal_s_e.append(vokal_s_e[0])
                vokale_index[vokal_gruppe + id] = vokal_s_e
                
        else:    
            index += 1
    return vokale_index

def m_gEnde(wort, vokaleWort):
    "gibt das Wort ab der maßgeblichen Vokalgruppe zurück"

    if len(vokaleWort) > 1:
        maßgebliche_vokabelgruppe = list(vokaleWort.values())[-2][0]
    else:
        maßgebliche_vokabelgruppe = list(vokaleWort.values())[-1][0]
    mg_ende = wort[maßgebliche_vokabelgruppe:]
    return mg_ende

def bedingung_2(word, mg_ende_wort):
    """Überprüft ob die maßgebliche Vokalgruppe und was ihr folgt
    mindestens die Hälfte der Buchstaben des gesamten Wortes entsprechen"""

    laenge = len(word)
    laenge_mg = len(mg_ende_wort)
    erwartete_laenge = laenge/2
    if laenge_mg >= erwartete_laenge:
        return True
    else:
        return False

def bedingung_3(grundword, wort):
    if grundword in wort or wort in grundword:
        return True
    else:
        return False

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
    vokaleWort_gw = finde_vokale(grundwort)
    vokaleWort_mglw = finde_vokale(mglWort)

    endeWort_gw = m_gEnde(grundwort, vokaleWort_gw)
    endeWort__mglw = m_gEnde(mglWort, vokaleWort_mglw)

    laenge_gw = len(grundwort)
    laenge_ende_gw = len(endeWort_gw)
    erwartete_laenge_gw = laenge_gw/2
    gw_bool = True if laenge_ende_gw >= erwartete_laenge_gw else False

    laenge_mglw = len(grundwort)
    laenge_ende_mglw = len(endeWort__mglw)
    erwartete_laenge_mglw = laenge_mglw/2
    mglw_bool = True if laenge_ende_mglw >= erwartete_laenge_mglw else False

    if gw_bool == True and mglw_bool == True:
        return True
    else:
        return False

#haelfteBuchstaben = bedingung_2(grundwort, endeWort)
be3 = bedingung_3(grundwort, moeglichesWort)

be1 = bedingung1(grundwort, moeglichesWort)

print(be1, be3)
