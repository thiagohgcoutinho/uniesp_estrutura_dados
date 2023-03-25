class Aluno:

  def __init__ (self, nome, nota1, nota2):
    self.nome = str(nome)
    self.nota1 = float(nota1)
    self.nota2 = float(nota2)
    self.media = 0.0
  
  def calcular_media(self):
    self.media = (self.nota1 + self.nota2) / 2
    return self.media

  def mostrar_dados(self):
    print(f"Nome do aluno: {self.nome}")
    print(f"Primeira nota: {self.nota1}")
    print(f"Segunda nota: {self.nota2}")
    print(f"Méda do aluno: {self.media}")

  def mostrar_situacao(self):
    if self.media >= 6.0:
      print(f"O aluno {self.nome} obteve média {self.media} e foi Aprovado!")
    else:
      print(f"O aluno {self.nome} obteve média {self.media} e foi Reprovado!")

aluno1 = Aluno("Thiago", 8.0, 9.0)
aluno1.calcular_media()
aluno1.mostrar_dados()
aluno1.mostrar_situacao()

aluno2 = Aluno("Luiz", 4.0, 6.0)
aluno2.calcular_media()
aluno2.mostrar_dados()
aluno2.mostrar_situacao()