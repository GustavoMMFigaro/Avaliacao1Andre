 if menu == 1:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x + y
       print("O resultado é: ",result)
       historico.append(f"Soma: {x} + {y} = {result}")

    elif menu == 2:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x - y
       print("O resultado é: ",result)
       historico.append(f"Subtração: {x} - {y} = {result}")

    elif menu == 3:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x * y
       print("O resultado é: ",result)
       historico.append(f"Subtração: {x} * {y} = {result}")

    elif menu == 4:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x // y
       print("O resultado é: ",result)
       historico.append(f"Divisão: {x} / {y} = {result}")
       if x or y == 0:
        print("Divisão por Zero não permitida.")
    