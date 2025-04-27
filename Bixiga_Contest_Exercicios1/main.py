# CONTESTS: https://docs.google.com/spreadsheets/d/1_GRq1Qe_mVBU440uyRJ_hkgnewaMnq4oK5VbppB-tnU/edit?gid=1735086912#gid=1735086912 

# QUESTAO 13

a = int(input())

m = int(input())

if 1 <= a <= 50 and 1 <= m <= 50:
    if a + m <= 50:
        print("S")
    else:
        print("N")
else:
    print("Por favor, digite valores entre 1 e 50")


if a + m <= 50:
    print("S")
else:
    print("N")


# ----------------------------------------

# QUESTAO 86

A, B = input().split(" ")

M = (float(A) + float(B))/2

if M >= 4:
    if M >= 7:
        print("Aprovado")
    else:
        print ("Recuperação")
else:
    print ("Reprovado")


# ----------------------------------------

# QUESTAO 260

A, B, C, D = input().split(" ")

PE, CE, PD, CD = int(A), int(B), int(C), int(D)

E = PE * CE
D = PD * CD

if 10 <= PE <= 100 and 10 <= CE <= 100 and 10 <= PD <= 100 and 10 <= CD <= 100:
    if E > D:
        print(-1)
    elif E < D: 
        print(1)
    else:
        print(0)
else:
    print("Por favor, digite valores entre 10 e 100")



# ----------------------------------------

# QUESTAO 146

X = int(input())
Y = int(input())

if -100 <= X <= 100 and -100 <= Y <= 100:
    if X > 0 and Y > 0:
        print('Q1')
    elif X < 0 and Y > 0:
        print('Q2')
    elif X < 0 and Y < 0:
        print('Q3')
    elif X > 0 and Y < 0:
        print('Q4')
    else:
        print("eixos")
else:
    print("Por favor, digite valores entre 10 e 100")














