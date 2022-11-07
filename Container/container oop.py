class Container:
    def __init__(self, dateipfad) -> None:
        self.dateipfad = dateipfad
        self.container_vektor = list()
        self.schwere_container = list()
        self.schwerster_container = int()
        self.anzahl_schwerster_container = int()
    
    def containerPaare_einlesen(self):
        with open(self.dateipfad, 'r', encoding="utf-8") as f:
            container_paare = f.readlines()
            for container_paar in container_paare:
                container_paar = container_paar.strip().split()
                container_paar = list(map(int, container_paar))

                self.container_vektor.append(container_paar)

    def containerPaare_vergleichen(self):
        for containerpaar in self.container_vektor:
            if containerpaar[0] > containerpaar[1]:
                self.schwere_container.append(containerpaar[0])
            else: 
                self.schwere_container.append(containerpaar[1])

    def schwersterConatiner(self):
        self.schwerster_container = max(self.schwere_container)
        self.anzahl_schwerster_container = self.schwere_container.count(self.schwerster_container)

if __name__ == "__main__":
    phad = "BWINF_WETTBEWERB_2022\Container\container0.txt"
    ctr = Container(phad)
    ctr.containerPaare_einlesen()
    ctr.containerPaare_vergleichen()
    ctr.schwersterConatiner()

    # print(ctr.container_vektor)
    # print(ctr.schwere_container)
    # print(ctr.schwerster_container)
    # print(ctr.anzahl_schwerster_container)

    print(f"Eindeutig! Gewicht: {ctr.schwerster_container}" if ctr.anzahl_schwerster_container == 1 else "Nicht eindeutig!")