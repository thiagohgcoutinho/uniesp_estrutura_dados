class No:
    def __init__(self, valor):
        self.valor = valor
        self.filho_esquerdo = None
        self.filho_direito = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivamente(valor, self.raiz)

    def _inserir_recursivamente(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.filho_esquerdo is None:
                no_atual.filho_esquerdo = No(valor)
            else:
                self._inserir_recursivamente(valor, no_atual.filho_esquerdo)
        else:
            if no_atual.filho_direito is None:
                no_atual.filho_direito = No(valor)
            else:
                self._inserir_recursivamente(valor, no_atual.filho_direito)
