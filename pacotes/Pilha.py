from pacotes.ListaEncadeada import ListaEncadeada
import pacotes.contato

class Pilha(ListaEncadeada):

  def deletar(self):
    self.inicioLista.estado = True
    self.inicioLista = self.inicioLista.prox