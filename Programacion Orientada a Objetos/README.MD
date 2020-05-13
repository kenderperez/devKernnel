<img src='https://i.imgur.com/gScS6Vz.png'>
<h1 style='color: red'>Programacion Orientada a Objetos (POO) con Python</h1><br>

<p>La programacion orientada a objetos es un paradigma de programacion, En otras palabras
es una forma de resolver problemas siguiendo una metodologia en particular en este caso es una forma especial de programar, más cercana a como expresaríamos las cosas en la vida real.
</p>
<p>tenemos que aprender a pensar las cosas de una manera distinta para poder escribir nuestros programas en términos de objetos, propiedades y métodos. La POO tiene como principio que todo en la vida es un objeto programable, entonces para empezar a programar con este paradigma tendríamos que empezar con desarrollar nuestro pensamiento basado en objetos.</p>

<p>Pensar en términos de objetos es pensar de manera natural como lo haríamos en la vida real. 
Un objeto contiene propiedades que almacenan valores y metodos que le añaden funcionalidad.
Por ejemplo al pensar en una espada como un objeto para ser programado diriamos que la espada contiene una serie de caracteristicas, como
podria ser el filo el nombre el daño o el color, Además tiene una serie de funcionalidades o métodos asociados al mismo, como pueden ser cortar, o atacar.
<p>En un esquema POO la espada sería el objeto, las propiedades serían las características como el filo o el daño y los métodos serían las funcionalidades asociadas como cortar o atacar.</p>
<p>vamos a ver esto de manera practica para entenderlo mejor.. </p>
<p align="center"><img width='600px' src='https://i.imgur.com/yb7s66g.png'></p>
<h5><i>como vimos en la imagen de arriba el objeto espada contiene la propiedad daño con un valor de 9 y filo con un valor de 8, tambien se puede apreciar que las propiedades se separan unas de otras por medio de una coma " , ".</i></h5>
<br>
<p>supongamos que tenemos un objeto
llamado kraken el cual es un mounstruo marino, este objeto contendra propiedades como nombre, tipo,
vida y resistencia y metodos como gruñir(), un metodo es una propiedad que contiene como valor una funcion
para crear dicho objeto escribamos el siguiente codigo:</p>
<p align="center"><img width='600px' src='https://i.imgur.com/eTdtwTP.png'></p>
<h5><i>como vimos en la imagen anterior para acceder a una propiedad de un objeto se hace mediante el nombre del objeto seguido por el nombre de la propiedad entre corchetes [] ejemplo: Kraken['vida'] esto retornara 12</i></h5>


```python
Kraken = {
          'nombre' = 'Kraken',
          'tipo' = 'marino',
          'vida' = 12,
          'resistencia' = 2.
          'gruñir' = def():
                          print('grrrr!')
         }
```


<h1>Clases en POO</h1><br>
<p>Una Clase es una plantilla para crear un nuevo objeto donde podemos definir que
propiedades y metodos contendra un objeto .</p>
<p>pensemos en las clases  como plantillas con las que podemos crear uno o varios objetos
que tendran mas o menos la misma estructura. en el siguiente ejemplo crearemos una plantilla para crear
espadas las cuales contendran propiedades tales como nombre, rareza, daño, filo y un metodo
llamado atacar() el cual restara vida a un objetivo dado:</p>

<p align="center"><img width='600px' src='https://i.imgur.com/oydQAAn.png'></p>
<p>Ahora Podremos crear tantas espadas como queramos!!! y definir su daño, filo ,nombre 
y rareza asi que manos a la obra!
A continuacion vamos a ver como crear objetos a partir de una clase:</p>
<p align="center"><img width='600px' src='https://i.imgur.com/8UkUbRu.png'></p>
<p>en la imagen que acabamos de ver se instancian dos objetos de la
clase Espada llamados espadaVikinga y espadaHeroica en otras palabras
se crean dos objetos con la plantilla Espada, y tan solo usando dos lineas de codigo!!
y es que el objetivo de las clases es ayudar a reducir el codigo.
cada vez que se ejecute la linea espadaVikinga.atacar(Kraken) se le restan 6 puntos 
de vida al krakeny el filo de la espada vikinga disminuye 2 puntos y cuando
el filo de la espada sea 0 o menos de 0 ya atacar() no causara daño alguno al kraken</p>



