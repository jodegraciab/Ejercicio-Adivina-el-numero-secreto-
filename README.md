import random
niveles = {'facil': 10, 'medio': 20, 'dificil': 50}
historial_global = []
while True:
    print("\n--- ADIVINA EL NUMERO SECRETO ---")
    opcion = input("Elige nivel (facil, medio, dificil): ").lower()
    
    # por si el jugador coloca una opcion que no esta en el menu lo colocara directamente al nivel medio  
  limite = niveles.get(opcion, 20)
    numero_secreto = random.randint(1, limite)
    
  intentos = 5
    lista_actual = [] 
    
  print(f"Adivina el nUmero entre 1 y {limite}.")
    
   while intentos > 0:
        jugada = int(input(f"Intentos que te quedan: {intentos}. Número: "))
        lista_actual.append(jugada) 
        
  if jugada == numero_secreto:
            print("¡Eres todo un Ganador!")
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
