class Container:
    def __init__(self, dateipfad) -> None:
        self.dateipfad = dateipfad
        self.spalte1 = list()
        self.spalte2 = list()

        # Spalte ohne Duplikate von Gewichten
        self.ohne_dupl = list()

        self.schwerste = list()

    def containerPaare_einlesen(self):
        with open(self.dateipfad, 'r', encoding="utf-8") as f:
            container_paare = f.readlines()
            for container_paar in container_paare:
                # spaltet die 2 Werte in "container_paar" 
                container_paar = container_paar.strip().split()
                self.spalte1.append(container_paar[0])
                self.spalte2.append(container_paar[1])

    def duplikate_entfernen(self):
        "entfernt Duplikate der ersten Spalte"
        self.ohne_dupl = list(dict.fromkeys(self.spalte1))
        self.schwerste = list(dict.fromkeys(self.spalte1))

    def dopplungen_entferen(self):
        """Überprüft, ob die Werte von 'ohne_dupl' in der zeiten Spalte vorkommen. 
        Entfernt falls sie dort nocheinmal vorkommen"""

        for gewicht in self.ohne_dupl:
            if gewicht in self.spalte2:
                self.schwerste.remove(gewicht)
    


if __name__ == "__main__":
    phad = "BWINF_WETTBEWERB_2022\Container\container0.txt"
    c = Container(phad)
    c.containerPaare_einlesen()
    c.duplikate_entfernen()
    c.dopplungen_entferen()
    # print(c.schwerste)

    print(f"Eindeutig! Gewicht: {c.schwerste[0]}" if len(c.schwerste) == 1 else "Nicht eindeutig!")