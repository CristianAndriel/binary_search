from typing import List

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    ## baixo e alto acompanham a parte da lista que você está procurando

    ## Enquanto ainda não achou o item, continua procurando
    while baixo <= alto:
        meio = (baixo + alto) / 2
        chute = lista[meio]

        ## Se o chute for o item, você encontrou o item
        if chute == item:
            return meio
        ## Se o chute for maior que o item, você precisa procurar na parte inferior da lista
        if chute > item:
            alto = meio -1
        ## Se o chute for menor que o item, você precisa procurar na parte superior da lista
        else:
            baixo = meio + 1
    return None 
    ## Se não achou o item, retorna None


# Testando a função
    minha_lista = [1, 3, 5, 7, 9]
    print(pesquisa_binaria(minha_lista, 3)) # => 1
    print(pesquisa_binaria(minha_lista, -1)) # => None
