#CRIAÇÃO DO TABULEIRO

def Board_create(dim):

    matrix = {}

    while len(matrix.values()) < 25:

        #COLETAR CHAVE (POSIÇÃO) E VALOR (NÚMERO JOGADO)

        try:

            position_I = int(input('Insira a linha: '))
            position_J = int(input('Insira a coluna: '))
            num = int(input('Insira o número: '))

        except:

            print('Insira um valor correto!')
            return Board_create(dim)
        
        if position_I > dim:
            print('Linha inválida!')
            return Board_create(dim)

        elif position_J > dim:
            print('Coluna inválida!')
            return Board_create(dim)

        elif num > dim * dim:
            print('Número inválido!')
            return Board_create(dim)

        #ATUALIZAR MATRIZ

        position = (position_I - 1, position_J - 1)

        matrix.update({position: num})

        for row in range(dim):
            for column in range(dim):
                
                if column == dim - 1:
                    print(matrix.get((row, column), ' '), )
                
                else:
                    print(matrix.get((row, column), ' '), end=' ')

#VALIDAÇÃO DE VITÓRIA                    

def Win_Validation(dim, matrix):

    for row in range(dim):
        for column in range(dim):
            pass