import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

#Utilizado para vizualizar caracteres correctamente en consola
win_unicode_console.enable()

#Abrimos el archivo
archivo = codecs.open('texto.txt', 'r', encoding='utf-8')
texto = ""

#Almacenamos el texto en una variable
for linea in archivo:
    linea = linea.strip()
    texto = texto + " " + linea

#Realizamos el Tokenizing con Sent_Tokenize() a cada una de las sentencias del texto
tokens = sent_tokenize(texto)

#Preguntamos por el numero de sentencia a mostrar
print "\nEl texto contine {} sentencias.\nComenzando de 0 hasta {}\n".format(len(tokens), len(tokens) - 1)
numero_sentencia = input("Ingresa en numero de sentencia: ")

if(numero_sentencia > 0 and numero_sentencia < len(tokens)):

    print "\n[Sentencia " + str(numero_sentencia) + "] -> " + tokens[numero_sentencia], '\n'

    #Realizamos el Word_Tokenize() para cada una de las sentencias
    word_tokens = []
    for token in tokens:
        word_tokens.append(word_tokenize(token))

    #Se imprimen los tokens resutantes en pantalla
    n = 0
    for tok in word_tokens[numero_sentencia]:
        print "Token " + str(n) + " -> " + tok
        n = n + 1

    print "\nTotal de tokens por palabras de la sentencia {} son: {} Tokens".format(numero_sentencia, len(word_tokens[numero_sentencia]))

    print "\nTotal de sentencias: {}".format(len(tokens) - 1)

else:
    print "\n\nNumero de sentencia no valido"