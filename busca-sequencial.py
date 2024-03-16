listaElementos = [1, 4 , 7, 8, 2, 3, 10, 20, 40]
elemento = 3

def buscaSequencial(elementoBuscado, lista):
  for i in range(len(lista)):
    if(lista[i] == elementoBuscado):
      return i
  return -1


listaElementos2 = [1, 4 , 7, 8, 2, 3, 10, 20, 40]
elemento = 3

def buscaSequencial(elementoBuscado, lista):
  for i in range(len(lista)):
    if(lista[i] == elementoBuscado):
      return i
    else:
	    if(lista[i] > elementoBuscado):
          return -1

print(buscaSequencial(elemento, lista=listaElementos))



print(buscaSequencial(elemento, lista=listaElementos))