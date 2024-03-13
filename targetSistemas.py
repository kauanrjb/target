#Kauan Rajab Lima 

def ex1():
    print('Exercicio 1:') 
    i = 13
    s = 0
    k = 0
    while k < i:
        k += 1 # ('+=' recebe o valor da variavel que o antecede e soma 1)
        s += k
    print(f'\n    Variavel soma recebe: {s}')

def ex2():
    print('\nExercicio 2: Sequencia de Fibonacci!')
    n = int(input('\n   Digite o termo que gostaria de saber se pertence a sequencia: '))
    a = 0 #primeiro valor da sequencia
    b = 1 #segundo valor da sequencia
    count = 3 #contador comecando a partir do terceiro valor 
    fibo = [a, b] #lista contendo os termos da sequencia
    for count in range (count, n + 4): #soma-se 4 no 'n' porque ja comeca do termo 3.
        c = a + b
        fibo.append(c)
        a = b
        b = c
        count += 1
    if n in fibo: #verificando se o valor digitado esta na sequencia
        print(f'        O valor {n} esta presente na sequencia!')
    else:
        print(f'        O valor {n} nao esta presente na sequencia')

def ex3():
    print('\nExercicio 3:')
    print('     a:9 / b:128 / c:49 / d:100 / e:13 / f:200')

def ex4():
    print('\nExercicio 4:')
    print('          Para resolver o desafio, deve-se levar em conta o aquecimento que existe na lampada, causado pela energia elétrica que a resistência absorve e transforma em energia térmica. A partir disso, acenderia um interruptor e o deixaria ligado por alguns minutos, depois o apagaria e acenderia algum outro, assim quando for a qualquer sala, posso assumir que se sua lampada estiver acesa, ela pertence ao interruptor ligado, se estiver apagada e quente pertence ao interruptor que foi ligado por um tempo e depois desligado, e se estiver apagada e fria a lampada pertence ao interruptor que não foi mexido. Para descobrir as demais salas, ligaria qualquer um dos interruptores restantes e iriamos para uma sala diferente da primeira. Caso a sala estivesse acesa, atribuiria o interruptor ligado àquela sala e o outro interruptor para a sala restante, e caso estivesse apagada, atribuiria o interruptor desligado à sala em que estou e o ligado à outra sala')

def ex5():
    print('\nExercicio 5:')
    a = str(input('Digite a String a ser invertida: '))
    b = a[::-1] #utilizando indexacao, pois a String é iteravel em python.
    print(f'String invertida: {b}')
    
ex1()
ex2()
ex3()
ex4()
ex5()
