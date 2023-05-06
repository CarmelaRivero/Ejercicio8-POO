class Conjunto:
    __listaNum=[]
    def __init__(self):
        self.__listaNum=[]
    def agregar (self,num):
        self.__listaNum.append(num)
    def obtenerlist (self):
        return self.__listaNum
    def __add__(self, otro):
        nueva=self.__listaNum.copy()
       
        for i in range (len(otro.obtenerlist())):
            j=0
            while(j<len(self.__listaNum) and (self.__listaNum[j]!=otro.obtenerList()[i])):
                j+=1
            if(j>=len(self.__listaNum)):
                nueva.append(otro.obtenerList()[i])
        print("UNION",nueva)        
    def __sub__(self, otro):
        nueva=self.__listaNum.copy()
        for i in range (len(otro.obtenerList())):
            j=0
            while(j<len(otro.obtenerList()))and (self.__listaNum[j]!=otro.obtenerList()[i]):
                j+=1
            if (j<len(otro.obtenerList())):
                nueva.pop(j)
        print("Diferencia",nueva) 
    def __eq__(self,otro):
        if (len(self.__listaNum)!=(len(otro.obtenerList()))):
            print("Los conjuntos son distintos")
        else:
            i=0
            bandera=True
            while (i< (len(otro.obtenerList())) and (bandera==True)):
                j=0
                while (j<len(otro.obtenerList()) and (self.__listaNum[j]!=otro.obtenerList()[i])):
                    j+=1
                if (j>=(len(otro.obtenerList()))):
                    print("Los conjuntos no son iguales")
                    bandera=False
                else:
                    i+=1
            if bandera==True:
                print("Los conjuntos son iguales")



