def soma(dado_um, dado_dois):
    return dado_um + dado_dois
	
def quadrado(numero):
    resultado = numero * numero
    return resultado
    
def soma_quadrados(num_um, num_dois, num_tres):
    prim_valor = quadrado(num_um)
    seg_valor  = quadrado(num_dois)
    terc_valor = quadrado(num_tres)
    
    return prim_valor + seg_valor  + terc_valor

def media(dados):
    soma = 0.0
    for r in dados:
        soma += r
    return soma / len(dados)

def variancia(dados):
    m = media(dados)
    var = 0.0
    for r in dados:
        var += (r - m) ** 2
    return var / (len(dados) -1)