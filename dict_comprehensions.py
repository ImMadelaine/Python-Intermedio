def run():

    #{key: value for value in iterable if condition}    
    #el if condition es opcional, no es obligatorio adicionarlo
    my_dict= {i: i**3 for i in range(1,6) if i%3 != 0}

    print(my_dict)

if __name__ == "__main__":
    run()