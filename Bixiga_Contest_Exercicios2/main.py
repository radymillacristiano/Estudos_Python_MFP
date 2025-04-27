# CONTESTS: https://docs.google.com/spreadsheets/d/1_GRq1Qe_mVBU440uyRJ_hkgnewaMnq4oK5VbppB-tnU/edit?gid=1735086912#gid=1735086912 

#--------------

# QUESTAO 4

w = int(input())

if 1 <= w <= 100:
    if w % 2 == 0 and w > 2:
        print("YES")
    else:
        print("NO")

#--------------

# QUESTAO 282

n = int(input());

valorX = 0

if 1 <= n <= 150:
    for i in range(n):
        operacao = input()
        if operacao == "X++" or operacao == "++X":
            valorX += 1

        elif operacao == "X--" or operacao == "--X":
            valorX -= 1

print(valorX)

# --------------

# QUESTAO 617

#OPCAO 1

posicaoE2 = int(input())

posicaoE1 = 0

passos = 0

if 1 <= posicaoE2 <= 10**6:
    while posicaoE1 < posicaoE2:
        for passo in [5, 4, 3, 2, 1]:
            if posicaoE1 + passo <= posicaoE2:
                posicaoE1 += passo
                passos += 1
                break

print(passos)
        
# OPCAO 2

posicaoE2 = int(input())

passos = posicaoE2 // 5
if posicaoE2 % 5 != 0:
    passos += 1

print(passos)

#--------------

# QUESTAO 520

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numeroCaracteres = int(input())
palavra = input().lower()

palavraEPangrama = True

if numeroCaracteres < len(alfabeto):
    print("NO")
else:
    for caractere in alfabeto:
        if caractere not in palavra:
            palavraEPangrama = False
            break

    if palavraEPangrama:
        print("YES")
    else:
        print("NO")


