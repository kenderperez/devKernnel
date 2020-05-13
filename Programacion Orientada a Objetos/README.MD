<img src='https://i.imgur.com/gScS6Vz.png'>
<h1 style='color: red'>Programacion Orientada a Objetos con Python</h1><br>
<div style="border: 1px solid red"><p>La programacion orientada a objetos es un paradigma de programacion, En otras palabras
es una forma de resolver problemas siguiendo una metodologia en particular</p></div>
<p>Un objeto contiene propiedades que almacenan valores y metodos que le añaden funcionalidad.
las propiedades de los objetos se separan unas de otras mediante una coma ","
para acceder a las propiedades de un objeto se hace mediante la siguiente sintaxys:
</p>

```python
objeto['propiedad']
objeto.propiedad
```
<p>vamos a ver esto de manera practica para entenderlo meojor.. </p>
<p align="center"><img width='600px' src='https://i.imgur.com/yb7s66g.png'></p>
<p>supongamos que tenemos un objeto
llamado kraken el cual es un mounstruo marino, este objeto contendra propiedades como nombre, tipo,
vida y resistencia y metodos como gruñir(), un metodo es una propiedad que contiene como valor una funcion
para crear dicho objeto escribamos el siguiente codigo:</p>

```python
objeto['propiedad']
objeto.propiedad
```

<p align="center"><img width='600px' src='https://i.imgur.com/eTdtwTP.png'></p>
<p>Una Clase es una plantilla para crear un nuevo objeto donde podemos definir que
propiedades y metodos contendra un objeto .
pensemos en las clases  como plantillas con las que podemos crear uno o varios objetos
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



