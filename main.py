import os

class Irasas():
    def __init__(self) -> None:
        self.__suma: float = 0
        self.komentaras: str = ''


class Islaidos(Irasas):
    def __init__(self) -> None:
        super().__init__()
        self.gavejas: str = None

    def __sub_suma(self, suma: float) -> float:
        self.__suma -= abs(self.__suma - suma)

    def main(self):
        self.komentaras = input("Komentaras: ")
        self.gavejas = input("set gavejas: ")
        try:
            set_suma = float(input("set suma: "))
        except:
            print("NAN")
        else:
            self.__sub_suma(set_suma)
            return self
    
    def get_suma(self):
        return self.__suma
    
    def __str__(self):
        return f"Siuntejas: {self.gavejas}. Komentaras {self.komentaras}. Suma: {self.get_suma()}" #{"Tipas": "Islaidos", "Suma": self.get_suma(), "Gavejas": self.gavejas,  "Komentaras": self.komentaras}


class Pajamos(Irasas):
    def __init__(self) -> None:
        super().__init__()
        self.siuntejas: str = None

    def __add_suma(self, suma: float) -> float:
        self.__suma = abs(self.__suma + suma)

    def main(self):
        self.komentaras = input("Komentaras: ")
        self.siuntejas = input("set siuntejas: ")
        try:
            set_suma = float(input("set suma: "))
        except:
            print("NAN")
        else:
            self.__add_suma(set_suma)
            return self
    
    def get_suma(self):
        return self.__suma
    
    def __str__(self) -> dict:
        return f"Siuntejas: {self.siuntejas}. Komentaras {self.komentaras}. Suma: {self.get_suma()}" #{"Tipas": "Pajamos", "Suma": self.get_suma(), "Siuntejas": self.siuntejas, "Komentaras": self.komentaras}


class Biudzetas():
    def __init__(self) -> None:
        self.zurnalas: list = []
        self.total = 0
        self.islaidos = 0
        self.pajamos = 0

    def ataskaita(self):
        """
        surenka israsu objektus is biudzeto zurnalo.

        return: atiduoda suformatuota str( Israsas(pajamos, islaidos), Israso(siuntejas, gavejas), Israso(suma))
        return: total_suma kiek pajamu, kiek islaidu is viso
        """
        for elm in self.zurnalas:
            if isinstance(elm, Pajamos):
                self.pajamos += elm.get_suma()
                self.total += elm.get_suma()
            if isinstance(elm, Islaidos):
                self.islaidos += elm.get_suma()
                self.total += elm.get_suma()

            try:
                print(f"Pajamos, {elm.get_suma()}, {elm.siuntejas}, {elm.komentaras}")
            except:
                print(f"Pajamos, {elm.get_suma()}, {elm.gavejas}, {elm.komentaras}")
            continue


    def balansas(self):
        """
        skaiciuoja israsu sumas, biudzeto zurnale

        return: pajamu sumos + islaidu sumos,
        """
        print(f"Total: {self.total}, Islaidos: {self.islaidos}, Pajamos: {self.pajamos}")


    def sukurti_pajamu_irasa(self):
        """
        sukuria pajamu irasa, 

        argumentai:
        Pajamos klases objektas

        return: pajamos.suma, pajamos.siuntejas
        """
        pajamu_irasas = Pajamos()
        pajamu_irasas.main()
        self.zurnalas.append(pajamu_irasas)


    def sukurti_islaidu_irasa(self):
        """
        sukuria islaidu irasa, 

        argumentai:
        Islaidos klases objektas

        return: Biudzetas.zurnalas.update({obj.siuntejas: obj.suma})
        """
        islaidu_irasas = Islaidos()
        islaidu_irasas.main()
        self.zurnalas.append(islaidu_irasas)

# Pagrindinis meniu: ataskaita, balansas, pajamu israsas, islaidu israsas. Biudzetas: islaidu ir pajamu zurnalas.
biudzetas = Biudzetas()

# Pagrindinis meniu: ataskaita, balansas, pajamu israsas, islaidu israsas  
while True:
    os.system('cls')
    print("-Programa Biudzetas-")
    print("------- Meniu -------\n")
    print("1: Ataskaita")
    print("2: Balansas")
    print("3: Pajamu israsas")
    print("4: Islaidu israsas")
    print("0: Uzdaryti programa")
    choice = input("Iveskite savo pasirinkimą (0-4): ")
    os.system('cls')
    if choice == "1":
        biudzetas.ataskaita()
        input("press any key")

    elif choice == "2":
        biudzetas.balansas()
        input("press any key")

    elif choice == "3":
        biudzetas.sukurti_pajamu_irasa()
        input("press any key")

    elif choice == "4":
        biudzetas.sukurti_islaidu_irasa()
        input("press any key")

    elif choice == "0":
        print('------- Gražios dienos! -------')
        break

       


    