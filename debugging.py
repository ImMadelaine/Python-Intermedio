def divisiors(num):
    divisiors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisiors.append(i)
    return divisiors

def run():
    num= int(input("Ingresa un número: "))
    print(divisiors(num))
    print('Ya termino mi programa')


if __name__ == '__main__':
    run()