import os

class Irasas():
    def __init__(self) -> None:
        self.__suma: float = 0
        self.komentaras: str = ''


class Islaidos(Irasas):
    def __init__(self) -> None:
        super().__init__()
        self.__suma: float = 0
        self.gavejas: str = None

    def __sub_suma(self, suma: float) -> float:
        self.__suma -= abs(self.__suma - suma)

    def main(self, suma):
        self.komentaras = input("Komentaras: ")
        self.gavejas = input("set gavejas: ")
        # try:
        #     set_suma = float(input("set suma: "))
        # except:
        #     print("NAN")
        self.__sub_suma(suma)
        return self
    
    def get_suma(self):
        return self.__suma
    
    def __str__(self):
        return f"Siuntejas: {self.gavejas}. Komentaras {self.komentaras}. Suma: {self.get_suma()}" #{"Tipas": "Islaidos", "Suma": self.get_suma(), "Gavejas": self.gavejas,  "Komentaras": self.komentaras}


class Pajamos(Irasas):
    def __init__(self) -> None:
        super().__init__()
        self.__suma: float = 0
        self.siuntejas: str = None

    def __add_suma(self, suma: float) -> float:
        self.__suma = abs(self.__suma + suma)

    def main(self, suma):
        self.komentaras = input("Komentaras: ")
        self.siuntejas = input("set siuntejas: ")

        self.__add_suma(suma)
        return self
    
    def get_suma(self):
        return self.__suma
    
    def __str__(self) -> dict:
        return f"Siuntejas: {self.siuntejas}. Komentaras {self.komentaras}. Suma: {self.get_suma()}" #{"Tipas": "Pajamos", "Suma": self.get_suma(), "Siuntejas": self.siuntejas, "Komentaras": self.komentaras}


class Biudzetas():
    def __init__(self) -> None:
        self.__zurnalas: list = []
        self.__total = 0
        self.__islaidos = 0
        self.__pajamos = 0

    def ataskaita(self):
        """
        surenka israsu objektus is biudzeto zurnalo.

        return: atiduoda suformatuota str( Israsas(pajamos, islaidos), Israso(siuntejas, gavejas), Israso(suma))
        return: total_suma kiek pajamu, kiek islaidu is viso
        """
        for elm in self.__zurnalas:
            if isinstance(elm, Pajamos):
                # self.__pajamos += elm.get_suma()
                # self.__total += elm.get_suma()
                print(f"Pajamos, {elm.get_suma()}, {elm.siuntejas}, {elm.komentaras}")
                continue
            if isinstance(elm, Islaidos):
                # self.__islaidos -= elm.get_suma()
                # self.__total -= elm.get_suma()
                print(f"Islaidos, {elm.get_suma()}, {elm.gavejas}, {elm.komentaras}")
                continue

            # try:
            #         print(f"Pajamos, {elm.get_suma()}, {elm.siuntejas}, {elm.komentaras}")
            # except:
            #     if isinstance(elm, Islaidos):
            #         print(f"Pajamos, {elm.get_suma()}, {elm.gavejas}, {elm.komentaras}")
            # continue


    def balansas(self):
        """
        skaiciuoja israsu sumas, biudzeto zurnale

        return: pajamu sumos + islaidu sumos,
        """
        print(f"Total: {self.__total}, Islaidos: {self.__islaidos}, Pajamos: {self.__pajamos}")


    def sukurti_pajamu_irasa(self):
        """
        sukuria pajamu irasa, 

        argumentai:
        Pajamos klases objektas

        return: pajamos.suma, pajamos.siuntejas
        """
        pajamu_irasas = Pajamos()
        try:
            set_suma = float(input("set suma: "))
        except:
            print("NAN")
        finally:
            pajamu_irasas.main(set_suma)
            self.__pajamos += pajamu_irasas.get_suma()
            self.__total += pajamu_irasas.get_suma()

            self.__zurnalas.append(pajamu_irasas)


    def sukurti_islaidu_irasa(self):
        """
        sukuria islaidu irasa, 

        argumentai:
        Islaidos klases objektas

        return: Biudzetas.zurnalas.update({obj.siuntejas: obj.suma})
        """
        islaidu_irasas = Islaidos()
        islaidu_irasas.__suma = 155

        try:
            set_suma = float(input("set suma: "))
        except:
            print("NAN")
        finally:
            islaidu_irasas.main(set_suma)
            self.__islaidos += islaidu_irasas.get_suma()
            self.__total += islaidu_irasas.get_suma()

            self.__zurnalas.append(islaidu_irasas)

# Pagrindinis meniu: ataskaita, balansas, pajamu israsas, islaidu israsas. Biudzetas: islaidu ir pajamu zurnalas.
biudzetas = Biudzetas()
biudzetas.__total = 12
biudzetas.__islaidos = 150
biudzetas.__pajamos = 155



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

#Belekas
       


    