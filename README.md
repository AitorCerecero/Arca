# Arca
Arca Engine to webscrap

 Hola, este es el read me de mi codigo

 Yo se lo que estas pensando, que clase de codigo es este o que es lo que esta haciendo este novato

 Si te soy honesto, es la primera vez que subo algo a GitHub y pense en subir lo que habia hecho ya que creo yo que es un buen trabajo

 Permiteme explicarte 

El objetivo de este codigo (No del repositorio clonado ya que ese ya esta hecho) es enseñarte a usar el web scrapping de una forma facil

Comenzaremos importando los assetes que ocupamos

Ten en cuentas que este archivo esta hecho en python

from bs4 import BeautifulSoup
import requests
import pandas as pd

BeautifulSoup es la extension que nos apoyara al manejo del webscrapping en si
request es la extentsion que manejara el URL del sitio donde estaremos sacando la informacion
pandas es la libreria de alto nivel de manejo de datos numericos

Una vez importado esto podemos empezar 

data = requests.get("https://www.highspeedinternet.com/in/mexico")
print(data.status_code)

data es donde por medio de request estamos pidiendo bajar la informacion del link (el link es totalmente personalizable)
data.status_code es la manera que te avisa la libreria que funcionó la importacion, si obtienes el codigo 200 es que fue un exito, de lo contrario si tienes el codido 403 es que algo falló

xtract = BeautifulSoup(data.content,"html.parser")

xtract es un nombre generico, puedes cambiarlo si quieres. sin embargo lo que corresponde dependera lo que pones, la extension de BS es totalmente necesaria, el data como te puedes dar cuenta es donde pusimos el 
nombre del link

para lo que sigues no podre poner todo, pero sin embargo te explico como se hacer

depende lo que intentes extraer es como manejaras la informacion, si quieres sacar el titulo de los elementos en lista de la pagina, has de poner lo siguiente

titulos = xtract.findall("data_type",class_="Nomrbe de la lista)

data_type es el tipo de datos que es, div, h2, h3, etc y nombre de lista es como esta puesto. generalmente sera conjunto el tipo de dato y nombre de clase, algo asi

("div",class_="columns small-12 medium-6 small-only-text-center font-medium")

acto seguido lo pasamos a una lista

titulo = list()

hacemos un ciclo que recorra la lista en busca de esos datos

for x in range titulos:
     titulo.append(x.text)

el x.text y el append son necesarios para los tipos de datos que se marcaran

por ultimo lo puedes imrpimir como print(titulo)

o lo puedes meter en un data frame con pandas, algo asi 

datalink = ('Nombre: ',titulo)

DL = pd.DataFrame(data=datalink)

DL.to_csv('ISP_Data.csv')

En la carpeta del codigo deberias ver el resultado

Espero te haya servido esto. Saludos
