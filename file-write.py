from io import open

archivo_texto=open("archivo.txt","w")

frase="Estupendo dia para estudiar Python \n el miercoles"

archivo_texto.write(frase)

archivo_texto.close()


