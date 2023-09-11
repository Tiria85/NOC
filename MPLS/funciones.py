def buscar_palabras(archivo_entrada, archivo_salida, palabras_clave):
    try:
        with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
            for linea in entrada:
                for palabra in palabras_clave:
                    if palabra in linea:
                        salida.write(linea)
                        break  # Rompemos el bucle si encontramos una palabra para esta línea
    except FileNotFoundError:
        print("El archivo de entrada no existe.")

# Archivo de entrada y salida
archivo_entrada = 'entrada.txt'
archivo_salida = 'salida.txt'

# Palabras clave que quieres buscar
palabras_clave = ['palabra1', 'palabra2', 'palabra3']

buscar_palabras(archivo_entrada, archivo_salida, palabras_clave)

print("Proceso completado. Líneas encontradas han sido guardadas en", archivo_salida)

# actualizando Git


import tkinter as tk
from tkinter import filedialog

def cargar_archivo():
    archivo_ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.log")])
    if archivo_ruta:
        entry_ruta.delete(0, tk.END)  # Limpiamos el campo de texto
        entry_ruta.insert(0, archivo_ruta)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cargar Archivo")

# Crear y posicionar los widgets
etiqueta = tk.Label(ventana, text="Seleccione un archivo:")
etiqueta.pack(pady=10)

entry_ruta = tk.Entry(ventana, width=40)
entry_ruta.pack()

boton_cargar = tk.Button(ventana, text="Cargar Archivo", command=cargar_archivo)
boton_cargar.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
