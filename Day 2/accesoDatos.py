
def abrirArchivo(ruta):
    try:
        archivo = open(ruta,"r")
    except FileNotFoundError:
        print("Archivo no encontrado")
    else:
        matriz = obtenerMatriz(archivo)
        cerrarArchivo(archivo)
        return matriz



def cerrarArchivo(archivo):
    archivo.close()

def obtenerMatriz(archivo):
    matrizCheckSum = []
    for linea in archivo:
        fila = linea.rstrip("\n").replace("\t"," ").split(" ")
        for x,item in enumerate(fila):
            fila[x] = int(fila[x])
        matrizCheckSum.append(fila)
    return matrizCheckSum


if __name__ == '__main__':
    ruta = "./casoTest.txt"
    print(abrirArchivo(ruta))
