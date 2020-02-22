import datetime
placa = ''
lista_de_entradas = []

# Os carros que entraram e sairam
todas = []

at = []
atu = []


def placas():
    """
    :author Roberto Weller
    :return Não um retorno especifico, mas um precesso simples de saida e entrada de carros num estacionnamento:
    """
    agora = datetime.datetime.now()
    while True:

        # Se for usado segundos.
        # segudos = agora.second

        placa = input('Digite sua placa, por favor >> ')

        # Me retorna a horas em str.
        agora = datetime.datetime.now()
        agora_str = str(agora.time())[0:5]

        # Se o carro ja esta dentro vai registrar saida.
        if placa in lista_de_entradas:
            acha = lista_de_entradas.index(placa)
            lista_de_entradas.insert(acha + 2, agora_str)
            print(f'O carro de placa {lista_de_entradas[acha]} entrou as {lista_de_entradas[acha + 1]} e saiu as {lista_de_entradas[acha + 2]}')

            # Atualiza minha lista com a saida e entrada.
            atu.append(f'O carro de placa {lista_de_entradas[acha]} entrou as {lista_de_entradas[acha + 1]} e saiu as {lista_de_entradas[acha + 2]}')
            # Registra os carros que ja sairam.
            for i in range(0, 3):
                todas.append(lista_de_entradas[acha + i])
            try:

                for i in range(0, 3):
                    lista_de_entradas.remove(lista_de_entradas[acha + i])

            except IndexError:
                pass

        if placa not in lista_de_entradas and placa != 'saidas':
            lista_de_entradas.append(placa)
            lista_de_entradas.append(agora_str)

        if placa == 'saidas':
            # Da um for em todos os carros que entraram e sairam. (Nota: os que não sairam n aparece aqui).
            for uu in atu:
                print(f'{uu}')

        at.append(f'O carro {lista_de_entradas[len(lista_de_entradas)-2]} entrou as {lista_de_entradas[len(lista_de_entradas) - 1]} e não saiu ainda...')
        # print(atu)
        # for u in at:
        # print(u)

        # Me atualiza os carros que não saiaram ainda.
        # print(f'O carro de placa {lista_de_entradas[u]} entrou as {lista_de_entradas[u]} não saiu ainda.')
        # print(todas)
        # print(lista_de_entradas)


if __name__ == '__main__':
    placas()
