<img src='https://i.imgur.com/gScS6Vz.png'>
<h1 style='color: red'>Programacion Orientada a Objetos (POO) con Python</h1><br>

<p>La programacion orientada a objetos es un paradigma de programacion, en otras palabras
es una forma de resolver problemas siguiendo una metodologia en particular, en este caso es una forma especial de programar, más cercana a como expresaríamos las cosas en la vida real.
</p>
<p>Tenemos que aprender a pensar las cosas de una manera distinta para poder escribir nuestros programas en términos de objetos, propiedades y métodos; la POO tiene como principio que todo en la vida es un objeto programable, entonces para empezar a programar con este paradigma, tendríamos que empezar con desarrollar nuestro pensamiento basado en objetos.</p>

<p>Pensar en términos de objetos es pensar de manera natural como lo haríamos en la vida real. 
Un objeto contiene propiedades que almacenan valores y metodos que le añaden funcionalidad.
Por ejemplo: <br>al pensar en una espada como un objeto para ser programado, diriamos que la espada contiene una serie de caracteristicas, como
podria ser el filo, el nombre, el daño o el color; además tiene una serie de funcionalidades o métodos asociados al mismo, como pueden ser: cortar o atacar.
<p>En un esquema POO la espada sería el objeto, las propiedades serían las características como el filo o el daño y los métodos serían las funcionalidades asociadas como cortar o atacar.</p>
<p>vamos a ver esto de manera practica para entenderlo mejor.. </p>
<p align="center"><img width='600px' src='https://i.imgur.com/qzHzrNa.png'></p>


> *como vimos en la imagen de arriba el objeto espada contiene la propiedad daño con un valor de 9 y filo con un valor de 8, tambien se puede apreciar que las propiedades se separan unas de otras por medio de una coma ",".


<br>
<p> Ahora supongamos que tenemos un objeto
llamado kraken 🦑 el cual es un mounstruo marino, este objeto contendra propiedades como nombre, tipo,
vida y resistencia.
para crear dicho objeto escribamos el siguiente codigo:</p>
<p align="center"><img width='600px' src='https://i.imgur.com/zYo2yq4.png'></p>



> *como vimos en la imagen anterior, para acceder a una propiedad de un objeto se hace mediante el nombre del objeto seguido por el nombre de la propiedad entre corchetes [] ejemplo: Kraken['vida'] esto retornara 12



<details>
  <summary>👀 Haz click aquí para ver el codigo</summary>


```python
kraken = {
          'nombre' : 'Kraken',
          'tipo' : 'marino',
          'vida' : 12,
          'resistencia' : 2
         }
```
 

</details>


<h1>Clases en POO</h1><br>
<p>Ahora que ya sabemos crear un objeto de manera estática veamos como crearlo a partir de una plantilla o clase</p>
<p>Una Clase es una plantilla para crear un nuevo objeto donde podemos definir que
propiedades y metodos contendra el objeto .</p>
<p>Pensemos en las clases  como plantillas con las que podemos crear uno o varios objetos
que tendran más o menos la misma estructura. En el siguiente ejemplo crearemos una plantilla para crear
espadas las cuales contendran propiedades tales como nombre, rareza, daño, filo y un metodo
llamado atacar() el cual restara vida a un objetivo dado:</p>
<p align="center"><img width='600px' src='https://i.imgur.com/obI3vrP.png'></p>


<details>
  <summary>👀 Haz click aquí para ver el codigo</summary>


```python
class Espada:
    def __init__(self, nombre, rareza, daño, filo):
        self.nombre = nombre
        self.rareza = rareza
        self.daño = daño
        self.filo = filo
        
    def atacar(self, objetivo):
        if self.filo > 0 and objetivo['vida'] > 0: #si la espada tiene filo suficiente y el objetivo esta vivo la espada atacara
             #se le restaran los puntos de daño de la espada a la vida del objetivo y se le sumara la resistencia del objetivo
            objetivo['vida'] = objetivo['vida'] - self.daño + objetivo['resistencia']
            self.filo = self.filo - 2 #Cada vez que la espada ataque perdera 2 puntos de filo
        elif objetivo['vida'] <= 0: #si la vida del objetivo es igual o menor que cero
            print('El '+ objetivo['nombre'] + ' a muerto!')
        else:
            print('La espada se a quedado sin filo!!') #si el filo de la espada llega a cero
```
 

