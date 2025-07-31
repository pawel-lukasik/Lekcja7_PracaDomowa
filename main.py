# Funkcje, obiekty, PEP
#
# Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.
# Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.
#
# Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
# Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
# Polecenie "koniec" - Kończy działanie aplikacji.
#
# Proces tworzenia użytkowników:
# Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
# Polecenie "koniec" - Wraca do pierwszego menu.
#
# Proces zarządzania użytkownikami:
# Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
# Polecenie "koniec" - Wraca do pierwszego menu.


class Uczen:
    def __init__(self, imie_i_nazwisko, klasa):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.klasa = klasa

    def __str__(self):
        return f"Uczeń: {self.imie_i_nazwisko}, klasa: {self.klasa}"

class Nauczyciel:
    def __init__(self, imie_i_nazwisko, przedmiot, klasy):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy

    def __str__(self):
        return f"Nauczyciel: {self.imie_i_nazwisko}, Przedmiot: {self.przedmiot}, Klasy: {self.klasy}"

class Wychowawca:
    def __init__(self, imie_i_nazwisko, klasa):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.klasa = klasa

    def __str__(self):
        return f"Wychowawca: {self.imie_i_nazwisko}, Wychowawca klasy: {self.klasa}"

uczniowie = [
    Uczen("ADAM MAŁYSZ", "1A"),
    Uczen("KAMIL STOCH", "1A"),
    Uczen("IGA ŚWIĄTEK", "2B"),
    Uczen("AGNIESZKA RADWAŃSKA", "2B"),
    Uczen("BARTOSZ KUREK", "3C"),
    Uczen("MARIUSZ WLAZŁY", "3C")
]

nauczyciele = [
    Nauczyciel("ANNA STĘPNIKOWSKA", "Biologia", ["1A", "2B", "3C"]),
    Nauczyciel("IRENA KAŃTOCH", "Język polski", ["1A", "2B", "3C"]),
    Nauczyciel("BEATA WLAŹ", "Matematyka", ["1A", "2B", "3C"]),
    Nauczyciel("JERZY TESARCZYK", "Historia", ["1A", "2B", "3C"])
]

wychowawcy = [
    Wychowawca("ADAM WÓJCIK", "1A"),
    Wychowawca("JAN KOWALSKI", "2B"),
    Wychowawca("STANISŁAW NOWAK", "3C")
]

def wczytaj_ucznia():
    imie_i_nazwisko = input("Podaj imię i nazwisko ucznia: ").upper()
    klasa = input("Podaj klasę ucznia: ").upper()

    nowy_uczen = Uczen(imie_i_nazwisko, klasa)
    return nowy_uczen

def wczytaj_nauczyciela():
    imie_i_nazwisko = input("Podaj imię i nazwisko nauczyciela: ").upper()
    przedmiot = input("Podaj przedmiot, który prowadzi: ").upper()
    klasy = list()
    while True:
        klasa = input("Podaj klasę, którą prowadzi nauczyciel i naciśnij ENTER (jeśli podałeś już wszystkie naciśnij sam ENTER): ")
        if not klasa:
            break
        else:
            klasy.append(klasa)

    nowy_nauczyciel = Nauczyciel(imie_i_nazwisko, przedmiot, klasy)
    return nowy_nauczyciel

def wczytaj_wychowawce():
    imie_i_nazwisko = input("Podaj imię i nazwisko wychowawcy: ").upper()
    klasa = input("Podaj klasę, którą prowadzi: ").upper()

    nowy_wychowawca = Wychowawca(imie_i_nazwisko, klasa)
    return nowy_wychowawca

def linia_oddzielająca(znak="_", liczba=90):
    print(znak * liczba)

