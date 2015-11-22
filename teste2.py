valores = [2,5,10,20,50,100]    
vetor = []
n = 0

def ordena(vet):
    for x in range(len(vet)-1,0,-1):
        for i in range(x):
            if vet[i] < vet[i+1]:
                aux = vet[i]
                vet[i] = vet[i+1]
                vet[i+1] = aux 

a = int(input( "Digite o valor da bandeja 1: "))

while n == 0:

    if a == 0:
        print("valor invalido!")
        a = int(input( "Digite o valor da bandeja: "))

    elif a not in valores:
        print("valor invalido! Não esta dentro dos valores possiveis")
        a = int(input( "Digite o valor da bandeja: "))
        
    else:
        print("valor correto! siga em frente!")
        vetor.append(a)
        n = 1

b = int(input( "Digite o valor da bandeja 2: "))

while n == 1:

    if b == 0 or b == a:
        print("valor invalido! O valor deve ser diferente das anteriores")
        b = int(input( "Digite o valor da bandeja: "))

    elif b not in valores:
        print("valor invalido!Não esta dentro dos valores possiveis")
        b = int(input( "Digite o valor da bandeja: "))

    else:
        print("valor correto! siga em frente!")
        vetor.append(b)
        n = 0

c = int(input( "Digite o valor da bandeja 3: "))

while n == 0:

    if c == 0 or c == a or c == b:
        print("valor invalido! O valor da bandeja deve ser diferente das anteriores")
        c = int(input( "Digite o valor da bandeja: "))
        
    elif c not in valores:
        print("valor invalido!Não esta dentro dos valores possiveis")
        c = int(input( "Digite o valor da bandeja: "))
        
    else:
        print("valor correto! siga em frente!")
        vetor.append(c)
        n = 1
        
ordena(vetor)

SAQUE = int(input("Digite o valor do saque: "))

i = 0

while i == 0:

    N1 = SAQUE/vetor[0]
    RESTO1 = SAQUE % vetor[0]

    N2 = RESTO1/vetor[1]
    RESTO2 = RESTO1 % vetor[1]

    N3 = RESTO2/vetor[2]
    RESTO3 = RESTO2 % vetor[2]

    print( vetor[0] ," x de ", N1 , vetor[1] ," x de ", N2 , vetor[2] ," x de ", N3 )  
    
    if N1 > 0:

        NII = SAQUE / x - 1 * vetor[0]   

        N2 = NII / vetor[1]
        RESTO2 = NII % vetor[1]

        N3 = RESTO2 / vetor[2]
        RESTO3 = RESTO2 % vetor[2]

        print( vetor[0] ," x de ", N1 , vetor[1] ," x de ", N2 , vetor[2] ," x de ", N3 )

    elif N1 == 0:

        N2 = SAQUE / vetor[1]
        RESTO2 = SAQUE % vetor[1]

        N3 = RESTO2 / vetor[2]
        RESTO3 = RESTO2 % vetor[2]

        print( vetor[0] ," x de ", N1 , vetor[1] ," x de ", N2 , vetor[2] ," x de ", N3 )

    i = 1
