import random

# Datos del brazo izquierdo en reposo
data_izq_reposo = """
# OpenSignals Text File Format. Version 1
# {"84:BA:20:5E:FF:7F": {"position": 0, "device": "bitalino_rev", "device name": "84:BA:20:5E:FF:7F", "device connection": "BTH84:BA:20:5E:FF:7F", "sampling rate": 100, "resolution": [4, 1, 1, 1, 1, 10], "firmware version": 1282, "comments": "", "keywords": "", "mode": 0, "sync interval": 2, "date": "2024-3-6", "time": "18:51:36.613", "channels": [1], "sensor": ["EMGBITREV"], "label": ["A1"], "column": ["nSeq", "I1", "I2", "O1", "O2", "A1"], "special": [{}], "digital IO": [0, 0, 1, 1]}}
# EndOfHeader
0	0	0	0	0	480	
1	0	0	0	0	542	
2	0	0	0	0	479	
3	0	0	0	0	543	
4	0	0	0	0	480	
5	0	0	0	0	544	
6	0	0	0	0	479	
7	0	0	0	0	541	
8	0	0	0	0	482	
9	0	0	0	0	539	
10	0	0	0	0	477	
11	0	0	0	0	542	
12	0	0	0	0	480	
13	0	0	0	0	542	
14	0	0	0	0	478	
15	0	0	0	0	542	
0	0	0	0	0	479	
1	0	0	0	0	541	
2	0	0	0	0	479	
3	0	0	0	0	542	
"""

# Obtén cada línea individual del string de datos
lineas_datos_izq_reposo = data_izq_reposo.strip().split('\n')

# Genera las líneas adicionales del brazo izquierdo cansado
lineas_datos_izq_cansado = []
valor_a1_cansado = 480  # Valor inicial para A1

# Repite el patrón de los datos en reposo para generar datos cansados
for i in range(3500):  # Generar 3500 líneas
    # Añade un poco de ruido aleatorio
    valor_a1_cansado += random.randint(-2, 2)
    # Asegura que el valor esté dentro del intervalo especificado
    valor_a1_cansado = max(450, min(575, valor_a1_cansado))
    # Construye la línea con el valor de A1 para el brazo izquierdo cansado
    linea = f"{i % 16}\t0\t0\t0\t0\t{valor_a1_cansado}"
    # Agrega la línea a la lista
    lineas_datos_izq_cansado.append(linea)

# Concatena las líneas de datos en cansado
datos_izq_cansado_str = '\n'.join(lineas_datos_izq_cansado)

# Guarda los datos en un archivo de texto
with open('data_mal/DATOS_11.txt', 'w') as file:
    file.write(data_izq_reposo.strip() + '\n')  # Escribe primero los datos del reposo
    file.write(datos_izq_cansado_str)  # Escribe los datos cansados

print("Datos del brazo izquierdo cansado generados y guardados en 'BRAZO_CANSADO_FUERZA_I.txt'")
