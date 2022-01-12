# Buscador-películas-vía-texto

## Contenidos:
 - [Descripción](#Descripción)
 - [Motivación](#Motivación)
 - [Código](#Código)
 - [Funcionamiento](#Funcionamiento)

### Descripción 
 El siguiente proyecto es un simple buscador de peliculas similares. Más en específico, el buscador
 utiliza subtítulos en español de distntas películas para realizar búsquedas por similitud, es decir,
 el buscador compara películas en base a los diálogos (subtítulos) de dichas películas y, dada los 
 parecidos entre los subtítulos, establece un criterio para decidir cuán parecidas son dos películas.
 El buscador crea un vocabulario mediante la `tf-idf` y luego, con dicho vocabulario,
 calcula descriptores de contenido para cada subtítulo, estableciendo una métrica
 para compara dos película (en futuras implementaciones se buscará utilizar técnicas que
 calculen descriptores más sofisticados para texto como `word2vec`)

### Motivación
 Una película es un contenido multimedia que consiste en, básicamente, un conjunto de imágenes
 y audios. Sin embargo, detrás de la simple combinación de ambos elementos se conjuga un relato
 que, la mayor parte de las veces, es difícil de entender y abstraer. 
 En ese sentido, comparar peliculas y establecer un criterio absoluto para equiparar dos películas cualquiera es una tarea titánica.
 En muchas ocasiones, la misma escena puede tener significados e interpretaciones radicalmente 
 variadas para diferentes grupos de personas: la misma escena puede significar escenarios totalmente
 opuestos para dos personas. Sin embargo, justamente, muchos buscadores de películas se basan en
 dicha idea: por ejemplo, al ver una película, se recomienda ver otra película porque las personas
 que vieron dicha película también vieron la otra película (y, por ende, son películas similares y/o
 que son del gusto del usuario). En ese sentido, el contenido objetivo de una película es una caja
 negra para la búsqueda y/o recomendación de películas similares y la subjetividad humana se sitúa
 como el criterio principal a la hora de comparar películas. Empero, la subjetividad humana no es
 un impedimiento supremo para no intentar nada y dejar al azar la respuesta de la pregunta sobre
 cómo compara distintas películas.

 Así, como se mencionó anteriormente, las películas son contenidos multimedia formados por,
 solamente, audios e imágenes. Sin embargo, detrás del audio hay diálogos y palabras que alguna vez
 fue representadas mediante texto. En ese sentido, el siguiente trabajo busca presentar un pequeño y
 simple buscador de peliculas a través de los diálogos de una película. Más en particular, el buscador
 utiliza subtítulos en español de distntas películas para realizar búsquedas por similitud, es decir,
 el buscador compara películas en base a los diálogos (subtítulos) de dichas películas y, dada las
 similitudes los subtítulos, establece un criterio para decidir cuán parecidas son dos películas.

 Finalmente, se estudiará la efectividad del buscador y se analizarán posibles 
 mejoras para abordar la búsqueda de películas similares mediante texto

### Código 
 El código del proyecto consiste en scripts de shell (bash) y scripts de python.

 Para los scripts de python se tienen las siguientes especificaciones:
 - Lenguaje de programación usado: Python 3.8.10
 - Librerías usadas: 
    - os
    - sklearn
    - pickle
    - sys

 Para los scripts de shell (bash) se tienen las siguientes especificaciones:
 - Comando usados:
    - mkdir 
    - read
    - printf
    - sed
    - curl
    - grep 
    - cd
    - mv 
    - declare 
    - cat 
    - rm
    - wget
    - file
    - iconv 
    - dos2unix

### Funcionamiento 
 La lógica y funcionamiento del proyecto es la siguient                  
  1. El script `create_data.sh` es el script encargado de generar el dataset para el proyecto. En
  particular, el script se utiliza de la siguiente forma:
  ```bash
   ./create_data file.txt
  ```

  donde `file.txt` es un archivo que contiene nombres de películas y sus fechas de de estreno (en el
  proyecto el archivo file.txt se llama peliculas.txt). Cada línea del archivo mencionado contiene
  un nombre y su respectiva fecha. Por ejemplo, una línea del archivo puede ser:
  > det sjunde inseglet 1957

  Ahora, el script `create_data.sh` lee cada línea del archivo `file.txt` y ejecuta dos scripts por
  cada línea del archivo:
  -  El primer script ejecutado es `get_subs.sh` que, dado el nombre una película y su año de
  estreno, busca en la página [subdivx](https://www.subdivx.com/) 
  los subtítulos asociados a dicha película y descargada los subtítulos 
  más descargados asociados a dicha búsqueda

  - El segundo script ejecutado es `process_sub.sh` que, dado el archivo descargado asociado
  a los subtítulos, formatea dicho archivo.

 2. Cuando se ejecuta el script
  ```bash
   ./create_data file.txt
  ```

  se crea un directorio con distintos archivos de texto que representan los subtítulos para las
  películas del archivo `file.txt`
  Ahora, dado los subtítulos, el script de python `create_tfidf.py` crea los descriptores de texto
  tf-idf asociado a los archivos de los subtítulos de las peliculas. En particular, el script se utiliza
  de la siguiente manera:
  ```bash
    python3 create_tfidf.py
  ```

  Dicho programa genera un archivo binario denominado `dataset.obj` que contiene 
  una estructura que almacena los descriptores de los subtítulos y una matriz de distancia que representa
  la distancia entre los distintos subtítulos (distancia entre los distintos descriptores).
  Luego, distintos scripts hacen uso de dicha estructura para gerarar consultas sobre la similitud
  de los subtítulos. En particular, se tienen los siguientes scripts:

  El script `get_nns.py` imprime por consola los n vecinos más cercanos de cada película
  del dataset. El script se utiliza de la siguiente forma:
  ```bash
    python3 create_tfidf.py
  ```

  donde n es la cantidad de vecinos más cercanos que se quiere imprimir.
  Se puede redigirir la salida del programa para guardar los resultados en un archivo de
  texto. En particular, se debe realizar lo siguiente:
  ```bash
    python3 create_tfidf.py > resultados.txt
  ```

  Respecto a la estructura de presentación de la información, el siguiente ejemplo muestra
  como se presenta: dada la película raging bull, se tiene que sus vecinos más cercanos son
  los siguientes:
  > Los 3 vecinos más cercanos de raging bull 1980 subs.srt son:
  >
  >   1 - rocky 1976 subs.srt 0.2743067667902098
  >
  >   2 - reservoir dogs 1992 subs.srt 0.2413979055133358
  >
  >   3 - pulp fiction 1994 subs.srt 0.22940523832788937

  El script `evaluate.py`, dado el nombre de un archivo `gt.txt`, imprime por consola una
  evaluación de los vecinos más cercanos de cada película del dataset dada la información
  presente en el archivo `gt.txt` (archivo que contiene información sobre un ground truth
  respecto a las similitudes entre distintas películas). Más en particular, el archivo `gt.txt`
  es un archivo que debe contener información sobre una películas y sus vecinos más
  cercanos respecto a alguna categoría. La estructura del archivo es la siguiente: cada
  línea del archivo del `gt.txt` es de la forma:
  > categoría,película_q,vecino_1,vecino_2,...,vecino_n

  donde `categoría` es el valor que define la similitud entre la película `películas_q` y las
  películas `vecino_1`, `vecino_2`, ... y `vecino_n`.
  Un ejemplo de una línea del archivo es la siguiente:
  > crime drama,taxi driver 1976, drive 2011, nightcrawler 2014,fargo 2016

  La línea anterior plantea lo siguiente: El ground truth establece que la película taxi driver
  se parece a las películas drive, nightcrawler y fargo según la categoría crime drama, es
  decir, taxi driver es similar a drive, nightcrawler y fargo porque dichas películas son del
  género crime drama. Nótese que la categoría mencionada no necesariamente tiene que
  un género de película. Se puede establecer, por ejemplo, que la categoría es francis ford
  coppola y luego nombrar películas de dicho director y, por tanto, establecer que películas
  son similares porque fueron dirigidas por el mismo director.

  Para realizar la evaluación, el script evalúa el recall at de los vecinos más cercanos según
  tf-idf en los vecinos según el ground truth, es decir, se revisa, para cada vecino según
  tf-idf, si dicho vecino se encuentra entre los vecinos según el ground truth. Así, el recall
  es la proporción entre los vecinos según tf-idf que se encuentran en los vecinos según el
  ground truth y los vecinos totales escogidos (se escoge la misma cantidad de vecinos que
  la cantidad de vecinos en el ground truth) según tf-idf.

  Respecto al uso del programa, el script se utiliza de la siguiente forma:
  ```bash
    python3 evaluate.py gt.txt
  ```

  Se puede redigirir la salida del programa para guardar los resultados en un archivo de
  texto. En particular, se debe realizar lo siguiente:
  ```bash
    python3 evaluate.py gt.txt > resultados_evaluate.py
  ```

  Respecto a la estructura de presentación de la información, el siguiente ejemplo muestra
  como se presenta:
  > Agrupando los vecinos más cercanos de det sjunde inseglet 1957 según la categoría religious (según el ground truth) se tiene :
  >
  >  ordet 1955
  >
  >  andrei rublev 1979
  >
  >  the tree of life 2011
  >
  > Ahora, los vecinos más cercanos de det sjunde inseglet 1957 obtenidos según td-idf son los siguientes :
  >
  >  ordet 1955 subs.srt
  >
  >  la dolce vita 1960 subs.srt
  >
  >  fanny och alexander 1982 subs.srt
  > 
  > Se obtuvo un recall de 0.3333333333333333
