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
        self.suma = abs(self.__suma + suma)

    def main(self):
        set_siuntejas = input("set gavejas: ")
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
        return {"Tipas": "Pajamos", "Suma": self.get_suma(), "Gavejas": self.siuntejas}


class Biudzetas():
    def __init__(self) -> None:
        self.zurnalas: list = []

    def ataskaita(self):
        """
        surenka israsu objektus is biudzeto zurnalo.

        return: atiduoda suformatuota str( Israsas(pajamos, islaidos), Israso(siuntejas, gavejas), Israso(suma))
        return: total_suma kiek pajamu, kiek islaidu is viso
        """
        pass

    def balansas(self):
        """
        skaiciuoja israsu sumas, biudzeto zurnale

        return: pajamu sumos + islaidu sumos,
        """
        pass


    def sukurti_pajamu_irasa(self, obj: Pajamos.obj):
        """
        sukuria pajamu irasa, 

        argumentai:
        Pajamos klases objektas

        return: pajamos.suma, pajamos.siuntejas
        """
        pass

    def sukurti_islaidu_irasa(self, obj: Islaidos.obj):
        """
        sukuria islaidu irasa, 

        argumentai:
        Islaidos klases objektas

        return: Biudzetas.zurnalas.update({obj.siuntejas: obj.suma})
        """
        pass



# Pagrindinis meniu: ataskaita, balansas, pajamu israsas, islaidu israsas
  
    
    print("-Programa Biudzetas-")
    print("------- Meniu -------\n")
    print("1: Ataskaita")
    print("2: Balansas")
    print("3: Pajamu israsas")
    print("4: Islaidu israsas")
    print("0: Uzdaryti programa")