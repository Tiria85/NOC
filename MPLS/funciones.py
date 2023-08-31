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
