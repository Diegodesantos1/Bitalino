# Nombre del archivo de entrada y salida
nombre_archivo_entrada = "data_reposo/BRAZO_FUERZA_D.txt"
nombre_archivo_salida = "DATOS_11.txt"

# Lista para almacenar los datos modificados
datos_modificados = []

# Abrir el archivo de entrada
with open(nombre_archivo_entrada, 'r') as archivo_entrada:
    # Leer cada línea del archivo de entrada
    lineas = archivo_entrada.readlines()
    # Iterar sobre las líneas, omitiendo las primeras tres
    for linea in lineas[3:]:
        # Dividir la línea en columnas separadas por tabulaciones
        columnas = linea.strip().split('\t')
        # Convertir el último valor de la última columna a entero y sumar 10
        valor_modificado = int(columnas[-1]) -30
        # Modificar el último valor en la lista de columnas
        columnas[-1] = str(valor_modificado)
        # Unir las columnas de nuevo en una línea y agregarla a la lista de datos modificados
        datos_modificados.append('\t'.join(columnas))

# Escribir los datos modificados en el archivo de salida
with open(nombre_archivo_salida, 'w') as archivo_salida:
    archivo_salida.write('\n'.join(datos_modificados))

print("Los valores de la última columna (a partir de la cuarta fila) se han incrementado en 10 y se han guardado en el archivo 'datos_modificados.txt'")