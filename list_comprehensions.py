def run():
 #   square = []
  #  for i in range(1, 101):
   #     square.append(i**2)   
    #print(square)

    #Uso de list comprehensions 
    #Sintaxis: [element for element in iterable if condition]
    square = [i**2 for i in range(1, 101) if i%3 != 0]

    #i**2: [Representa a cada uno de los elementos a poner en la nueva lista]
    #for i in range(1, 101): [ciclo a partir del cual se extraeran elementos de otra lista o cualquier iterable]
    #if i%3 != 0: [condicion opcional para filtrar los elementos del ciclo]
    print(square)

if __name__ == '__main__':
    run()
