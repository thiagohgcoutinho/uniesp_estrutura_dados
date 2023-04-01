class Aluno:

  def __init__ (self, nome, nota1, nota2,nota3):
    self.nome = str(nome)
    self.nota1 = float(nota1)
    self.nota2 = float(nota2)
    self.nota3 = float(nota3)
    self.media = 0.0
  
  def calcular_media(self):
    self.media = (self.nota1 + self.nota2 + self.nota3) / 3
    return self.media

  def mostrar_dados(self):
    print(f"Nome do aluno: {self.nome}")
    print(f"Primeira nota: {self.nota1}")
    print(f"Segunda nota: {self.nota2}")
    print(f"Terceira nota: {self.nota3}")
    print(f"Méda do aluno: {self.media}")

  def mostrar_situacao(self):
    if self.media <= 5.0:
      print(f"O aluno {self.nome} obteve média {self.media} e foi Reprovado!")
    elif 6 <= self.media < 7:
      print(f"O aluno {self.nome} obteve média {self.media} e está na final!")
    else:
      print(f"O aluno {self.nome} obteve média {self.media} e foi Aprovado!")

aluno1 = Aluno("Thiago", 8.0, 9.0, 7.5)
aluno1.calcular_media()
aluno1.mostrar_dados()
aluno1.mostrar_situacao()

aluno2 = Aluno("Luiz", 4.0, 6.0, 4.5)
aluno2.calcular_media()
aluno2.mostrar_dados()
aluno2.mostrar_situacao()

aluno3 = Aluno("Amanda", 6.0, 7.0, 6.5)
aluno3.calcular_media()
aluno3.mostrar_dados()
aluno3.mostrar_situacao()