    elif menu == 5:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x % y
       print("O resto da sua divisão é: ",result)   
       historico.append(f"Divisão: {x} % {y} = {result}")

    elif menu == 6:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result1 = x * x
       result2 = y * y
       print("O resultado é: ",result1, "para n1 ao quadrado e ",result2, "para n2 ao quadrado.")
       historico.append(f"Elevação ao quadrado: {x}^2 = {result1}, {y}^2 = {result2}")
    
    elif menu == 7:
       print("Histórico de Cálculos:")
       if historico:
           for item in historico:
               print(item)
       else:
           print("Nenhum cálculo realizado ainda.")