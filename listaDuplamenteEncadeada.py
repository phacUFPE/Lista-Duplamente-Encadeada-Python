## NO
class No:
   def __init__(self, anterior=None, item=None, proximo=None):
      self.anterior = anterior
      self.item = item
      self.proximo = proximo

   def __getitem__(self):
      return self.item

## LISTA
class Lista:
   def __init__(self):
      self.primeiro = self.ultimo = No()
      self.tamanho = 0
      self.contIter = 0

   def checarOrdenagem(self):
      if self.vazia():
         return None
      anterior = self.primeiro
      atual = self.primeiro.proximo
      while not atual.proximo is None:
         if atual.item > atual.proximo.item:
            return False
         anterior = atual
         atual = anterior.proximo
      return True

   def inserir(self, item):
      self.ultimo.proximo = No(self.ultimo, item, None)
      self.ultimo = self.ultimo.proximo
      self.tamanho += 1

   def inserirOrdenado(self, item):
      if self.vazia():
         self.inserir(item)
         return
      anterior = self.primeiro
      atual = self.primeiro.proximo
      while not atual is None and atual.item < item:
          anterior = atual
          atual = anterior.proximo
      anterior.proximo = No(anterior, item, atual)
      self.tamanho += 1
      if atual is None:
          self.ultimo = anterior.proximo

   def removerInicio(self):
      if self.vazia(): return
      proximo = self.primeiro.proximo
      anterior = self.primeiro.anterior
      self.primeiro.proximo = None
      self.primeiro.anterior = None
      item = self.primeiro.item
      proximo.anterior = anterior
      temp = self.primeiro
      self.primeiro = self.primeiro.proximo
      del temp
      del proximo
      del anterior
      return item

   def remover(self, item):
      if self.vazia(): return
      auxiliar = self.primeiro.proximo
      while not auxiliar is None and auxiliar.item != item:
         auxiliar = auxiliar.proximo

      if auxiliar is None: return

      item = auxiliar.item
      if auxiliar == self.ultimo:
         self.ultimo = auxiliar.anterior
      else: auxiliar.proximo.anterior = auxiliar.anterior
      auxiliar.anterior.proximo = auxiliar.proximo
      auxiliar.proximo = None
      auxiliar.anterior = None
      del auxiliar
      return item

   def vazia(self):
      return self.primeiro == self.ultimo

   def __represent(self):
      texto = "["
      anterior = self.primeiro
      atual = self.primeiro.proximo
      while not atual is None:
         if atual.proximo != None:
            texto += str(atual.item)
            texto += ", "
         else:
            texto += str(atual.item)

         anterior = atual
         atual = anterior.proximo
      texto += "]"
      return texto

   def buscaBinaria(self, item):
      inicio = 0
      fim = self.tamanho-1
      while inicio <= fim :
         meio = (fim + inicio)/2
         if chaves[meio] < chave: fim = meio -1
         elif chaves[meio] > chave: inicio = meio +1
         else: return meio
      return inicio
   
   #BUSCA UM ITEM, SE FOR VAZIO, RETORNA NONE. SE NAO FOR, DEFINE UMA VARIAVEL PEGANDO O PRIMEIRO DA LISTA E VARRE TODOS OS ITENS DA LISTA ATÉ QUE ACHE O ITEM PEDIDO. RETORNA O ITEM, SE ACHAR. RETORNA None, SE NÃO.
   def busca(self, item):
      if self.vazia():
         return None
      aux = self.primeiro.proximo
      while aux.proximo != None:
         if aux.item.getIdCandidato() == item:
            return aux
         aux = aux.proximo
         
   def __str__(self):
      return self.__represent()

   def __repr__(self):
      return self.__represent()

   def __getitem__(self, indice):
      if indice >= self.tamanho:
         raise IndexError("Indice Inexistente")
      no = self.primeiro.proximo
      for contAux in range(indice):
         no = no.proximo
      return no.item

   def __iter__(self):
      return self

   def __next__(self):
      if self.contIter == 0:
         self.raiz = self.primeiro
      if self.tamanho > self.contIter:
         self.raiz = self.raiz.proximo
         self.contIter += 1
         return self.raiz.item
      else:
         del self.raiz
         self.contIter = 0
         raise StopIteration   
     
