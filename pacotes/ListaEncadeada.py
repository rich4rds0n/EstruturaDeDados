class ListaEncadeada:
  inicioLista = None
  fimLista = inicioLista

  def adicionar(self, contato):
    if self.inicioLista = None
        self.iniciolista = contato
    else:
        contato.prox = inicioLista
        self.inicioLista = contato

  def exibir(self):
    aux = self.inicioLista
    ant = aux
    while aux:
      if contato == self.inicioLista:
        self.inicioLista = contato.prox
      if aux == contato:
        ant.prox = contato.prox
      ant = aux
      aux = aux.prox

  def buscar(self, info):
    aux = self.inicioLista

    while aux:
      if (aux.nome == info) | (aux.telefone == info) | (aux == info):
        print("Achou !!" + aux.nome)
        return aux
      elif aux.prox is None:
        ("Essa criatura não existe !!")
      aux = aux.prox