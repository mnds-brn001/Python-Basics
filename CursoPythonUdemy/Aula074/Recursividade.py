def repetir(n):
    for x in range(n):
        print("Ola mundo!")

def repetirRecursivo(n):
    if n > 0:
        print("Ola Mundo Recursivo!")
        repetirRecursivo(n-1)

#repetir(4)
repetirRecursivo(5)