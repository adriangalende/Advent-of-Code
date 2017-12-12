#Part 1
#The spreadsheet consists of rows of apparently-random numbers.
#To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum.
#For each row, determine the difference between the largest value and the smallest value;
#the checksum is the sum of all of these differences.

#For example, given the following spreadsheet:

#5 1 9 5
#7 5 3
#2 4 6 8
#The first row's largest and smallest values are 9 and 1, and their difference is 8.
#The second row's largest and smallest values are 7 and 3, and their difference is 4.
#The third row's difference is 6.


def checkSum(matrizCheckSum):
    sumaDigitos = 0
    for fila in matrizCheckSum:
        sumaDigitos += max(fila) - min(fila)
    return sumaDigitos

def checkSum2Parte(matrizCheckSum):
    sumaDigitos = 0

    print(int(sumaDigitos))
    return sumaDigitos


if __name__ == "__main__":
    import accesoDatos
    #--------- 1 parte ---------
    #caso test ejemplo
    ruta = "./basicTest.txt"
    matrizCheckSum = accesoDatos.abrirArchivo(ruta)
    assert checkSum(matrizCheckSum) == 18, "Caso test básico fallado"
    #caso test personal
    ruta = "./casoTest.txt"
    matrizCheckSum = accesoDatos.abrirArchivo(ruta)
    print(checkSum(matrizCheckSum))
    #--------- 2 parte ---------
    #caso test ejemplo
    ruta = "./basicTest2Parte.txt"
    matrizCheckSum = accesoDatos.abrirArchivo(ruta)
    assert checkSum2Parte(matrizCheckSum) == 9, "Caso test básico 2 parte fallado"
