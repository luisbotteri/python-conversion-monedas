# Uso de API Exchange
# --------------------------------------------------------------------------------------
import requests

API_KEY = "b1bc07c865154a6b43390962"  # API Key

def obtener_tipos():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/ARS"
    response = requests.get(url)
    data = response.json()
    
    if data.get("result") == "success":
        rates = data["conversion_rates"]
        return rates["EUR"], rates["USD"]
    else:
        print("Error al obtener datos:", data.get("error-type", "Desconocido"))
        return None, None

cambio_ars_eur, cambio_ars_usd = obtener_tipos()

if cambio_ars_eur is None or cambio_ars_usd is None:
    print("No se pudo obtener los tipos de cambio, usando valores por defecto.")
    cambio_ars_eur = 1286.00
    cambio_ars_usd = 1130.00

cambio_eur_ars = 1 / cambio_ars_eur
cambio_usd_ars = 1 / cambio_ars_usd

# Código principal.
# --------------------------------------------------------------------------------------_
print("¡Hola, bienvenido/a al programa de conversión de moneda!")
print("Este programa ayuda a convertir automáticamente de mxn a eur o usd y viceversa.")

while True:
    try:
        opcion = input("Por favor, elija el tipo de cambio que desea realizar: \n" 
        "1 para ARS a EUR \n"
        "2 para ARS a USD \n"
        "3 para EUR a ARS \n"
        "4 para USD a ARS \n"
        
        "\n\n").strip().lower()
        
    except ValueError:
        print("Por favor, ingrese un valor válido.")
        continue
    
    if opcion == "1":
        valor = float(input("\nIngrese la cantidad de pesos (ARS): "))
        resultado1 = valor * cambio_ars_eur
        print(f"El resultado del cambio realizado es {resultado1:.2f} euros (EUR)")
    elif opcion == "2":
        valor = float(input("\nIngrese la cantidad de pesos (ARS): "))
        resultado2 = valor * cambio_ars_usd
        print(f"El resultado del cambio realizado es {resultado2:.2f} dólares (USD)")  
    elif opcion == "3":
        valor = float(input("\nIngrese la cantidad de euros (EUR): "))
        resultado3 = valor / cambio_ars_eur
        print(f"El resultado del cambio realizado es {resultado3:.2f} pesos (ARS)")
    elif opcion == "4":
         valor = float(input("\nIngrese la cantidad de dólares (USD): "))
         resultado4 = valor / cambio_ars_usd
         print(f"El resultado del cambio realizado es {resultado4:.2f} pesos (ARS)")
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")
        continue
    
    print("¿Deseas realizar otra conversión? Sí/No")
    
    respuesta = input().strip().lower()
    if respuesta not in ("sí", "si"):
        print("Muchas gracias por haber utilizado el conversor de monedas.")
        break

    