class GTAV:
    def __init__(self, modoHistoria):
        self.modoHistoria = modoHistoria
    

Franklin = GTAV("Misión en modo historia de asaltar un barco")
ChavezSV = GTAV("Misión de crear una organización")

class Jugador1(GTAV):
    pass
    def jugar():
        return 'Iniciar {}'.format(Franklin.modoHistoria)
    
class Jugador2(GTAV):
    pass
    def jugar():
        return 'Iniciar {}'.format(ChavezSV.modoHistoria)
    
JugadorF = Jugador1
JugadorC = Jugador2
print(JugadorF.jugar())
print(JugadorC.jugar())