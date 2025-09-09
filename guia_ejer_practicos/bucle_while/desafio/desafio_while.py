
# Desafio: Encuesta Tecnológica en UTN Technologies

contador = 0
acumulador_empleados = 0
porcentaje = 0
mayor_edad = 0

while contador < 10:

    nombre = input('Ingrese su nombre: ').lower()
    edad =  int(input('Ingrese su edad: '))
    genero = input('Ingrese su genero (mas/fem): ').lower()
    tecnologia_elegida = input('''
🔹 Inteligencia Artificial (IA)
🔹 Realidad Virtual/Aumentada (RV/RA)
🔹 Internet de las Cosas (IOT)
>= ''').lower()
    
    contador += 1

    if (tecnologia_elegida == 'iot' or tecnologia_elegida == 'ia') and genero == 'mas':
        if 25 <= edad <= 50:
            acumulador_empleados += 1
    
    if not tecnologia_elegida == 'ia' and not genero == 'fem' and 33 <= edad <= 40:
            porcentaje += 1

    if genero == 'mas' and edad > mayor_edad:
        mayor_edad = edad
        nombre_mayor = nombre
        tecnologia_mayor = tecnologia_elegida

porcentaje_aplicado = (porcentaje * 100) / 10

print(f'''
1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, 
cuya edad esté entre 25 y 50 años: {acumulador_empleados}

2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
Su género no sea Femenino
Su edad está entre los 33 y 40 años: {porcentaje_aplicado}%

3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó:
Nombre: {nombre_mayor.title()} | Edad: {mayor_edad} | Tec: {tecnologia_mayor.title()}''')



