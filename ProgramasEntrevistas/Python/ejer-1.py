"""
1. Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión),
sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def print_nums():
    for i in range(1,100):
        if (i % 3) == 0 and (i % 5) == 0:
            print("fizzbuzz", "\n")
        elif (i % 3) == 0:
            print("fizz", "\n")
        elif (i % 5) == 0:
            print("buzz", "\n")
        else:
            print(i , "\n")
    return 0

def main():
    print_nums()
    return 0

main()