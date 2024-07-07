from tabulate import tabulate
import os
from colorama import Fore, Style, init
import time
import json

init(autoreset=True)

# MENU ------- START

def menu(list):

    enum = 1
    print('\n')
    for item in list:   
        print(f'[{enum}]. {item}')
        enum += 1

    try:
        option = int(input('\nInsira uma opção: '))
        return option
    except:
        print('\nOpção inválida!')
        return menu(list)
    
# MENU --------- END

# CRIAÇÃO DA TABELA ------ START
    
def board_create(dim):

    matrix = []

    for row in range(dim):

        matrix.append([])

        for column in range(dim):

            matrix[row].append('')

    headers = []

    for i in range(1, dim + 1):
        headers.append(i)

    print(tabulate(matrix, headers=headers, tablefmt="heavy_grid", showindex=headers))

    return matrix, headers

# CRIAÇÃO DA TABELA --------- END

# JOGO ------------ START

def game(matrix, headers, dim, check_in_positions=None, check_in_values=None, player_1_sequence=None, player_2_sequence=None, player_1=None, player_2=None, opt_mode=None, counter_1=None, counter_2=None):

    if opt_mode is not None:

        print('Jogo salvo carregado!')

    else:

        #DEFINIÇÃO DO MODO DE JOGO

        print('\nSelecione o modo de jogo')

        opt_mode = menu(['Clássico', 'Especial'])

        #CRIAÇÃO DOS JOGADORES E DISTRIBUIÇÃO DE SEQUÊNCIAS

        sequences = {'Par', 'Impar', 'Ascendente', 'Descendente'}

        player_1_sequence = sequences.pop()
        player_2_sequence = sequences.pop()

        counter_1 = 0
        counter_2 = 0

        player_1 = 1
        player_2 = 0

    #EXIBIR SEQUÊNCIAS

    input(f'\nPressione Enter para exibir a sequência do {Fore.RED}Jogador 1{Fore.RESET}')

    print(f'\nA ordem do {Fore.RED}jogador 1{Fore.RESET} é: {player_1_sequence}.')

    time.sleep(1)
    os.system('cls || clear')
    
    input(f'\nPressione Enter para exibir a sequência do {Fore.BLUE}Jogador 2{Fore.RESET}')

    print(f'\nA ordem do {Fore.BLUE}jogador 2{Fore.RESET} é: {player_2_sequence}.')

    time.sleep(1)
    os.system('cls || clear')

    print(tabulate(matrix, headers=headers, tablefmt="heavy_grid", showindex=headers))

    #COLETA DOS VALORES JÁ PREENCHIDOS
        
    check_in_values = []
    check_in_positions = []

    while True:

        while True:

            #COLETAR POSIÇÃO E VALOR, JUNTO COM TRATAMENTO DE ERROS

            if player_1 > player_2:

                print(Fore.RED + '\n= JOGADOR 1 =' + Style.RESET_ALL)

                #JOGADA ESPECIAL

                if opt_mode == 2 and counter_1 == 0:

                    print('\nSelecione uma jogada')

                    opt_play = menu(['Jogada Normal', 'Jogada Especial', 'Salvar e Sair', 'Sair'])

                    if opt_play == 2:

                        special(matrix, check_in_positions, check_in_values)
                        counter_1 += 1
                        player_2 += 1
                        
                        break

                    if opt_play == 3:

                        save(matrix, headers, dim, player_1, player_1_sequence, counter_1, player_2, player_2_sequence, counter_2, check_in_values, check_in_positions, opt_mode=2)

                    if opt_play == 4:

                        break

                else:

                    print('\nSelecione uma jogada')

                    opt_play = menu(['Jogada Normal', 'Salvar e Sair', 'Sair'])


                    if opt_play == 2:

                        save(matrix, headers, dim, player_1, player_1_sequence, counter_1, player_2, player_2_sequence, counter_2, check_in_values, check_in_positions, opt_mode=1)
                        break

                    if opt_play == 3:

                        break

                try:

                    position_I = int(input('\nInsira a linha: '))
                    position_J = int(input('\nInsira a coluna: '))
                    num = int(input('\nInsira o número: '))

                    pos = (position_I, position_J)
                    
                    if position_I <= dim and position_J <= dim and pos not in check_in_positions and num <= dim * dim and num not in check_in_values:
                        
                        #ATUALIZAÇÃO DA MATRIZ

                        matrix[position_I - 1][position_J - 1] = f"{Fore.RED}" + str(num)
                        tabel = tabulate(matrix, headers=headers, tablefmt="heavy_grid", showindex=headers)

                        player_2 += 1

                        check_in_values.append(num)
                        check_in_positions.append(pos)

                        break

                    else:
                        print("\nEntrada inválida. Tente novamente.")

                except:
                    print('\nInsira um valor correto!')
                            
            else:

                print(Fore.BLUE + '\n= Jogador 2 =' + Style.RESET_ALL)

                if opt_mode == 2 and counter_2 == 0:

                    print('\nSelecione uma jogada')

                    opt_play = menu(['Jogada Normal', 'Jogada Especial', 'Salvar e Sair', 'Sair'])

                    if opt_play == 2:

                        special(matrix, check_in_positions, check_in_values)
                        counter_2 += 1
                        player_1 += 1
                        break
                    
                    if opt_play == 3:

                        save(matrix, headers, dim, player_1, player_1_sequence, counter_1, player_2, player_2_sequence, counter_2, check_in_values, check_in_positions, opt_mode=2)
                        break

                    if opt_play == 4:

                        break

                else:

                    print('\nSelecione uma jogada')

                    opt_play = menu(['Jogada Normal', 'Salvar e Sair', 'Sair'])

                    if opt_play == 2:

                        save(matrix, headers, dim, player_1, player_1_sequence, counter_1, player_2, player_2_sequence, counter_2, check_in_values, check_in_positions, opt_mode=2)
                        
                        break

                    if opt_play == 3:

                        break

                try:

                    position_I = int(input('\nInsira a linha: '))
                    position_J = int(input('\nInsira a coluna: '))
                    num = int(input('\nInsira o número: '))

                    pos = (position_I, position_J)
                    
                    if position_I <= dim and position_J <= dim and pos not in check_in_positions and num <= dim * dim and num not in check_in_values:

                        #ATUALIZAÇÃO DA MATRIZ
                        
                        matrix[position_I - 1][position_J - 1] = f"{Fore.BLUE}" + str(num)
                        tabel = tabulate(matrix, headers=headers, tablefmt="heavy_grid", showindex=headers)

                        player_1 += 1

                        check_in_values.append(num)
                        check_in_positions.append(pos)
                       
                        break

                    else:
                        print("\nEntrada inválida. Tente novamente.")

                except:
                    print('\nInsira um valor correto!')
            
        #FORMATAÇÃO DA MATRIZ - REMOVER ANSI CHARS PARA VALIDAÇÃO

        if opt_play == 2 or opt_play == 3 or opt_play == 4:

            break

        formated = matrix_format(matrix)

        #REUNIR LISTAS DE LINHAS, COLUNAS E DIAGONAIS

        data = get_data(formated, dim)
        
        #VERIFICAÇÃO DE VITÓRIA

        check = win_validation(data, player_1_sequence, player_2_sequence)

        match check:

            case 1:

                print(Fore.RED + 'Jogador 1 venceu!' + Fore.RESET)

                ranking(dim)

                break

            case 2:

                print(Fore.BLUE + 'Jogador 2 venceu!' + Fore.RESET)
               
                ranking(dim)

                break

            case 3:

                print(Fore.WHITE + 'Empate!' + Fore.RESET)

        #IMPRIMIR TABULEIRO

        os.system('cls || clear')

        colored_table = f"{Fore.WHITE}{Style.BRIGHT}{tabel}{Style.RESET_ALL}{Fore.RESET}"

        print(colored_table)

