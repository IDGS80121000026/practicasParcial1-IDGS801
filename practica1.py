
class Practica1:
    
    #declaracion de los metodos de clase
        def __init__(self):
            self.listaNumeros = []
            
        def arbol(self):
                for i in range(5,0,-1):
                    print("*"*i)
                 
        def lista(self):       
                a= int(input("Ingresa el largo de la lista"))
                for i in range(a,0,-1):
                   numero = int(input("Dame el numero: "))
                   self.listaNumeros.append(numero)
        
        def ordenado(self):
            numeros = len(self.listaNumeros)
            for i in range(numeros - 1):
                for j in range(0, numeros - i - 1):
                    if self.listaNumeros[j] > self.listaNumeros[j + 1]:
                     self.listaNumeros[j], self.listaNumeros[j + 1] = self.listaNumeros[j + 1], self.listaNumeros[j]
            print(self.listaNumeros)
            
        def pares(self):
            self.listaPares = []
            for i in self.listaNumeros:
                if i % 2 == 0:
                    self.listaPares.append(i)
            listaFinal = list(set(self.listaPares))        
            print("Los números pares son:", listaFinal)
        
        def inpares(self):
            self.listaInpares = []
            for i in self.listaNumeros:
                if i % 2 != 0:
                    self.listaInpares.append(i)
            listaFinal = list(set(self.listaInpares))
            print("Los números inpares son:", listaFinal)
        
        def repetidos(self):
            conteo = {}
            repetidos = {}

            for i in self.listaNumeros:
                if i in conteo:
                    conteo[i] += 1
                else:
                    conteo[i] = 1

            for i, repeticiones in conteo.items():
                if repeticiones > 1:
                    repetidos[i] = repeticiones

            print("Números repetidos son:")
            for i, repeticiones in repetidos.items():
                print(f"El número {i} se repite --- {repeticiones} veces.")
        
                 
def main():
        obj=Practica1()
        obj.arbol()
        obj.lista()
        obj.ordenado()
        obj.pares()
        obj.inpares()
        obj.repetidos()
        
        
        
if __name__=="__main__":
    main()