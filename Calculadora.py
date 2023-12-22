def calculadora():
    numero1 = int(input('Primeiro valor:'))
    numero2 = int(input('Segundo valor:'))

    while True:
        menu = int(input('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    
    O que deseja fazer?:'''))
        if menu == 1:
            print(numero1 + numero2)
        elif menu == 2:
            print(numero1 * numero2)
        elif menu == 3:
            if numero1 > numero2:
                print(numero1)
            elif numero1 < numero2:
                print(numero2)
            else:
                print('N/A')
        elif menu == 4:
            numero1 = int(input('Primeiro valor:'))
            numero2 = int(input('Segundo valor:'))
        elif menu == 5:
            break
        else:
            print('Opção inválida.')
calculadora()
