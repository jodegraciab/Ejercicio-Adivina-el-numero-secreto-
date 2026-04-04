import random

def input_int(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = int(valor)
            if numero > 0:
                return numero
            else:
                print("Por favor ingresar un numero positivo mayor a 0")
        except ValueError:
            print("Este número no es válido, por favor ingresar un numero positivo mayor a 0.")

def input_dificultad(mensaje):
    while True:
        dificultad = input(mensaje).lower()
        if dificultad in ("facil", "medio", "dificil"):
            return dificultad

        else:
            print("Las dificultades validas son 'facil', 'medio', 'dificil'")


niveles = {'facil': 10, 'medio': 20, 'dificil': 50}
historial_global = []
while True:
    print("\n--- ADIVINA EL NUMERO SECRETO ---")
    opcion = input_dificultad("Elige nivel (facil, medio, dificil): ").lower()
    
    limite = niveles.get(opcion, 20)
    numero_secreto = random.randint(1, limite)
    
    intentos = 5
    lista_actual = [] 
    
    print(f"Adivina el nUmero entre 1 y {limite}.")
    
while intentos > 0:
    jugada = input_int(f"Intentos que te quedan: {intentos}. Número: ")
    lista_actual.append(jugada) 
    
    if jugada == numero_secreto:
        print("¡Eres todo un Ganador!")
        print(f"Ganaste en {6 - intentos} intentos.")
        break
    elif jugada < numero_secreto:
        print("El numero es Mayor.")
    else:
        print("El numero es Menor.")
    intentos -= 1
        
    if intentos == 0:
        print(f"Perdedor. El numero era {numero_secreto}")

    if len(lista_actual) > 0:
        lista_actual.insert(0, "Temp")   
        lista_actual.remove("Temp")     
        ultimo = lista_actual.pop(-1)    
        lista_actual.append(ultimo)      

    historial_global.extend(lista_actual)
    
    if input("\n¿Quieres jugar otra vez? (si/no): ").lower() != "si":
        break
# agregue un historial por si el jugador quiere sacar su estadistica como apostador
print(f"\nJuego terminado. Todos tus intentos fueron: {historial_global}")
