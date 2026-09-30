import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#cargamos desde csv :b
df = pd.read_csv('Ejercicio_01.csv')
n = len(df)

#calculamos los estadisticos
media = df['valor'].mean()
mediana = df['valor'].median()

#operaciones manuales...
df['desviacion'] = df['valor'] - media
df['desv_cuadrado'] = df['desviacion']**2
df['desv_cubo']=df['desviacion']**3
df['desv_cuarta']=df ['desviacion']**4

#varianza muestral
suma_cuadrados = df['desv_cuadrado'].sum()
var_mestral = suma_cuadrados/(n-1)

#desviacion estandar
desv_muestral = np.sqrt(var_mestral)

#errores estandar
se_var = var_mestral*np.sqrt(2/n)
se_desv = desv_muestral / np.sqrt(2*n)

#asimetria
suma_cubos = df['desv_cubo'].sum()
asimetria = (suma_cubos/n)/(desv_muestral**3)
se_asimetria = np.sqrt(6/n)

#Curtosis
sumas_cuartas = df['desv_cuarta'].sum()
m4 = sumas_cuartas/n
m2 = var_mestral

curtosis = m4/(m2**2)
se_curtosis = np.sqrt(24/n)

#Extremos
val_min = df['valor'].min()
val_max = df['valor'].max()

#Intervalo de confianza
z_critico = 1.96
se_media = desv_muestral/np.sqrt(n)
margen_error = z_critico * se_media
ic_inferior = media - margen_error
ic_superior = media + margen_error

#impresion de resultados

print(f"Media: {media:.4f}")
print(f"Mediana: {mediana:.4f}")
print(f"Varianza Muestral: {var_mestral:.4f}")
print(f"Desviación estandar: {desv_muestral:.4f}")
print(f"Error Varianza: {se_var:.4f}")
print(f"Error Desv: {se_desv:.4f}")
print(f"Asimetria: {asimetria:.4f}")
print(f"Error asimetria: {se_asimetria:.4f}")
print(f"Curtosis: {curtosis:.4f}")
print(f"Error Curtosis: {se_curtosis:.4f}")
print(f"Margen de Error (95%): {margen_error:.4f}")
print(f"Intervalo de confianza: \
      {ic_inferior:.4f} - {ic_superior:.4f}")

#figura :b
plt.figure(figsize=(9,5))

plt.hist(
    df['valor'], bins=8, color='royalblue', 
    edgecolor='black', alpha=0.7)

plt.axvline(
    media, color='red', linestyle='--', linewidth=2,
    label=f'Media: {media:.2f}'
)

plt.axvline(
    mediana, color='orange', linestyle='-', linewidth=2,
    label = f'Mediana: {mediana:.2f}'
)

plt.title("Histograma")
plt.xlabel('Valores xi', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle = ':', alpha=0.7)
plt.tight_layout()
plt.show()