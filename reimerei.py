# Vokale/Umlaute sind: a, e, i, o, u, ä, ö ,ü
# Konsonanten sind: alle anderen der 26 Buchstaben des Alphabets 

#print("bem" in wort) # 3.

woerter = ["bemühen","Biene","breitschlagen","glühen","hersagen","Hygiene","Knecht","Recht","Schiene","schlank","Schwank"]
wort = "bemühen"

dic_vok = {"a": [], "e": [], "i": [], "o": [], "u": [], "ä": [], "ö": [], "ü": []}
for index, buchstabe in enumerate(wort):
    if buchstabe == "a":
        dic_vok["a"] += [index]
    if buchstabe == "e":
        dic_vok["e"] += [index]
    if buchstabe == "i":
        dic_vok["i"] += [index]
    if buchstabe == "o":
        dic_vok["o"] += [index]
    if buchstabe == "u":
        dic_vok["u"] += [index]
    if buchstabe == "ä":
        dic_vok["ä"] += [index]
    if buchstabe == "ö":
        dic_vok["ö"] += [index]
    if buchstabe == "ü":
        dic_vok["ü"] += [index]

print(dic_vok)
