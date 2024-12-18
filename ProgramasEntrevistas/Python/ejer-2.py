"""
2. Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(text1, text2):
    ans = False
    # Dos palabras exactamente iguales no son anagrama
    if text1 == text2:
        ans = False
    else:
        # Convertimos todas las letras de las palabras en minusculas para evitar inconsistencias
        text1 = text1.lower()
        text2 = text2.lower()

        # Se ordenan las letras de ambas palabras y ser verifica que sean las mismas, si son iguales, son anagramas
        if sorted(text1) == sorted(text2):
            ans = True

    return ans

def main():
    palabra1 = "amor"
    palabra2 = "roma"
    print(anagrama(palabra1,palabra2))
    return 0

main()