class Irasas():
    def __init__(self) -> None:
        self.__suma: float = 0
        self.komentaras: str = ''

    def __add_suma(self, suma):
        pass

    def __sub_suma(self, suma):
        pass
    



class Islaidos(Irasas):
    def __init__(self, gavejas) -> None:
        super().__init__()
        self.gavejas: str = gavejas

    def __sub_suma(self, suma: float, gavejas: str) -> float:
        super().__sub_suma()





class Pajamos(Irasas):
    def __init__(self, siuntejas) -> None:
        super().__init__()
        self.siuntejas: str = siuntejas

    def __add_suma(self, suma: float, siuntejas: str) -> float:
        super().__add_suma()





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








































# Pagrindinis meniu: ataskaita, balansas, pajamu israsas, islaidu israsas. Biudzetas: islaidu ir pajamu zurnalas.
import.os
biudzetas = Biudzetas()
    
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


    elif choice == "2":
        os.system('cls')


    elif choice == "3":
        os.system('cls')


    elif choice == "4":
        os.system('cls')


    elif choice == "0":
        os.system('cls')
        print('------- Gražios dienos! -------')
        break

       


    