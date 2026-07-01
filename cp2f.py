
import re
import os
import time

def verificando():
    os.system("cls")
    print(f"Verificando...")
    time.sleep(2)
    os.system("cls")


while True:
    print("=" * 50)
    print("       BEM-VINDO AO GERADOR E VERIFICADOR DE CPF")
    print("=" * 50)
    print()
    print("Este programa permite:")
    print("• Validar um CPF")
    print("• Gerar um CPF válido")
    print()
    print("[1] Verificar CPF")
    print("[2] Gerar CPF")
    print("[3] Encerrar")
    print()
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
        pesos =[10,9,8,7,6,5,4,3,2]
        soma=0
        soma2=0
        
        if len(numero_cpf2)== 9:
            lista=[int(i) for i in numero_cpf2]
        else:
            print("Faltam numeros no CPF")


        for i in range(len(lista)):
            result= lista[i]*pesos[i]
            soma += result

        verificador_1= soma % 11

        if verificador_1 <2:
            digito_1=0
        else:
            digito_1=11-verificador_1
        
        lista.append(digito_1)
        pesos.insert(0,pesos[0]+1)
        for i2 in range(len(lista)):
            soma2+= lista[i2]*pesos[i2]

        verificador_2= soma2%11
        if verificador_2 < 2:
            digito_2=0
            
        else:
            digito_2= 11-verificador_2

        if str(digito_1)+str(digito_2)== verificadores:
            verificando()
            print("O CPF existe.")
            time.sleep(1)
            continue

        else:
            verificando()
            print("O CPF não existe.")
            time.sleep(1)
            continue
    if opcoes=="2":
        numero_cpf= input("Digite 9 digitos: ")
        if len(numero_cpf) <9:

            print("O seu CPF é invalido pois faltam numeros")
            continue
        numero_cpf2=re.sub('[^0-9]','',numero_cpf)
        pesos =[10,9,8,7,6,5,4,3,2]
        soma=0
        soma2=0
        if len(numero_cpf2)== 9:
            lista=[int(i) for i in numero_cpf2]
        else:
            print("Faltam numeros no CPF")


        for i in range(len(lista)):
            result= lista[i]*pesos[i]
            soma += result

        verificador_1= soma % 11

        if verificador_1 <2:
            digito_1=0
        else:
            digito_1=11-verificador_1
        
        lista.append(digito_1)
        pesos.insert(0,pesos[0]+1)
        for i2 in range(len(lista)):
            soma2+= lista[i2]*pesos[i2]

        verificador_2= soma2%11
        if verificador_2 < 2:
            digito_2=0
            
        else:
            digito_2= 11-verificador_2
        
        lista.append(digito_2)
        numero_cpf_final=int("".join(map(str,lista)))
        os.system("cls")
        print("criando o seu CPF...")
        time.sleep(1)
        print(f"O numero em CPF é: {numero_cpf_final}")
        time.sleep(2)
        continue
    if opcoes == "3":
        print("Obrigado por utilizar o Gerador e Verificador de CPF!")
        print("Até a próxima. 👋")
        break

