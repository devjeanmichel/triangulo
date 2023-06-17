A = int(input("Digite o 1º lado do triangulo"))
B = int(input("Digite o 2º lado do triangulo"))
C = int(input("Digite o 3º lado do triangulo"))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
        if A != B and A != C and B != C:
            print("O Triangulo é Escaleno")
        else:
            if A == B and A == C and B == C:
                print("O triangulo é equilatero")
            else:
                print("O triangulo é isosceles")

    else:
            print("Ao menos um dos valores indicados não serve pra formar um triangulo")

else:
        print("Ao menos um dos valores indicados não serve pra formar um triangulo")