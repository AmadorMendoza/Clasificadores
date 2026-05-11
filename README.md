#Clasificadores KNN y Random Forest para detectar Deterioro Cognitivo Leve (DCL)



# Instrucciones para replicar resultados

> [!WARNING]
> Este repositorio no cuneta con un archivo para instalar las librerias necesarios, considere ver la primer celda del archivo
> [Clasificadores](Clasificadores.ipynb) para instalar las libererias faltantes en tu espacio de trabajo.

El archivo [clasificadores](Clasificadores.ipynb) tiene un conjunto de funciones que ayudaran a trabajar 
con algoritmos de clasificaci\`on, en este trabajo en particular se trabajan los algoritmos KNN y Random Forest.

Para trabajar con el conjunto de datos completos es recomendable descargar la carpeta [Recortes aleatorios](Recortes_alaeatorios) 
donde encontraran dos archivos comprimidos del tipo **.7z**, descomprimalos y asegurese de que las carpetas descomprimidas se llamen 
**Control** y **DCL** y que cuentan con 10 capertas y 8 carpetas respectivamente en cada carpeta descomprimida, a su vez cada una de las 
18 carpetas debe contar con al menos 21 carpetas las cuales corresponden a los nodos con los cuales se ha trabajado en este proyecto.


> [!NOTE]
> Si su equipo no cuenta con una forma de abrir este archivo puede visitar la pagina oficila de [7-Zip](https://www.7-zip.org/download.html),
> ahi encontrara los enlaces para descargar el archivo correspondiente a su sistema operativo, de igual forma si es usuario de
> alguna distribucion de linux igual puedes instalarlo directamente en terminal.

Si solo necesita trabajar con las metricas **SD1** y **SD2** que correcponden a la desviaci\`on a corto y largo plazo respectivamente 
puede descargar la carpeta [sd1_sd2](sd1_sd2) en la cual encontrara los valores para cada desviaci\`on por nodo y correspondiente a cada sujeto.

La carpeta [Reporte](Reporte) puede ignorarla si lo que busca solo son los archivos con los datos de los encefalogramas.
