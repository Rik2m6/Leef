def conversorKeyName(KeyName:str) -> list:
    dezena = int
    centena = int
    target = int 
    coordenada = []

    for i, letra in enumerate(KeyName):

        if len(KeyName) == 4:
            if i == 1 or i == 3:
                coordenada.append(int(letra))

        if len(KeyName) == 6:

            if i == 1:
                dezena = int(letra) * 10

            if i == 2:
                target = dezena + int(letra)
                coordenada.append(target)

            if i == 4:
                dezena = int(letra) * 10

            if i == 5:
                target = dezena + int(letra)
                coordenada.append(target)

        if len(KeyName) == 8:

            if i == 1:
                centena = int(letra) * 100

            if i == 2:
                dezena = int(letra) * 10

            if i == 3:
                target = centena + dezena + int(letra)
                coordenada.append(target)

            if i == 5:
                centena = int(letra) * 100

            if i == 6:
                dezena = int(letra) * 10

            if i == 7:
                target = centena + dezena + int(letra)
                coordenada.append(target)

    return coordenada 

if __name__ == "__main__":
    pass