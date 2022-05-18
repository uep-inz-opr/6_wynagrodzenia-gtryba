class Pracownik: 
    def __init__(self, imie, brutto):
        self.imie = imie
        self.wyn_brutto = brutto

    def __repr__(self):
        return f"{self.imie} {self.wyn_brutto}"

    def wynagrodzenie_netto(self):
        skladki_c = self.wyn_brutto*0.0976 + self.wyn_brutto*0.015 + self.wyn_brutto*0.0245
        brutto_skladki_d = self.wyn_brutto - round(skladki_c, 2)
        skladki_zdrowotne_e = round(brutto_skladki_d, 2) * 0.09
        koszt_przychodu_g = 111.25
        skladka_ubezpieczenie_zdrowotne_f = round(brutto_skladki_d) * 0.0775
        podstawa_podatek_doch_h = int(self.wyn_brutto) - int(koszt_przychodu_g) - int(skladki_c)
        zaliczka_podatek_doch_i = (round(podstawa_podatek_doch_h, 2) * 0.18) - 46.33
        zaliczka_podatech_doch_zaokr_j = int(zaliczka_podatek_doch_i) - int(skladka_ubezpieczenie_zdrowotne_f)
        self.netto = self.wyn_brutto - round(skladki_c, 2) - round(skladki_zdrowotne_e, 2) - round(zaliczka_podatech_doch_zaokr_j, 2)
        return round(self.netto, 2)

    def skladki_pracodawcy(self):
        skladki = self.wyn_brutto*0.0976 + self.wyn_brutto*0.065
        skladka_wypad = self.wyn_brutto*0.0193 + self.wyn_brutto*0.0245
        skladka_fgsp = self.wyn_brutto*0.001
        self.skladka_pracodawcy = round(skladki, 2) + round(skladka_wypad,2) + round(skladka_fgsp, 2)
        return round(self.skladka_pracodawcy, 2)

    def laczny_koszt_prac(self):
        return round((self.wyn_brutto + self.skladki_pracodawcy()), 2)


liczba_pracownikow = int(input())
pracownicy = []
for i in range (0, liczba_pracownikow):
    temp = input()
    temp = temp.split()
    imie = temp[0]
    brutto = int(temp[1])
    pracownik = Pracownik(imie, brutto)
    pracownicy.append(pracownik)


laczny_koszt_pracodawcy = 0
for i in range(0, liczba_pracownikow):
    imie = pracownicy[i].imie
    brutto = pracownicy[i].wyn_brutto
    laczny_koszt_pracodawcy += pracownicy[i].laczny_koszt_prac()
    print(imie, f"{pracownicy[i].wynagrodzenie_netto():.2f}",
    f"{pracownicy[i].skladki_pracodawcy():.2f}", 
        f"{pracownicy[i].laczny_koszt_prac():.2f}")
print(laczny_koszt_pracodawcy)