import os
os.system("cls")
# Requerimientos
# 1.	Mostrar menú de productos: 
# El programa debe mostrar el siguiente menú:
# 1. Pokébola → $1000
# 2. Poción → $1500
# 3. Revivir → $3000
# 4. Baya → $500
# 5. Finalizar compra
# ________________________________________
# 2.	Ingreso de productos: 
# •	El usuario debe poder seleccionar productos ingresando el número correspondiente. 
# •	Validar que la opción ingresada sea correcta (entre 0 y 4). 
# •	Si la opción es inválida, mostrar un mensaje de error y volver a pedirla. 
# ________________________________________
# 3.	Cantidad de productos: 
# •	Por cada producto seleccionado, pedir la cantidad. 
# •	Validar que la cantidad sea un número entero positivo. 
# ________________________________________
# 4.	Acumulación de compra: 
# •	Calcular el total acumulado de la compra. 
# •	Llevar un contador de la cantidad total de productos comprados. 
# ________________________________________
# 5.	Sistema de descuentos: 
# Aplicar los siguientes descuentos:
# •	🔹 Si el total de la compra supera los $5000 → aplicar 10% de descuento. 
# •	🔹 Si compra más de 10 productos en total → aplicar un 5% adicional. 
# •	🔹 Si el entrenador compra al menos 3 “Revivir” → aplicar un 15% adicional SOLO sobre ese producto. 
#  Los descuentos son acumulables.
# ________________________________________
# 6.	Uso de bandera (flag): 
# •	Usar una bandera para verificar si el usuario compró al menos un producto antes de finalizar. 
# •	Si no compró nada, mostrar un mensaje:
# "No has realizado ninguna compra." 
# ________________________________________
# 7.	Manejo de errores: 
# •	Utilizar try-except para evitar que el programa se rompa ante entradas inválidas (por ejemplo, letras en vez de números). 
# ________________________________________
# 8.	Salida final:
# Mostrar un resumen con: 
# •	Total bruto 
# •	Total de descuentos aplicados 
# •	Total final a pagar 
# •	Cantidad total de productos comprados
opcion = int
pokeball = 1000
pocion = 1500
revive = 3000
baya = 500
cant_poke = 0
cant_pocion = 0
cant_revive = 0
cant_baya = 0
acum_compra = 0
acum_cant = 0
try:
    print("------Bienvenido a la poketienda------")
    while True:
        opcion = int(input("Seleccione su opción:\n1. Pokébola -> 1000\n2. Poción -> 1500\n3. Revivir -> 3000\n4. Baya -> 500\n5. Finalizar compra.\n"))
        if opcion == 1:
            cant = int(input("¿Cuántas va a llevar?\n"))
            cant_poke = 0 + cant
        elif opcion == 2:
            cant = int(input("¿Cuántas va a llevar?\n"))
            cant_pocion = 0 + cant
        elif opcion == 3:
            cant = int(input("¿Cuántas va a llevar?\n"))
            cant_revive = 0 + cant
        elif opcion == 4:
            cant = int(input("¿Cuántas va a llevar?\n"))
            cant_baya = 0 + cant
        elif opcion == 5:
            print("Gracias por su compra")
            break
        else:
            print("Valor ingresado no válido.")
            os.system("cls")
        precio_poke = pokeball * cant_poke
        precio_pocion = pocion * cant_pocion
        precio_revive = revive * cant_revive
        precio_baya = baya * cant_baya
        acum_compra = precio_poke + precio_pocion + precio_revive + precio_baya
        acum_cant = cant_poke + cant_pocion + cant_revive + cant_baya
        if acum_compra > 5000:
            desc_5000 = acum_compra * 0.1
        else:
            desc_5000 = 0
        prov1 = acum_compra - desc_5000
        if acum_cant > 10:
            desc_cant = prov1 * 0.05
        else:
            desc_cant = 0
        prov2 = prov1 - desc_cant
        if cant_revive > 2:
            desc_revive = precio_revive * 0.15
        else:
            desc_revive = 0
        prov_revive = precio_revive - desc_revive
        valor_final = prov2 - desc_revive
        desc_total = desc_cant + desc_revive + desc_5000
    if acum_cant == 0:
        print("No ha comprado nada.")

except:
    print("Mal ahí.")
print(f"Total bruto:\n{acum_compra}")
print(f"Descuentos aplicados:\nDescuento por precio:\n{desc_5000}\nDescuento por más de 10 productos:\n{desc_cant}\nDescuento por más de 3 revivir:\n{desc_revive}\nTotal de descuento:\n{desc_total}")
print(f"Total a pagar:\n{valor_final}")
print(f"Cantidad total de productos comprada:\nPokébolas: {cant_poke}\nPociones: {cant_pocion}\nRevivir: {cant_revive}\nBayas: {cant_baya}")