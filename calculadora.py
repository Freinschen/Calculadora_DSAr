# Calculadora utilizando funções
print('='*40)
operacao = ' '
while operacao not in'ASMD':
    operacao = str(input('Qual operação deseja efetuar:\n[ADIÇÃO(A),SUBTRAÇÃO(S),MULTIPLICAÇÃO(M),DIVISÃO(D)]? ')).upper().strip()[0]
primeiro_num = float(input('Primeiro número: '))
segundo_num = float(input('Segundo número: '))
if operacao == 'A':
    def adicao():
        add = primeiro_num + segundo_num
        return f'{primeiro_num} + {segundo_num} = {add:.2f}'
    res_adicao = adicao()
    print(res_adicao)
if operacao == 'S':
    def subtracao():
        sub = primeiro_num - segundo_num
        return f'{primeiro_num} - {segundo_num} = {sub:.2f}'
    res_subtracao = subtracao()
    print(res_subtracao)
if operacao == 'M':
    def multiplicacao():
        mult = primeiro_num * segundo_num
        return f'{primeiro_num} * {segundo_num} = {mult:.2f}'
    res_multiplicacao = multiplicacao()
    print(res_multiplicacao)
if operacao == 'D':
    def divisao():
        div = primeiro_num / segundo_num
        return f'{primeiro_num} / {segundo_num} = {div:.2f}'
    res_divisao = divisao()
    print(res_divisao)