# JOGO -------------- END

# VALIDAÇÕES PARA CADA SEQUÊNCIA ------- START

#1. PAR

def odd_validation(lists):

    for item in lists:

        check = []

        for num in item:

            if int(num) % 2 == 0:

                check.append(int(num))

            else:

                break

        if len(check) == len(item):

            for i in range(len(item) - 1):

                if check[i] + 2 != check[i + 1]:
                    
                    break

            else:

                return True
        
    else:

        return False
    
#2. IMPAR

def even_validation(lists):

    for item in lists:

        check = []

        for num in item:

            if int(num) % 2 == 1:

                check.append(int(num))

            else:

                break

        if len(check) == len(item):

            for i in range(len(item) - 1):

                if check[i] + 2 != check[i + 1]:
                    
                    break

            else:

                return True
    
    else:

        return False
    
#3. ASCENDENTE

def ascending_validation(lists):

    for item in lists:
        for i in range(len(item) - 1):

            if int(item[i]) + 1 != int(item[i + 1]):
                
                break

        else:

            return True
        
    else:

        return False
    
#4. DESCENDENTE

def descending_validation(lists):

    for item in lists:

        for i in range(len(item) - 1):

            if int(item[i]) + 1 != int(item[i + 1]):
                
                break

        else:

            return True
        
    else:

        return False
    