while True:
    linia_oddzielająca()
    akcja = input("Zarządzanie bazą szkolną. Wpisz komendę [utwórz, zarządzaj, koniec]: ").upper()

    if akcja == "KONIEC":

        print("Koniec programu.")
        break

    elif akcja == "LISTA":
        print("Uczniowie:")
        for uczen in uczniowie:
            print(uczen)

        print("Nauczyciele:")
        for nauczyciel in nauczyciele:
            print(nauczyciel)

        print("Wychowawcy:")
        for wychowawca in wychowawcy:
            print(wychowawca)

    elif akcja == "UTWÓRZ":
        linia_oddzielająca()
        while True:
            akcja2 = input("TWORZENIE UŻYTKOWNIKA -> Wpisz nazwę nowego użytkownika [uczeń, nauczyciel, wychowawca, koniec]: ").upper()

            if akcja2 == "KONIEC":
                break

            elif akcja2 == "UCZEŃ":
                nowy_uczen = wczytaj_ucznia()
                uczniowie.append(nowy_uczen)
                print("UCZEŃ DODANY!")
                linia_oddzielająca()

            elif akcja2 == "NAUCZYCIEL":
                nowy_nauczyciel = wczytaj_nauczyciela()
                nauczyciele.append(nowy_nauczyciel)
                print("NAUCZYCIEL DODANY!")
                linia_oddzielająca()

            elif akcja2 == "WYCHOWAWCA":
                nowy_wychowawca = wczytaj_wychowawce()
                wychowawcy.append(nowy_wychowawca)
                print("WYCHOWAWCA DODANY!")
                linia_oddzielająca()

            else:
                print(f"Błędna komenda '{akcja2}'")
                linia_oddzielająca()

    elif akcja == "ZARZĄDZAJ":
        while True:
            akcja2 = input("ZARZĄDZANIE -> Wpisz komendę [klasa, uczeń, nauczyciel, wychowawca, koniec]: ").upper()

            if akcja2 == "KONIEC":
                break

            elif akcja2 == "KLASA":
                klasa = input("Podaj klasę, którą chcesz wyświetlić: ").upper()
                czy_jest_taki = False
                for uczen in uczniowie:
                    if uczen.klasa == klasa:
                        czy_jest_taki = True
                        print(uczen)
                for wychowawca in wychowawcy:
                    if wychowawca.klasa == klasa:
                         print(f"Wychowawcą klasy {klasa} jest: {wychowawca.imie_i_nazwisko}")
                if czy_jest_taki == False:
                    print("Nie ma takiej klasy w naszej bazie.")
                linia_oddzielająca()

            elif akcja2 == "UCZEŃ":
                szukany_uczen = input("Podaj imię i nazwisko ucznia, którego chcesz wyświetlić: ").upper()
                czy_jest_taki = False
                for uczen in uczniowie:
                    if uczen.imie_i_nazwisko == szukany_uczen:
                        czy_jest_taki = True
                        print(uczen)
                        print(f"Przedmioty, na które uczęszcza:")
                        for nauczyciel in nauczyciele:
                            if uczen.klasa in nauczyciel.klasy:
                                print(f"{nauczyciel.przedmiot}, prowadzony przez {nauczyciel.imie_i_nazwisko}")
                                linia_oddzielająca()
                if czy_jest_taki == False:
                    print("Nie ma takieo ucznia w naszej bazie.")
                    linia_oddzielająca()


            elif akcja2 == "NAUCZYCIEL":
                szukany_nauczyciel = input("Podaj imię i nazwisko nauczyciela, którego chcesz wyświetlić: ").upper()
                czy_jest_taki = False
                for nauczyciel in nauczyciele:
                    if nauczyciel.imie_i_nazwisko == szukany_nauczyciel:
                        czy_jest_taki = True
                        print(f"Nauczyciel: {nauczyciel.imie_i_nazwisko} prowadzi klasy: {nauczyciel.klasy}")
                        linia_oddzielająca()
                if czy_jest_taki == False:
                    print("Nie ma takiego nauczyciela w naszej bazie.")
                    linia_oddzielająca()

            elif akcja2 == "WYCHOWAWCA":
                szukany_wychowawca = input("Podaj imię i nazwisko wychowawcy, którego chcesz wyświetlić: ").upper()
                czy_jest_taki = False
                for wychowawca in wychowawcy:
                    if wychowawca.imie_i_nazwisko == szukany_wychowawca:
                        czy_jest_taki = True
                        print(f"Wychowawca {wychowawca.imie_i_nazwisko} prowadzi klasę {wychowawca.klasa}:")
                        for uczen in uczniowie:
                            if uczen.klasa == wychowawca.klasa:
                                print(uczen.imie_i_nazwisko)

                if czy_jest_taki == False:
                    print("Nie ma takiego wychowawcy w naszej bazie.")
                linia_oddzielająca()

            else:
                print(f"Błędna komenda '{akcja2}'")

    else:
        print(f"Błędna komenda '{akcja}'")