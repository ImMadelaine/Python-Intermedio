def run():
    my_list= [3, 'Hello', True, 4.5]
    my_dict= {"firstname": "Madelaine", "lastname": "Barahona"}

    super_list= [
        {"firstname": "Madelaine", "lastname":"Barahona"},
        {"firstname": "Cristian", "lastname":"Gonzalez"},
        {"firstname": "Miguel", "lastname":"torres"},
        {"firstname": "Pepe", "lastname":"Rodelo"},
        {"firstname": "Nala", "lastname":"Gonzalez"}
    ]

    super_dict= {
        "natural_nums": [1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[4.5,3.3,6.4]
    }
    
    #Recorrer el diccionario con el ciclo for usando ITEMS() que nos ayuda a recorrer la clave y el valor del dict

    for key, value in super_dict.items():
        print(key, "-", value)

    #Recorrer la lista con el ciclo for usando i como el indice 
    
    for i in super_list:
        print(i, "-")

if __name__ == '__main__':
    run()