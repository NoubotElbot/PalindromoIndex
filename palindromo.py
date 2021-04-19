""" 
Retorna el indice de un caracter de la cadena que al removerse convertiría la cadena en un palindromo
Ej:  
I: aaaad
O: 4

En el caso que ya sea un palindromo o no tenga solución retorna -1
"""
def palindromenindex(cadena):
    inversa = cadena[::-1]
    indice = 0
    aux = cadena
    while(indice < len(cadena)):
        if(cadena == inversa):
            return -1
        elif(cadena[indice] != inversa[indice]):
            aux = cadena[:indice] + "" + cadena[indice+1:]
            rever = aux[::-1]
            if(aux == rever):
                return indice
        indice += 1
    return -1

cadena = input("Ingrese un cadena de texto: ")
print("output:",palindromenindex(cadena))