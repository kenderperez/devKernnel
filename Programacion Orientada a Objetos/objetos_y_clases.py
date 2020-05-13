#Creamos la Clase Espada
class Espada:
    def __init__(self, nombre, rareza, daño, filo):
        self.nombre = nombre
        self.rareza = rareza
        self.daño = daño
        self.filo = filo
        
    def atacar(self, objetivo):
        if self.filo > 0 and objetivo['vida'] > 0:
            objetivo['vida'] = objetivo['vida'] - self.daño + objetivo['resistencia']
            self.filo = self.filo - 2
        elif objetivo['vida'] <= 0:
            print('El '+ objetivo['nombre'] + ' a muerto!')
        else:
            print('La espada se a quedado sin filo!!')
            
#Creamos al kraken           
kraken = {
          'nombre' : 'Kraken',
          'tipo' : 'marino',
          'vida' : 12,
          'resistencia' : 2
         }
#Creamos una espada llamada Espada Vikinga a partir de la clase Espada a la cual le asignamos 6 puntos de daño y 7 de filo
espadaVikinga = Espada('Espada Vikinga', 'comun', 6, 7)

#Imprimimos la vida del kraken
print(kraken['vida'])

#Atacamos al kraken
espadaVikinga.atacar(kraken)

#Vemos la vida del Kraken despues de atacarlo
print(kraken['vida'])
