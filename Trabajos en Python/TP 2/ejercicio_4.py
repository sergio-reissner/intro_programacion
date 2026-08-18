numero1 = 10
numero2 = 5
resultado = numero1 * numero2
print('El producto entre ' + str(numero1) + ' y ' + str(numero2) + ' da ' + str(resultado))

#numero1, numero2 y resultado son variables del tipo entero (int)
#Es necesaria la función str(...) ya que los signos + en el print están concatenando texto.
#Por lo tanto es necesario convertir datos de enteros a texto.
#Si por el contrario, deseamos dejar las variables como enteros, debemos sustituir los signos + por comas (,)
#El resultado sería el siguiente:

numero1 = 10
numero2 = 5
resultado = numero1 * numero2
print('El producto entre ',numero1,' y ',numero2,' da ',resultado)