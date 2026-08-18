# almaceno cuántos alumnos asistieron a la clase de hoy
alumnos_presentes = 35
# almaceno el total de inscriptos en la asignatura
alumnos_inscriptos = 54
# calculo del porcentaje de alumnos presentes en la clase de hoy
porcentaje_presentes = (alumnos_presentes * 100) / alumnos_inscriptos
# muestro el porcentaje calculado en pantalla
print('Hoy asistió el ' + str(porcentaje_presentes) + ' porciento del alumnado.')

p = 35
i = 54
pp = (p * 100) / i
print('Hoy asistió el ' + str(pp) + ' % del alumnado.')

#Ambas versiones resuelven satisfactoriamente el problema.
#La versión del programador A es más legible y fácil de comprender, ya que, además de intercalar
#anotaciones, las variables tienen nombres que facilitan su identificación.
#Por el contrario, la desventaja de escribir código como el programador B es que, si bien funciona
#correctamente y es más compácto, cuesta mucho más identificar para qué sirve cada variable.