# VALIDAÇÃO GERAL ------- START
    
def win_validation(lists, p1s, p2s):

    #EXCLUSÃO DE LISTAS INCOMPLETAS

    start = len(lists) 

    for i in range(len(lists)):

        for item in lists:

            if '' in item:
                lists.remove(item)

    #JOGADOR 1

    if p1s == 'Par':

        if odd_validation(lists):

            return 1

    elif p1s == 'Impar':

        if even_validation(lists):

            return 1

    elif p1s == 'Ascendente':

        if ascending_validation(lists):

            return 1
        
    elif p1s == 'Descendente':

        if descending_validation(lists):

            return 1
        
    #JOGADOR 2
    
    if p2s == 'Par':
        
        if odd_validation(lists):

            return 2
        
    elif p2s == 'Impar':

        if even_validation(lists):

            return 2
        
    elif p2s == 'Ascendente':

        if ascending_validation(lists):

            return 2
        
    elif p2s == 'Descendente':

        if descending_validation(lists):

            return 2
        
    for lst in lists:

        if any(isinstance(item, str) for item in lst):

            return 0  
        
    return 3  #Empate
        
# VALIDAÇÃO GERAL -------- END

# GERAÇÃO E REUNIÃO DE TODAS AS LISTAS PARA VALIDAÇÃO --------- START
        
def get_data(matrix, dim):

    matrix_i = []
    matrix_j = []
    diagonals = [[], []]

    for i in range(dim):

        matrix_i.append([])
        matrix_j.append([])

        for j in range(dim):

            matrix_i[i].append(matrix[i][j])
            matrix_j[i].append(matrix[j][i])

    counter = 1
    
    for i in range(dim):
        
        diagonals[0].append(matrix_i[i][i])
        diagonals[1].append(matrix_i[i][dim - counter])

        counter += 1

    #Reunir todas as "sub listas" em uma única lista

    all_data = matrix_i + matrix_j + diagonals

    return all_data

# GERAÇÃO E REUNIÃO DE TODAS AS LISTAS PARA VALIDAÇÃO --------- END

# FORMATAÇÃO DA MATRIX PARA EXCLUSÃO DE ANSI CHARS -------- START

def matrix_format(matrix):

    formated = []

    for row in range(len(matrix)):

        formated.append([])

        for column in range(len(matrix)):

            formated[row].append('')

    for i, item in enumerate(matrix):

        for j, char in enumerate(item):

            if isinstance(char, str):

                try:

                    formated[i][j] = int(char[-1])

                except:

                    formated[i][j] = char

    return formated