</details>



<p>Ahora Podremos crear tantas espadas como queramos!!! y definir su daño, filo ,nombre 
o rareza asi que manos a la obra!!!<br>
A continuacion vamos a ver como crear objetos a partir de una clase:</p>
<p align="center"><img src='https://i.imgur.com/wFSmLDt.png'></p>
<p>En la imagen que acabamos de ver se instancian dos objetos de la
clase Espada llamados espadaVikinga y espadaHeroica en otras palabras
se crean dos objetos con la plantilla Espada, y tan solo usando dos líneas de código!!
y es que el objetivo de las clases es ayudar a reducir el código.
cada vez que se ejecute la linea espadaVikinga.atacar(kraken) se le restan 6 puntos 
de vida al kraken y el filo de la espada vikinga disminuye 2 puntos, cuando
el filo de la espada sea 0 o menos de 0 ya atacar() no causara daño alguno al kraken</p>
<p align="center"><img src='https://i.imgur.com/YUIntBg.gif'></p>
<h1>La herencia</h1>
<p>
es uno de los fundamentos de la programación orientada a objetos,  Se usa para hacer que una clase hija obtenga o herede todos los elementos (métodos y propiedades) de una clase padre, a partir de esta copia del padre podemos crear nuevos métodos y propiedades, así como mantener, modificar o eliminar los ya existentes que hemos heredado.
</p>
<p>
Uno de los objetivos de la herencia es reducir la cantidad de código, ya que no tenemos que escribir una clase desde cero, si no que podemos reutilizar métodos o atributos definidos ya en otra clase.
</p>
<p>
Ya tenemos una plantilla para crear espadas básicas con los atributos: nombre, rareza, daño y filo, así como un método para atacar a un objetivo, ahora supongamos que queremos crear un tipo especial de espadas que contenga un ataque especial para monstruos de tipo marino, para hacer esto solo tenemos que crear una clase que herede las propiedades y métodos de la clase Espada y luego añadirle la nueva funcionalidad “ataque tsunami”.
</p>
<p align="center"><img src='https://i.imgur.com/tsGBabf.png'></p>



> *la clase EspadaMarina hereda los atributos nombre, rareza, daño, filo y el método atacar() de la clase Espada y luego le agregamos el nuevo método ataqueTsunami().



<p>Como ya hemos venido haciendo vamos a ver esto de manera practica para entender mejor el concepto:</p>
<p align="center"><img width='600px' src='https://i.imgur.com/F6E9B49.png'></p>
<details>
  <summary>👀 Haz click aquí para ver el codigo</summary>


```python
class EspadaMarina(Espada):
	
	def ataqueTsunami(self, objetivo):
		
		if objetivo['tipo'] == 'marino':
			
            objetivo['vida'] = objetivo['vida'] - 10 + objetivo['resistencia']
		else:
			
			print('este ataque solo funciona contra enemigos marinos!!')
```
 

</details>
<p>Ahora ya tenemos una clase nueva para crear espadas con un nuevo tipo de ataque que solo causa daño a enemigos de tipo marino, procedamos a crear dos espadas nuevas</p>
<p align="center"><img width='600px' src='https://i.imgur.com/WFOq2Qe.png'></p>


<hr>
<h1>Quieres apoyarme?</h1>
<noscript><a href="https://liberapay.com/devKernnel/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a></noscript>
<hr>
<p align="center"><a href='https://twitter.com/devKernnel'>❤ si este pequeño tutorial te sirvio de algo sigueme en twitter, estaré creando contenido didáctico todas las semanas ❤</a></p>

