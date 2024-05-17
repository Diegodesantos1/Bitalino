<h1 align="center">Análisis de Datos Bitalino</h1>

En este [repositorio](https://github.com/Diegodesantos1/Bitalino) queda resuelta la práctica de los análisis y limpieza de datos.

Autores:

1. [Javier](https://github.com/PdEXavierMY)
2. [Diego](https://github.com/Diegodesantos1)

<h2 align="center">Limpieza y obtención de la muestra</h2>

Primero hemos comenzado realizando las diferentes pruebas de los sensores del dispositivo Bitalino, hemos captado los datos de EDA (Actividad electrodérmica), de EMG (Electromiografía), de EGC (Electrocardiograma), de ACC (Acelerómetro) y de LUX (Luz)

Una vez hemos obtenido los datos hemos utilizado la librería OpenSignalsReader para poder trabajar con los datos obtenidos en formato txt:

![image](https://github.com/Diegodesantos1/Bitalino/assets/91721855/c80d9bf9-56ab-43e5-913e-f5ffcb6c8bdf)

Los hemos cargados:

![image](https://github.com/Diegodesantos1/Bitalino/assets/91721855/a06ba726-4ef3-4527-8e20-a8b151681ee1)


Una vez cargados los datos procedemos a realizar el análisis que se muestra en el fichero visualización.ipynb

Aquí algunos ejemplos de las gráficas generadas:


![image](https://github.com/Diegodesantos1/Bitalino/assets/91721855/3c1d449b-a241-41f6-b604-fbdfa02bc3d5)


![image](https://github.com/Diegodesantos1/Bitalino/assets/91721855/78dc7b12-1c4d-4061-8c3a-f5bf5eb769a3)


![image](https://github.com/Diegodesantos1/Bitalino/assets/91721855/324dd554-3047-43ea-8b2e-398daafcb500)


![image](https://github.com/Diegodesantos1/Bitalino/assets/91721855/936a811a-c521-4413-b504-80af076fb8b5)


![image](https://github.com/Diegodesantos1/Bitalino/assets/91721855/c19f06f8-98bb-4ca4-9766-bfed88320096)


![image](https://github.com/Diegodesantos1/Bitalino/assets/91721855/1ad67cd1-8944-4cc3-ae82-7980c93e1f15)


<h2>Primera Parte: Datos</h2>
Para iniciar el proyecto, depuramos los datos y generamos muestras aleatorias con el fin de aumentar la eficacia del entrenamiento del modelo posteriormente definido.

<h2>Segunda Parte: Modelo</h2>
Después de adquirir una base decente de muestras, procedimos a entrenar un modelo de red neuronal convolucional capaz de distinguir el estado de un músculo según la gráfica introducida que hace referencia a él.

<h2>Trabajo</h2>
El trabajo tipo "TFG" se encuentra en Bitalino.pdf
