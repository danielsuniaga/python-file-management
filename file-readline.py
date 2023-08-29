from io import open

archivo_texto = open("archivo.txt","r")

lineas_texto=archivo_texto.readline()

archivo_texto.close()

print(lineas_texto[0])