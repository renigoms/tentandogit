# 3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o
# jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
# que você gostaria de convidar para jantar. Em seguida, utilize sua lista para
# exibir uma mensagem para cada pessoa, convidando-a para jantar.
print()
convidados_do_jantar = []
print('escolha três pessoas para o jantar.')
cont = 0
while True:
    nomes = input(f'{cont + 1} pessoa: ')
    nomes = nomes.title()
    cont += 1
    convidados_do_jantar.append(nomes)
    if cont == 3:
        break
print(convidados_do_jantar)
print(f'{convidados_do_jantar[0]}, venha jantar comigo.')
print(f'{convidados_do_jantar[1]}, quer jantar comigo?')
print(f'{convidados_do_jantar[2]}, hoje o jantar è comigo. Topa?')
input()
# 3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar
# um novo conjunto de convites. Você deverá pensar em outra pessoa para
# convidar.
# • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
# no final de seu programa, especificando o nome do convidado que não
# poderá comparecer.
# • Modifique sua lista, substituindo o nome do convidado que não poderá
# comparecer pelo nome da nova pessoa que você está convidando.
# • Exiba um segundo conjunto de mensagens com o convite, uma para cada
# pessoa que continua presente em sua lista.

print('Puxa, alguém não vai vim.')
naovaivim = input('QUEM SERÁ?')
naovaivim = naovaivim.title()
localizacao = convidados_do_jantar.index(naovaivim)
convidados_do_jantar.remove(naovaivim)
novapessoa = input(f'QUEM VAI VIM NO LUGAR DE {naovaivim}?')
novapessoa = novapessoa.title()
convidados_do_jantar.insert(localizacao, novapessoa)
print()
print(convidados_do_jantar)
print(f'{convidados_do_jantar[0]}, venha jantar comigo.')
print(f'{convidados_do_jantar[1]}, quer jantar comigo?')
print(f'{convidados_do_jantar[2]}, hoje o jantar è comigo. Topa?')
print()
# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados
# para o jantar.
# • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
# uma instrução print no final de seu programa informando às pessoas que
# você encontrou uma mesa de jantar maior.
# 79
# • Utilize insert() para adicionar um novo convidado no início de sua lista.
# • Utilize insert() para adicionar um novo convidado no meio de sua lista.
# • Utilize append() para adicionar um novo convidado no final de sua lista.
# • Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
# que está em sua lista.

print('EITA, A MESA TEM ESPAÇO PARA MAIS 3 PESSOAS')
cont = 0
while True:
    nomes = input(f'{cont + 1} pessoa: ')
    nomes = nomes.title()
    cont += 1
    if cont == 1:
        convidados_do_jantar.insert(0, nomes)
    elif cont == 2:
        convidados_do_jantar.insert(2, nomes)
    elif cont == 3:
        convidados_do_jantar.append(nomes)
        break

print(f'{convidados_do_jantar[0]},{convidados_do_jantar[2]} e {convidados_do_jantar[-1]} encontrei uma mesa maior '
      f'aqui, venham.')
print(convidados_do_jantar)

input()
# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
# dois convidados.
# • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
# mostre uma mensagem informando que você pode convidar apenas duas
# pessoas para o jantar.
# • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
# que apenas dois nomes permaneçam em sua lista. Sempre que remover um
# nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
# saiba que você sente muito por não poder convidá-la para o jantar.
# • Apresente uma mensagem para cada uma das duas pessoas que continuam
# na lista, permitindo que elas saibam que ainda estão convidadas.
# • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
# tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
# uma lista vazia no final de seu programa.
input()
print('EITA P****, A MESA NÃO VAI CHEGAR A TEMPO!!!!'
      'SÓ VAI TER ESPAÇO PARA DUAS PESSOAS!!!'
      'E AGORA ?')
input()
cont = 0
while True:
    print()
    removido = convidados_do_jantar.pop()
    cont += 1
    print(f'infelismente não deu certo {removido} sinto muito')
    print()

    if cont == 4:
        break

print(f'nova lista: {convidados_do_jantar}')

print('deletando a lista')
del convidados_do_jantar[0]
del convidados_do_jantar[0]
print(convidados_do_jantar)
input()