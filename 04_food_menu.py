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
  
  # Selección del usuario
  option = int(input("¿Qué te gustaría añadir a tu orden?: "))
  
  # Casos
  match option:
    
    # Caso 1
    case 1:
      print("¿Qué tipo de hamburguesa quieres?: ")
      print("1. Hamburguesa de carne")
      print("2. Hamburguesa de pollo")
      
      extra_burger = int(input("Escoje una opción: "))
      
      match extra_burger:
        case 1: 
          print("Añadiste una hamburguesa de carne.")
        
        case 2:
          print("Añadiste una hamburguesa de pollo.")
          
        case _:
          print("No es una opción válida.")
      
  

main()