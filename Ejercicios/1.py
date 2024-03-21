
#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Diferencias de 

diferencia_con_min = 100 - dalto_curso * 1000 // otros_cursos_min / 10
diferencia_con_max = 100 - dalto_curso  * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso * 1000 // otros_cursos_promedio / 10

print(f'El curso de esta persona dura un {diferencia_con_min}% menos que el mas rápido')
print(f'El curso de esta persona dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de esta persona dura un {diferencia_con_promedio}% menos que el promedio')