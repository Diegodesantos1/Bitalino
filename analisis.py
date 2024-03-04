import matplotlib.pyplot as plt
from opensignalsreader import OpenSignalsReader

# Cargar los datos desde el archivo TXT de Bitalino

data = OpenSignalsReader('data_diego_txt/EDA.txt')
data2 = OpenSignalsReader('data_diego_txt/EMG.txt')
data3 = OpenSignalsReader('data_diego_txt/LUX_ACC.txt')
data4 = OpenSignalsReader('data_javi_txt/ACC_J.txt')
data5 = OpenSignalsReader('data_javi_txt/ECG_J.txt')
data6 = OpenSignalsReader('data_javi_txt/EDA_J.txt')
data7 = OpenSignalsReader('data_javi_txt/EMG_J.txt')
data8 = OpenSignalsReader('data_javi_txt/LUX_J.txt')
# Ploteamos las señales usando matplotlib

# Señal de EDA (Electrodermal Activity)

plt.plot(data.raw([1]))
plt.title('EDA signal')
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()

# Señal de EMG (Electromyography)

plt.plot(data2.raw([1]))
plt.title('EMG signal')
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()

# Señal de Acelerómetro

plt.plot(data3.raw([5]))
plt.title('ACC signal')
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()

# Señal de Luz

plt.plot(data3.raw([6]))
plt.title('LUX signal')
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()

# Señal de Acelerómetro 2

plt.plot(data4.raw([1]))
plt.title('ACC signal')
plt.xlabel('Sample')
plt.ylabel('Value')
plt.show()

# Señal de LUX 2

