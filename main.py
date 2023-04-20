class Irasas():
    def __init__(self):
        self.suma: float = 0
        self.komentaras: str = ''

class Islaidos(Irasas):
    def __init__(self, gavejas):
        super().__init__()
        self.gavejas: str = gavejas

class Pajamos(Irasas):
    def __init__(self, siuntejas):
        super().__init__()
        self.siuntejas: str = siuntejas

class Biudzetas():
    def __init__(self):
        self.zurnalas: list = []

    def ataskaita(self):
        pass

    def balansas(self):
        pass

    def sukurti_pajamu_irasa(self, obj: Pajamos.obj):
        pass

    def sukurti_islaidu_irasa(self, obj: Islaidos.obj):
        pass



