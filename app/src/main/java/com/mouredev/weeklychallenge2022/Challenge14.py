# package com.mouredev.weeklychallenge2022

# import kotlin.math.pow

# /*
#  * Reto #14
#  * ¿ES UN NÚMERO DE ARMSTRONG?
#  * Fecha publicación enunciado: 04/04/22
#  * Fecha publicación resolución: 11/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
#  * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */


def Armstrong():
    number = int(input("Escribe un número: "))

    digits = [int(x) for x in str(number)]

    suma = 0
    
    for i in digits:
        potencia = i ** 3
        suma = potencia + suma 

    if suma == number:
        print("El número es un número Armstrong")
    else:
        print("No es un número Armstrong")

def main():
    Armstrong()


if __name__ == "__main__": 
    main()
