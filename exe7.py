'''
Exercicio 7
Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada 
um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 
ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
    ValueError: se o usuário digitar um caracter</li>
    ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão</li>
    IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista</li>
    KeyboardInterrupt: caso o usuário interrompa a execução

'''
while True:
        
    try:
        lista_numeros = []
        for i in range(2):
            numero = float(input("Digite um número: "))
            lista_numeros.append(numero)  
        
        resultado = lista_numeros[0] / lista_numeros[1]
         
    except ValueError:
        print("Valor Invalido")
        del(lista_numeros) 
    except ZeroDivisionError:
        print("Não é possivel dividir por 0")
        del(lista_numeros) 
    except IndexError:
        print("O Indice da matriz não é valido")
        del(lista_numeros) 
    except KeyboardInterrupt:
        print("O usuario Interrompeu a execução")
        del(lista_numeros)
        break
    else:
        print(f"O resultado da divisão é: {resultado}")
        del(lista_numeros) 
        break