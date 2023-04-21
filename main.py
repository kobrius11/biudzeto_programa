import os

class Irasas():
    def __init__(self) -> None:
        self.__suma: float = 0
        self.komentaras: str = ''


class Islaidos(Irasas):
    def __init__(self) -> None:
        super().__init__()
        self.gavejas: str = None

    def __sub_suma(self, suma: float, gavejas: str) -> float:
        temp = abs(self.__suma - suma)
        self.__suma -= temp

    def main(self):
        set_gavejas = input("set gavejas: ")
        try:
            set_suma = float(input("set suma: "))
        except:
            print("NAN")
        else:
            self.__sub_suma(set_suma, set_gavejas)
            return self.__str__(self)
    
    def get_suma(self):
        return self.__suma
    
    def __str__(self):
        return {"Tipas": "Islaidos", "Suma": self.get_suma(), "Gavejas": self.gavejas}





class Pajamos(Irasas):
    def __init__(self) -> None:
        super().__init__()
        self.siuntejas: str = None

    def __add_suma(self, suma: float, siuntejas: str) -> float:
        self.__suma = abs(self.__suma + suma)

    def main(self):
        set_siuntejas = input("set gavejas: ")
        set_komentaras = input("Komentaras")
        try:
            set_suma = float(input("set suma: "))
        except:
            print("NAN")
        else:
            self.__add_suma(set_suma, set_siuntejas)
            return self.__str__(self)
    
    def get_suma(self):
        return self.__suma
    
    def __str__(self) -> dict:
        return {"Tipas": "Pajamos", "Suma": self.get_suma(), "Gavejas": self.siuntejas, "Komentaras": self.komentaras}


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
            for el in elm:
                if el == "Pajamos":
                    self.pajamos += elm["Suma"]
                    self.total += elm["Suma"]
                if el == "Islaidos":
                    self.islaidos += elm["Suma"]
                    self.total -= elm["Suma"]
            try:
                print(f"{elm['Tipas']}, {elm['Suma']}, {elm['Siuntejas']}, {elm['Komentaras']}")
            except:
                print(f"{elm['Tipas']}, {elm['Suma']}, {elm['Gavejas']}, {elm['Komentaras']}")
            continue


           

    def balansas(self):
        """
        skaiciuoja israsu sumas, biudzeto zurnale

        return: pajamu sumos + islaidu sumos,
        """
        self.ataskaita()
        return self.total


    def sukurti_pajamu_irasa(self):
        """
        sukuria pajamu irasa, 

        argumentai:
        Pajamos klases objektas

        return: pajamos.suma, pajamos.siuntejas
        """
        pajamu_irasas = Pajamos()
        self.zurnalas.append(pajamu_irasas.main())


    def sukurti_islaidu_irasa(self):
        """
        sukuria islaidu irasa, 

        argumentai:
        Islaidos klases objektas

        return: Biudzetas.zurnalas.update({obj.siuntejas: obj.suma})
        """
        islaidu_irasas = Islaidos()
        self.zurnalas.append(islaidu_irasas.main())




# Pagrindinis meniu: ataskaita, balansas, pajamu israsas, islaidu israsas. Biudzetas: islaidu ir pajamu zurnalas.

biudzetas = Biudzetas()

# Pagrindinis meniu: ataskaita, balansas, pajamu israsas, islaidu israsas
  

    
while True:
    print("-Programa Biudzetas-")
    print("------- Meniu -------\n")
    print("1: Ataskaita")
    print("2: Balansas")
    print("3: Pajamu israsas")
    print("4: Islaidu israsas")
    print("0: Uzdaryti programa")
    choice = input("Iveskite savo pasirinkimą (0-4): ")
    
    if choice == "1":
        os.system('cls')
        biudzetas.ataskaita()
        input()


    elif choice == "2":
        os.system('cls')
        biudzetas.balansas()

        input()


    elif choice == "3":
        os.system('cls')
        biudzetas.sukurti_pajamu_irasa()

        input()


    elif choice == "4":
        os.system('cls')
        biudzetas.sukurti_islaidu_irasa()
        input()


    elif choice == "0":
        os.system('cls')
        print('------- Gražios dienos! -------')
        break

       


    