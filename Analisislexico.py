def obtener_palabras_reservadas():
    palabras = input("Ingrese las palabras reservadas separadas por espacios: ").split()
    return set(palabras)  

def verificar_cadena(palabras_reservadas, cadena):
    palabras_en_cadena = cadena.split()  
    palabras_encontradas = [palabra for palabra in palabras_en_cadena if palabra in palabras_reservadas]
    
    if palabras_encontradas:
        print("La cadena contiene palabras reservadas:", ", ".join(palabras_encontradas))
    else:
        print("La cadena no contiene palabras reservadas.")

def main():
    palabras_reservadas = obtener_palabras_reservadas()
    while True:
        cadena = input("Ingrese una cadena (o escriba 'salir' para terminar): ")
        if cadena.lower() == "salir":
            break
        verificar_cadena(palabras_reservadas, cadena)

if __name__ == "__main__":
    main()