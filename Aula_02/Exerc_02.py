print("Média das Notas")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

soma = (nota1 + nota2 + nota3) / 3

print("A média é", round(soma,2))

if 7 <= soma < 10:
    print("APROVADO")
elif soma < 7:
    print("REPROVADO")
else:
    print("APROVADO COM DISTINÇÃO")