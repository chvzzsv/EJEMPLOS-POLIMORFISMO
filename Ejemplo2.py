class Salida:
    def __init__(self, nombreLugar):
        self.nombreLugar = nombreLugar
    

Metrocentro = Salida("a comprar comida")
GardenMall = Salida("a pasear en familia")

class Parte1(Salida):
    pass
    def salir():
        return 'Estamos planeando ir metro {}'.format(Metrocentro.nombreLugar)
    
class Parte2(Salida):
    pass
    def salir():
        return 'Estamos planeando ir al garden {}'.format(GardenMall.nombreLugar)
    
Lugar1 = Parte1
Lugar2 = Parte2
print(Lugar1.salir())
print(Lugar2.salir())