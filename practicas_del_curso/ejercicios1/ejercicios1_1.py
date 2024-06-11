#promedio duracion de cursos python
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

#duracion de crudo
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion en porcentaje
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso / otros_cursos_max * 100
diferencia_con_prom = 100 - dalto_curso / otros_cursos_prom * 100

print(f"el curso de dalto dura un {int(diferencia_con_min)}% menos que el curso mas corto")
print(f"\nel curso de dalto dura un {int(diferencia_con_max)}% menos que el curso mas largo")
print(f"\nel curso de dalto dura un {int(diferencia_con_prom)}% menos que el curso promedio")

#calcular tiempo vacio promedio
diferecia_crudo = 100 - crudo_dalto / crudo_promedio * 100

print(f"\nEl curso de crudo dura un {int(diferecia_crudo)}% menos que el curso promedio")

#mostrando diferencias si los cursos de dalto fueran de 10 horas

print(f"\nVer 10 horas en un curso de dalto equivale a ver {int(otros_cursos_prom / dalto_curso * 10)} horas en otro curso")