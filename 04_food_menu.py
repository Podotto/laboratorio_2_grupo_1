def main():
  
  # Bienvenida
  print("Bievenido/a al restaurante Byte Bites")
  print("======================================")
  
  #Bucle
  option = 0
  while option != 6:
    
    #Menú de Opciones
    print("1. Hamburguesa\n2. Nuggets\n3. Papas fritas\n4. Soda\n5. Sundae\n6. Terminar")
  
    # Selección del usuario
    option = int(input("¿Qué te gustaría añadir a tu orden?: "))
    
    # Casos
    match option:
      
      # Caso 1
      case 1:
        print("¿Qué tipo de hamburguesa quieres?: ")
        print("1. Hamburguesa de carne")
        print("2. Hamburguesa de pollo")
        
        burger_type = int(input("Escoge una opción: "))
        
        match burger_type:
          case 1: 
            print("Añadiste una hamburguesa de carne.")
            
          case 2:
            print("Añadiste una hamburguesa de pollo.")
            
          case _:
            print("No es una opción válida.")
      
      # Caso 2
      case 2:
        print("¿Qué salsa quieres?")
        print("1. BBQ\n2. Ranch\n3. Honey Mustard\n4. Buffalo\n5. Ninguna")
        
        sauce = int(input("Escoge una opción: "))
        
        match sauce:
          case 1: 
            print("Añadiste nuggets con salsa BBQ.")
          
          case 2:
            print("Añadiste nuggets con salsa ranch.")
            
          case 3:
            print("Añadiste nuggets con salsa honey mustard")
            
          case 4:
            print("Añadiste nuggets con salsa buffalo.")  
          
          case 5:
            print("Añadiste nuggets sin salsa.")  
            
          case _:
            print("No es una opción válida.") 
            
      # Caso 3
      case 3:
        print("Añadiste papas fritas.")
        
      # Caso 4
      case 4:
        print("¿Qué sabor de soda quieres?: ")
        print("1. Coca Cola\n2. Pepsi\n3. Sprite\n4. Kist Naranja\n5. Kist Fresa")
        
        soda = int(input("Escoge una opción: "))
        
        match soda:
          case 1: 
            print("Añadiste una soda Coca Cola.")
          
          case 2:
            print("Añadiste una soda Pepsi.")
            
          case 3:
            print("Añadiste una soda Sprite.")
            
          case 4:
            print("Añadiste una soda Kist Naranja.")  
          
          case 5:
            print("Añadiste una soda Kist Fresa.")  
            
          case _:
            print("No es una opción válida.") 
      
      # Caso 5
      case 5:
        print("¿Qué tipo de sundae quieres?: ")
        print("1. Chocolate\n2. Caramelo\n3. Fresa")
        
        sundae = int(input("Escoge una opción: "))
        
        match sundae:
          case 1: 
            print("Añadiste un sundae de chocolate.")
          
          case 2:
            print("Añadiste un sundae de caramelo.")
            
          case 3:
            print("Añadiste un sundae de fresa.")
            
          case 4:
            print("No es una opción válida")
                   
      # Caso 6
      case 6:
        print("Hemos tomado tu orden. Por favor pasa a ventanilla para pagar.")  

main()