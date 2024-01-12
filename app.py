from time import sleep

saldo = 0

historicoTransferencias = []    

while True:
    print("\n=== Olá, seja bem-vindo ao Banco Imper ===\n\n O que deseja fazer?\n\n[1] - Checar Saldo\n[2] - Sacar\n[3] - Depositar\n[4] - Histórico de Transferências\n[5] - Transferência PIX")

    try:
        option = int(input("\n=== Digite sua escolha aqui:  ===\n"))
        if option <= 0 or option >= 6:
            print("Por favor, escolha uma opção válida...\n")
            sleep(1.5)


        elif option ==1:
            print(f"\n - O seu saldo atual é de R$ {saldo}\n")


        elif option ==2:
            try:
                saque = int(input("Digite aqui o valor do saque que deseja efetuar: \n"))
                historicoTransferencias.append(f"-Saque de R${saque}")
                saldo = saldo - saque  
            except:
                print("\n <> Digite um valor válido. <>") 


        elif option ==3:
            try:
                deposito = int(input("Digite aqui o valor do depósito que deseja efetuar: \n"))
                historicoTransferencias.append(f"-Depósito de R${deposito}")
                saldo = saldo + deposito  
            except:
                print("\n <> Digite um valor válido. <>")
        

        elif option ==4:
            print(historicoTransferencias)

        
        elif option ==5:
            try:
                opcao = int(input("Escolha qual a opção do PIX: \a 1) Celular \a 2) CPF \a 3) Chave Aleatória \a 4) E-mail \nDigite sua escolha aqui: "))
                if opcao == 1:
                    pixId = int(input("Digite para qual Número de Celular deseja efetuar o PIX: \n"))
                if opcao == 2:
                    pixId = int(input("Digite para qual CPF você deseja efetuar o PIX: \n"))
                if opcao == 3:
                    pixId = int(input("Digite para qual Chave Aleatória deseja efetuar o PIX: \n"))
                if opcao == 4:
                    pixId = str(input("Digite para qual E-mail deseja efetuar o PIX:\n"))

                pix = int(input("Digite aqui o valor do PIX que deseja efetuar: \n"))
                historicoTransferencias.append(f"-Pix de R${pix} para {pixId}")
                saldo = saldo - pix  
            except:
                print("\n <> Digite um valor válido. <>")



    
            
            

        else:
            print("Obrigado!")
            break
    except:
        sleep(1)
        print("Por favor, escolha uma opção válida.\n")
        sleep(1)
        print("Voltando do INÍCIO...\n")
        
