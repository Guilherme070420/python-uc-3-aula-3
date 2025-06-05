tamanho = int(input('informe o tamanho:'))
def parte_um(tamanho):
    for _ in range(tamanho):
        print('*' * tamanho)

def parte_dois(tamanho):
    meio = tamanho // 2
    for i in range (tamanho):

        for j in range(tamanho):
            if i == meio and j == meio:
                linha = ' '
        else:
            linha = '*'
    print(linha)  
parte_dois(tamanho)    

def parte_tres(tamanho):
    altura=tamanho//2
    for i in range(altura + 1):
        espaços=(altura - 1)
        asteristicos = '*' * (2*i+1)
        print(espaços+ asteristicos + espaços) 

parte_tres(tamanho)