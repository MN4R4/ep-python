valores = [2,5,10,20,50,100]    
vetor = []
n = 0
i = 0
                
print ("Valores possiveis para bandeja",valores)
a = int(input( "Digite o valor da bandeja 1: "))
b = int(input( "Digite o valor da bandeja 2: "))
c = int(input( "Digite o valor da bandeja 3: "))

while n == 0:

    if a == 0:
        print("ERRO! Nenhuma bandeja pode ter valor zerado.")
        a = int(input( "Digite o valor da bandeja 1: "))
               
    elif b == 0:
        print("ERRO! Nenhuma bandeja pode ter valor zerado.")
        b = int(input( "Digite o valor da bandeja 2: "))

    elif c == 0:
        print("ERRO! Nenhuma bandeja pode ter valor zerado.")
        c = int(input( "Digite o valor da bandeja 3: "))
        
    elif a not in valores and b not in valores and c not in valores:
        print("ERRO! Valor de cédula inválido na bandeja 1, bandeja 2 e bandeja 3")
        a = int(input( "Digite o valor da bandeja 1: "))
        b = int(input( "Digite o valor da bandeja 2: "))
        c = int(input( "Digite o valor da bandeja 3: "))

    elif a not in valores and b not in valores:
        print("ERRO! Valor de cédula inválido na bandeja 1 e bandeja 2")
        a = int(input( "Digite o valor da bandeja 1: "))
        b = int(input( "Digite o valor da bandeja 2: "))

    elif a not in valores and c not in valores:
        print("ERRO! Valor de cédula inválido na bandeja 1 e bandeja 3")
        a = int(input( "Digite o valor da bandeja 1: "))
        c = int(input( "Digite o valor da bandeja 3: "))

    elif b not in valores and c not in valores:
        print("ERRO! Valor de cédula inválido na bandeja 2 e bandeja 3")
        b = int(input( "Digite o valor da bandeja 2: "))
        c = int(input( "Digite o valor da bandeja 3: "))

    elif a not in valores:
        print("ERRO! Valor de cédula inválido na bandeja 1")
        b = int(input( "Digite o valor da bandeja 1: "))

    elif b not in valores:
        print("ERRO! Valor de cédula inválido na bandeja 2")
        b = int(input( "Digite o valor da bandeja 2: "))
        
    elif c not in valores:
        print("ERRO! Valor de cédula inválido na bandeja 3")
        c = int(input( "Digite o valor da bandeja 3: "))
        
    elif b == a:
        print("ERRO! Não são permitidos valores iguais em bandejas diferentes")
        b = int(input( "Digite o valor da bandeja 2 novamente: "))

    elif c == a or c == b:
        print("ERRO! Não são permitidos valores iguais em bandejas diferentes")
        c = int(input( "Digite o valor da bandeja 3 novamente: "))
      
    else:
        print ("Bandejas Ok!")
        vetor.append(a)
        vetor.append(b)
        vetor.append(c)
        n = 1
        
vetor.reverse()

SAQUE = int(input("Digite o valor do saque: "))

while n == 1:
    
    if SAQUE > 2500:
        print("ERRO! Valor desejado excede R$2500,00 !")
        SAQUE = int(input("Digite o valor do saque novamente: "))

    elif SAQUE <= 0:
        print("ERRO! Valor tem que ser maior que R$ 0,00!")
        SAQUE = int(input("Digite o valor do saque novamente: "))

    else:
        n = 0

if SAQUE > vetor[0]:
    n1 = SAQUE / vetor[0]
    resto = SAQUE % vetor[0]
    resto2 = resto % vetor[1]
    resto3 = resto2 % vetor[2]
    
    if resto > vetor[1]:
        n2 = resto / vetor[1]
        resto2 = resto % vetor[1]
        
    elif resto2 > vetor[2]:
        n3 = resto2 / vetor[2]
        resto3 = resto2 % vetor[2]
        
    elif resto3 != 0:
        print("valor invalido")
        
elif SAQUE > vetor[1]:
    n2 = SAQUE / vetor[1]
    resto2 = SAQUE % vetor[1]
    resto3 = resto2 % vetor[2]
    
    if resto2 > vetor[2]:
        n3 = resto2 / vetor[2]
        resto3 = resto2 % vetor[2]
        
    elif resto3 > 0:
        print("valor inválido")
        
elif SAQUE > vetor[2]:
    n3 = SAQUE / vetor[2]
    resto3 = SAQUE % vetor[2]

    if resto3 > 0:
        print("valor invalido")
        
else:
    print("valor invalido")
    
        
    
