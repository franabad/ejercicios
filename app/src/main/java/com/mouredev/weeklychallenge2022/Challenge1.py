# package com.mouredev.weeklychallenge2022

# /*
#  * Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama. 
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

def limpiar_acentos(word):
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for acen in acentos:
        if acen in word:
            word = word.replace(acen, acentos[acen])
    return word

def main():
    word1 = input("Escribe una palabra: ")
    word2 = input("Escribe otra palabra: ")

    word1Clean = limpiar_acentos(word1)
    word2Clean = limpiar_acentos(word2)

    word1list = list(word1Clean.lower())
    word2list = list(word2Clean.lower())

    if word1 == word2:
        print("No es un anagrama")

    for i in word1list:
        contador = False
        if i in word2list:
            contador = True
        else:
            print("No es un anagrama")
    if contador == True:
        print("Es un anagrama")

if __name__ == "__main__":
    main()