# FORMATAÇÃO DA MATRIX PARA EXCLUSÃO DE ANSI CHARS --------- END

# JOGADA ESPECIAL - LIMPAR UMA LINHA OU COLUNA --------- START

def special(matrix, check_in_positions, check_in_values):

    opt = menu(['Linha', 'Coluna'])

    try:

        opt_index = int(input('\nInsira o índice que deseja remover: '))

        if opt_index > len(matrix):

            print('\nValor inválido!')
            return special(matrix)

    except:

        print('\nValor inválido!')
        return special(matrix)

    match opt:

        case 1:

            for i in range(len(matrix)):

                try:
                    check_in_values.remove(int(matrix[opt_index - 1][i][-1]))
                    check_in_positions.remove((opt_index, i + 1))

                except:
                    pass

                matrix[opt_index - 1][i] = ''
                

        case 2:

            for i in range(len(matrix)):

                try:
                    check_in_values.remove(matrix[i][opt_index - 1][-1])
                    check_in_positions.remove((i + 1, opt_index))

                except:
                    pass

                matrix[i][opt_index - 1] = ''

    return matrix

def save(matrix, headers, dim, p1, p1s, c1, p2, p2s, c2, values, positions, opt_mode):

    game_data = {
        "matrix": matrix,
        "headers":headers,
        "dimension":dim,
        "check_in_positions": positions,
        "check_in_values": values,
        "player_1_sequence": p1s,
        "player_2_sequence": p2s,
        "player_1": p1, 
        "player_2": p2,
        "opt_mode": opt_mode,
        "counter_1": c1,
        "counter_2": c2
    }

    with open("saved_game.json", "w", encoding='utf-8') as f:
        json.dump(game_data, f, indent=4)

    print("\nJogo salvo!")

def load():

    try:
        with open("saved_game.json", "r", encoding='utf-8') as f:
            game_data = json.load(f)

        matrix = game_data["matrix"]
        headers = game_data["headers"]
        check_in_positions = game_data["check_in_positions"]
        check_in_values = game_data["check_in_values"]
        player_1_sequence = game_data["player_1_sequence"]
        player_2_sequence = game_data["player_2_sequence"]
        player_1 = game_data["player_1"]
        player_2 = game_data["player_2"]
        counter_1 = game_data["counter_1"]
        counter_2 = game_data["counter_2"]
        opt_mode = game_data["opt_mode"]
        dim = game_data["dimension"]

        return matrix, headers, dim, check_in_positions, check_in_values, player_1_sequence, player_2_sequence, player_1, player_2, opt_mode, counter_1, counter_2

    except FileNotFoundError:
        print("\nVocê não possui jogos salvos!")
        return None, None, None, None, None, None, None, None, None
    
def ranking(difficulty):

    try:

        with open("ranking.json", "r") as f:

            ranking_data = json.load(f)

    except FileNotFoundError:

        ranking_data = {}

    player_name = input("\nInsira o nome do jogador ganhador: ")

    if player_name not in ranking_data:

        ranking_data[player_name] = {"score": 0}

    if difficulty == 3:

        points = 5

    elif difficulty == 4:

        points = 10

    elif difficulty == 5:

        points = 15

    else:

        points = 0

    ranking_data[player_name]["score"] += points

    with open("ranking.json", "w") as f:
        json.dump(ranking_data, f, indent=4)

    print(f"\nRanking atualizado! {player_name} agora possui {ranking_data[player_name]['score']} pontos.")

def display_ranking():

    try:

        with open("ranking.json", "r") as f:

            ranking_data = json.load(f)

        sorted_ranking = sorted(ranking_data.items(), key=lambda item: item[1]["score"])

        print("\nRanking:")

        for player, data in sorted_ranking:

            print(f"{player} - {data['score']}")

    except FileNotFoundError:

        print("\nSem dados de ranqueamento ainda.")