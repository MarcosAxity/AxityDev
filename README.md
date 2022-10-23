# AbrazaLaDiversidad (Challenge Diversidad e inclusión - reto BBVA)

<p align="center"><img src="https://w7.pngwing.com/pngs/771/451/png-transparent-group-of-children-and-earth-illustration-equality-and-diversity-multiculturalism-social-group-child-social-equality-youth-activities-hand-people-friendship-thumbnail.png"/> </p>

## Índice
* [1.Resumen del proyecto](#1-resumen-del-proyecto)
* [2.Conoce nuestra aplicación](#2-conoce-nuestra-aplicacion)
* [3.Creadores ](#3-creadores)

***

## 1. Resumen del proyecto

**Conoce si esxisten sesgos de género en twitter** ¿Sabías que existen sesgos de género en los contenidos de internet que consumimos a diario de forma conciente o inconciente? ¿o que en los contenidos que comparten o comentan tus amigos pueden existir sesgos de género?
Los sesgos de género son una una inclinación consiente o inconsiente a favor o en contra de una persona sin una base objetiva, es decir, puede ser con base en atributos que son inherentes a la persona y que no son cambiables, como puede ser el género, la nacionalidad, la religión, la etnia, etc.
Con el propósito de detectar estos sesgos en los contenidos que consumimos a diario en la red social Twitter, hemos creado la iniciativa #AbrazaLaDiversidad, que está estructurada de la siguiente manera:

* El usuario ingresa un tema de su interés que se esté tratando en twitter a través de la UI, los colores, la presentación y el diseño de la UI se seleccionaron con base en un análisis del usuario objetivo

* A partir de lo anterior se extraen los tweets relacionados al tema, usando la librería de python snscrape y se hace limpieza del texto mediante el uso de expresiones regulares, para posteriormente hacer la conexión del analizador de texto de aws, Amazon Comprehend.

* Se hace el análisis del sentimiento de los tweets en Amazon Comprehend que internamente utiliza el esquema NLP y nos arroja un análisis del sentimiento reconociendo las entidades (personas, organizaciones, cosas, etc), palabras clave, sintaxis entre otras.

* Con los resultados del paso anterior se hace el análisis del sesgo a partir de un árbol de decisión y un modelo de la librería de Python nltk que nos permite determinar los géneros de las personas en los tweets, los resultados en este paso son si cada uno de los tweets analizados presentan sesgo o no -Se generan estadísticas usando lo que se obtuvo del análisis de sesgo: porcentajes de tweets sesgados hacía cualquiera de los géneros y porcentaje de tweets no sesgados.

* Se presentan los resultados al usuario por medio de gráficas que reflejen las estadísticas de manera intuitiva.

## 2. Conoce nuestra aplicación.
 Prueba nuestra aplicación y esta funcionalidad que hemos pensado para ti. Danos un tema de tu interés que se esté tratando en Twitter y nosotros analizaremos si existen sesgos de género. Usa @ si quieres hacer una búsqueda por usuario, **no uses #**.
 
 Visita nuestra App aquí [click aqui ](https://sesgos-de-genero-1pued2rd5-melissa-bracamonte.vercel.app/)
 
 ## 3. Creadores.
 
* Berenice Zavala Jiménez - **Cientifica de datos**
* Melissa Bracamonte Jaraba - **Desarrolladora Frontend**
* Jessica Astrid Valle Dávila - **Desarrolladora Backend**
* Emmanuel Rosas López - **Desarrollador Backend**
* Marcos Olguín Martinez - **Cientifica de datos**
* Jose Ángel Chavez Vizcaíno - **Desarrolladora Backend**