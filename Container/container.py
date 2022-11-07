vektor_container = [] # [[1,3], [4,5]]
all_container = [] # [1,3,4,5]

dateipfad = "BWINF_WETTBEWERB_2022\Container\container0.txt"
with open(dateipfad, 'r', encoding="utf-8") as f:
    zeilen = f.readlines()
    for zeile in zeilen:
        zeile = zeile.strip().split()
        zeile = list(map(int, zeile))

        vektor_container.append(zeile)
        for container in zeile:
            all_container.append(container)

schwerster_container = max(all_container)
häufigkeit_schwerster_container = all_container.count(schwerster_container)

if häufigkeit_schwerster_container == 1:

    index_s_c = all_container.index(schwerster_container)
    if index_s_c%2 == 1:
        reihe = (index_s_c+1)/2 
    else:
        reihe = index_s_c/2 
    print(f"Der schwerste Container wiegt: {schwerster_container}")
    print(f"Er befindet sich in Reihe: {int(reihe)} Platz: {2 if index_s_c%2 == 1 else 1}")
else:
    print(f"Es gibt {häufigkeit_schwerster_container} Container die gleich wiegen.")
    print(f"Sie wiegen: {schwerster_container}")