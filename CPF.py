# nome= "matheus"

# for indice in range(len(nome)):
#     print(indice,nome[indice])
import re
import os
import time
while True:
    print("Digite 1 - Verificar CPF")
    print("Digite 2 - Criar um CPF")
    print("Digite 3 - Sair")
    opcoes=input("Qual das Opções deseja hoje? ")
    if opcoes =="1":
        numero_cpf= input("Digite o seu CPF: ")
        if len(numero_cpf) <11:
            os.system("cls")
            print("O seu CPF é invalido pois faltam numeros")
            time.sleep(1)
            continue
        numero_cpf2=re.sub('[^0-9]','',numero_cpf)
        verificadores=numero_cpf2[-2:]
        numero_cpf2=numero_cpf2[:-2]
        print(numero_cpf2,verificadores)
        pesos =[10,9,8,7,6,5,4,3,2]
        soma=0
        soma2=0
        lista=[]
        lista2=[]
        if len(numero_cpf2)== 9:
            for i3 in numero_cpf2: 
                lista.append(i3)
            lista2 = list(map(int, lista))
            print(lista2)
        else:
            print("Faltam numeros no CPF")


        for i in range(len(lista2)):
            result= lista2[i]*pesos[i]
            soma += result

        verificador_1= soma % 11

        if verificador_1 <2:
            digito_1=0
        else:
            digito_1=11-verificador_1
        
        lista2.append(digito_1)
        pesos.insert(0,pesos[0]+1)
        for i2 in range(len(lista2)):
            soma2+= lista2[i2]*pesos[i2]

        verificador_2= soma2%11
        if verificador_2 < 2:
            digito_2=0
            
        else:
            digito_2= 11-verificador_2
        if str(digito_1)+str(digito_2)== verificadores:
            print("O CPF existe.")
        else:
            print("O CPF não existe.")
    if opcoes=="2":
        numero_cpf= input("Digite 9 digitos: ")
        if len(numero_cpf) <9:

            print("O seu CPF é invalido pois faltam numeros")
            continue
        numero_cpf2=re.sub('[^0-9]','',numero_cpf)
        print(numero_cpf2)
        pesos =[10,9,8,7,6,5,4,3,2]
        soma=0
        soma2=0
        lista=[]
        lista2=[]
        if len(numero_cpf2)== 9:
            for i3 in numero_cpf2: 
                lista.append(i3)
            lista2 = list(map(int, lista))
            print(lista2)
        else:
            print("Faltam numeros no CPF")


        for i in range(len(lista2)):
            result= lista2[i]*pesos[i]
            soma += result

        verificador_1= soma % 11

        if verificador_1 <2:
            digito_1=0
        else:
            digito_1=11-verificador_1
        
        lista2.append(digito_1)
        pesos.insert(0,pesos[0]+1)
        for i2 in range(len(lista2)):
            soma2+= lista2[i2]*pesos[i2]

        verificador_2= soma2%11
        if verificador_2 < 2:
            digito_2=0
            
        else:
            digito_2= 11-verificador_2
        
        lista2.append(digito_2)
        numero_cpf_final=int("".join(map(str,lista2)))
        print(f"O numero em CPF é: {numero_cpf_final}")
    if opcoes == "3":
        break

