def run():
    
    
    my_list= [1, 2, 3, 4, 5, 6]

    #for i in my_list:
    #res= lambda x: x*2
    #print(res(my_list))

    squares= list(map(lambda x: x*2, my_list))
    print(squares)


if __name__ == '__main__':
    run()