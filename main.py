import os
import pickle
import logging

#logeris
def create_logger(logger_name, log_file):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('TIME: %(asctime)s - NAME: %(name)s - LINE: %(lineno)d - LEVEL: %(levelname)s - MESSAGE: %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

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

    def meniu(self): 
        while True:
            os.system('cls')
            print("-Programa Biudzetas-")
            print("------- Meniu -------\n")
            print("1: Ataskaita")
            print("2: Balansas")
            print("3: Pajamu israsas")
            print("4: Islaidu israsas")
            print("0: Uzdaryti programa")
            try:
                choice = input("Iveskite savo pasirinkimą (0-4): ")
            except Exception as e:
                mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                pass
            os.system('cls')
            if choice == "1":
                try:
                    self.ataskaita()
                    input("press any key")
                except Exception as e:
                    mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                    pass

            elif choice == "2":
                try:
                    self.balansas()
                    input("press any key")
                except Exception as e:
                    mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                    pass

            elif choice == "3":
                try:
                    self.sukurti_pajamu_irasa()
                    input("press any key")
                except Exception as e:
                    mano_logeris.info(f"Klaida bandant sukurti pajamu irasa: {e.__class__.__name__}, {e.with_traceback(None)}")
                    pass

            elif choice == "4":
                try:
                    self.sukurti_islaidu_irasa()
                    input("press any key")
                except Exception as e:
                    mano_logeris.info(f"Klaida bandant sukurti islaidu irasa: {e.__class__.__name__}, {e.with_traceback(None)}")
                    pass

            elif choice == "0":
                print('------- Gražios dienos! -------')
                try:
                    with open("biudzetas.p", 'wb') as pkl_file:
                        pickle.dump(biudzetas.__zurnalas, pkl_file)
                        mano_logeris.info("-----Exit-----")
                        break
                except Exception as e:
                    mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                    pass

    def ataskaita(self):
        """
        surenka israsu objektus is biudzeto zurnalo.

        return: atiduoda suformatuota str( Israsas(pajamos, islaidos), Israso(siuntejas, gavejas), Israso(suma))
        return: total_suma kiek pajamu, kiek islaidu is viso
        """
        mano_logeris.info(f"-----Ataskaita-----")
        for elm in self.__zurnalas:
            if isinstance(elm, Pajamos):
                print(f"Pajamos, Suma: {elm.get_suma()}, siuntejas: {elm.siuntejas}, komentaras: {elm.komentaras}")
                mano_logeris.info(f"Pajamos, Suma: {elm.get_suma()}, siuntejas: {elm.siuntejas}, komentaras: {elm.komentaras}")
                continue
            if isinstance(elm, Islaidos):
                print(f"Islaidos, Suma: {elm.get_suma()}, gavejas: {elm.gavejas}, komentaras: {elm.komentaras}")
                mano_logeris.info(f"Islaidos, Suma: {elm.get_suma()}, gavejas: {elm.gavejas}, komentaras: {elm.komentaras}")
                continue
        mano_logeris.info(f"-----Ataskaitos Pabaiga-----")

    def balansas(self):
        """
        skaiciuoja israsu sumas, biudzeto zurnale

        return: pajamu sumos + islaidu sumos,
        """
        print(f"Total: {self.__total}, Islaidos: {self.__islaidos}, Pajamos: {self.__pajamos}")
        mano_logeris.info(f"Atidarytas balansas: Total: {self.__total}, Islaidos: {self.__islaidos}, Pajamos: {self.__pajamos}")

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
        except Exception as e:
                mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                pass
        finally:
            pajamu_irasas.main(set_suma)
            self.__pajamos += pajamu_irasas.get_suma()
            self.__total += pajamu_irasas.get_suma()
            self.__zurnalas.append(pajamu_irasas)
            mano_logeris.info(f"Islaidu irasas: suma - {pajamu_irasas.get_suma()}, siuntejas - {pajamu_irasas.siuntejas}, komentaras - {pajamu_irasas.komentaras}")

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
        except Exception as e:
                mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                pass
        else:
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

#belekas delevop

#Belekas

#develop
       




# Pagrindinis meniu: ataskaita, balansas, pajamu israsas, islaidu israsas. Biudzetas: islaidu ir pajamu zurnalas.
if __name__ == '__main__':
    try:
        mano_logeris = create_logger("mano_logeris", 'logeris.log')
        mano_logeris.info("-----Start-----")
        biudzetas = Biudzetas()
        biudzetas.meniu()
    except Exception as e:
        mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")

with open("biudzetas.p", 'rb') as read_pkl:
    file_data = pickle.load(read_pkl)
print(file_data)
