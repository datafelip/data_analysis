def pegaStringVazia(texto):
    while True:
        entrada = input(texto)
        if not entrada:
            print("O campo não pode estar vazio")
        else:
            return entrada
def pegaNumeroPositivo(entrada):
    while True:
        try:
            numero = int(input(entrada))
            if not numero or numero < 0:
                raise ValueError
            else:
                return numero
        except ValueError:
            print("Digite uma entrada válida")

