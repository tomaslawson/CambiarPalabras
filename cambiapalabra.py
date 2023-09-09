print("hola python")
#cambiar palabra original por una nueva en un txt
"""
1. Abrir y leer archivo 
2. Cambiar palabra
3. guardar el archivo
"""

Palaba_original = "tizas"
palabra_nueva = "yesos"

fichero = open("fichero.txt", "r")
texto = fichero.read()
fichero.close()

texto_final = texto.replace(Palaba_original, palabra_nueva)

fichero = open("fichero.txt", "w")
fichero.write(texto_final)
fichero.close()

fichero = open("fichero.txt", "r")
fichero.close()



print(texto_final)
