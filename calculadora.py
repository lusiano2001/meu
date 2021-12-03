print('Bem vindo á minha calculadora!\n')

while True:

# 0. operação
    operacao = input('Que operação você deseja efetuar? Digite:\n(1) para soma;\n(2) para subtração;\n(3) para multiplicação;\n(4) para divisão.\n')

# 1. soma
    if operacao == '1':
        a1 = int(input('\nDigite o primeiro número a somar:\n'))
        a2 = int(input('\nDigite o segundo número somar:\n'))
        a = a1 + a2
        print('\n{} + {} = {}'.format(a1, a2, a))

# 1.1. fim
        fim = input('\nOperação concluída! Digite 0 para encerrar ou 1 para repetir.\n')
        if fim == '0':
            break
        else:
            print('')

# 2. subtração
    elif operacao == '2':
        s1 = int(input('\nDigite o primeiro número a subtrair:\n'))
        s2 = int(input('\nDigite o segundo número subtrair:\n'))
        s = s1 - s2
        print('\n{} - {} = {}'.format(s1, s2, s))

# 2.1. fim
        fim = input('\nOperação concluída! Digite 0 para encerrar ou 1 para repetir.\n')
        if fim == '0':
            break
        else:
            print('')

# 3. multiplicação
    elif operacao == '3':
        p1 = int(input('\nDigite o primeiro número a multiplicar:\n'))
        p2 = int(input('\nDigite o segundo número multiplicar:\n'))
        p = p1 * p2
        print('\n{} * {} = {}'.format(p1, p2, p))

# 3.1. fim
        fim = input('\nOperação concluída! Digite 0 para encerrar ou 1 para repetir.\n')
        if fim == '0':
            break
        else:
            print('')

# 4. divisão
    elif operacao == '4':
        q1 = int(input('\nDigite o número que irá ser dividido:\n'))
        q2 = int(input('\nDigite o número divisor:\n'))
        q = q1 / q2
        print('\n{} / {} = {}'.format(q1, q2, q))

# 4.1. fim
        fim = input('\nOperação concluída! Digite 0 para encerrar ou 1 para repetir.\n')
        if fim == '1':
            print('')
        else:
            break

# 5. te amo, juliana
    elif operacao == '17/04':
        input('\nte amo meu amor <3\n'*1000)

# 6. erro
    else:
        print('\nErro! Tente novamente.\n')
