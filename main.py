from ClaseConjunto import Conjunto

if __name__=='__main__':
    unConjunto=Conjunto()
    otroConjunto=Conjunto()
    unConjunto.agregar(1)
    unConjunto.agregar(2)
    unConjunto.agregar(3)
    unConjunto.agregar(4)
    otroConjunto.agregar(6)
    otroConjunto.agregar(7)
    otroConjunto.agregar(8)
    print(unConjunto.obtenerlist())
    print(otroConjunto.obtenerlist())

    opcion=0
    def menu():
       opc=int(input("Menu Principal\n"+
       "1)Union de dos conjuntos\n"+
       "2)Diferencia de dos conjuntos \n"+
       "3)Verificar si dos conjuntos son iguales\n"+
       "4)Finalizar\n"+
       "Seleccione una opcion\n"))
       return opc
    while opcion!=4:
       opcion=menu()
       if opcion==1:
        unConjunto + otroConjunto
       if opcion==2:
        unConjunto - otroConjunto
       if opcion==3:
        unConjunto == otroConjunto
