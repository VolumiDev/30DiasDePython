edad = 35
altura = 1.77
complex_number = 4 + 3j
triangle_base = float(input("Introduce la base de un trialgulo "))
triangle_height = float(input("Introduce la altura de un triangulo "))
print("El area del triangulo con base:", triangle_base, "y con altura:", triangle_height, "es de:", 0.5 * triangle_base * triangle_height)

a ,b, c = float(input("Introduce lado a del triangulo ")), float(input("Introduce lado b del triangulo ")), float(input("Introduce lado c del triangulo "))
print("El perimetro es de:", a+b+c)

rec_width = float(input("Introduce la anchura de un rectangulo "))
rec_length = float(input("Introduce la altura de un rectangulo "))

print("El area del rectanguolo es:", rec_width * rec_length, "y el perimetro es de:", 2 * rec_length + 2 * rec_width)