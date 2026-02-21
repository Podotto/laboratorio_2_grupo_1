def main():
  
  # Bienvenida
  print("Bievenido/a al restaurante Byte Bites")
  print("======================================")
  
  #Menú de Opciones
  print("1. Hamburguesa")
  print("2. Nuggets")
  print("3. Papas fritas")
  print("4. Soda")
  print("5. Sundae")
  print("6. Terminar")
  
  #Bucle
  option = 0
  while option != 6:
  
    # Selección del usuario
    option = int(input("¿Qué te gustaría añadir a tu orden?: "))
    
    # Casos
    match option:
      
      # Caso 1
      case 1:
        print("¿Qué tipo de hamburguesa quieres?: ")
        print("1. Hamburguesa de carne")
        print("2. Hamburguesa de pollo")
        
        burger_type = int(input("Escoje una opción: "))
        
        match burger_type:
          case 1: 
            print("Añadiste una hamburguesa de carne.")
          
          case 2:
            print("Añadiste una hamburguesa de pollo.")
            
          case _:
            print("No es una opción válida.")
      
      
      
      #Caso 6
      case 6:
        print("Hemos tomado tu orden. Por favor pasa a ventanilla para pagar.")  

main()