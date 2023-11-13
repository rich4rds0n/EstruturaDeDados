from pacotes.Contato import Contato
from pacotes.ListaEncadeada import ListaEncadeada
from pacotes.Fila import Fila
from pacotes.Pilha import Pilha

l1 = ListaEncadeada()
l2 = Fila()
l3 = Pilha()

c1 = Contato()
c1.nome = "Kelvin"
l1.adicionar(c1)
l2.adicionar(c1)
l3.adicionar(c1)

c2 = Contato()
c2.nome = "Richardson"
l1.adicionar(c2)
l2.adicionar(c2)
l3.adicionar(c2)

c3 = Contato()
c3.nome = "Erick"
l1.adicionar(c3)
l2.adicionar(c3)
l3.adicionar(c3)

c4 = Contato()
c4.nome = "Joaquim"
l1.adicionar(c4)
l2.adicionar(c4)
l3.adicionar(c4)

l1.exibir()