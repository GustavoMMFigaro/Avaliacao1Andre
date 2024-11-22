    elif menu == 0:
        print("Saindo do software...")
        break

    else:
        print("Opção invalida, encerrando programa...")
        break

    print()
    print("Deseja continuar utilizando o software?")
    print("1 - Sim")
    print("2 - Não")
    continuar = int(input("Escolha a opção desejada: "))
    
    if continuar == 1:
        limpar_tela()
    else:
        print("Encerrando o programa...")
        break