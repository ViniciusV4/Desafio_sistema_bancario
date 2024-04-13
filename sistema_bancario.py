# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
# Para deposito o valor tem que ser positivo;
# O sistemas só permiter 3 saques diarios com limite de 500,00. O usuário só pode sacar se tiver o saldo do saque solicitado em conta.
# O extrato deve listar todos os depósitos e saques realizados na conta e no fim mostrar o valor em conta. O valor deve estar formatado com R$

saldo = 0 
limite = 500
saques_realizados = 0
depositos_realizados = 0

while True:

    menu = int(input("""          
=============================               
        MENU:
    [1] Sacar
    [2] Depositar
    [3] Exatrato
    [4] Sair
                     
=============================
                     
=> """))

    if menu == 1:
        print("======= Sacando =======")
        
        valor = float(input("Digite o valor que deseja sacar: => "))

        if valor <= saldo and valor > 0 and saques_realizados < 3 and valor <= limite:
            limite -= valor
            saldo -= valor
            saques_realizados += 1
            print(f"Saque realizado com sucesso.")

        elif saques_realizados >= 3:
            print("""
                    Saque não realizado. O número de saques permitidos por dia é = 3. 
                    Tente novamente amanhã
                  """)
            
        elif valor > limite:
            print("""Saque não realizado. Limite atingido você só pode sacar R$ 500,00 por dia. Tente novamente amanhã
            """)
            
        elif valor < 0:
            print("Saque não realizado. Digite um valor positivo.")
        else:
            print("Saque não realizado. Saldo insulficiente")

    elif menu == 2:
        print("== Depositando ==")
        valor = float(input("Digite o valor que deseja depositar: => "))
        
        if valor > 0:
            saldo += valor
            depositos_realizados += 1
            print("Deposito realizado com sucesso.")
        else:
            print("Deposito não realizado. O valor de deposito tem que ser positivo.")

    elif menu == 3:
        print(f"""
              ========= Extrato =========

              Seu saldo atual =  R$ {saldo:.2f} 
              Numero de saques = {saques_realizados}
              Numero de depositos = {depositos_realizados}

              ===========================
              """)
    
    elif menu == 4:
        break

    else:
        print("Opção invalida, escolha outra opção.")