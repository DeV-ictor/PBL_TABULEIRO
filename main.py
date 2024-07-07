import module
import os
import time

while True:

    opt_start = module.menu(['Novo Jogo', 'Carregar', 'Ranking', 'Regras','Sair'])

    match opt_start:

        case 1:

            print('Escolha a dificuldade')

            opt_difficulty = module.menu(['3 x 3', '4 x 4', '5 x 5', 'Voltar'])

            dimension = opt_difficulty + 2

            match opt_difficulty:

                case 4:

                    breakpoint

                case _:

                    matrix, headers = module.board_create(dimension)
                    module.game(matrix, headers, dimension)

        case 2:
            
            print('Gostaria de carregar último jogo salvo?')

            opt_load = module.menu(['Sim', 'Não'])

            match opt_load:

                case 1:

                    matrix, headers, dim, player_1, player_1_sequence, counter_1, player_2, player_2_sequence, counter_2, check_in_values, check_in_positions, opt_mode = module.load()
                    module.game(matrix, headers, dim, player_1, player_1_sequence, counter_1, player_2, player_2_sequence, counter_2, check_in_values, check_in_positions, opt_mode)

                case 2:

                    breakpoint

        case 3:

            module.display_ranking()

            input('\nPressione Enter para voltar.')
            os.system('cls || clear')
            breakpoint

        case 4:
            
            os.system('cls || clear')
            print('\nO jogo em questão trata-se de um jogo de tabuleiro com o objetivo de realizar sequências que serão previamente definidas.')

            time.sleep(5)

            print('\n1. As sequências são:')
            print('\n   Sequência Ascendente: 1, 2, 3 ou 4, 5, 6.')
            print('   Sequência Descendente: 9, 8, 7 ou 6, 5, 4.')
            print('   Sequência Pares: 2, 4, 6 ou 8, 6, 4.')
            print('   Sequência Ímpares: 1, 3, 5 ou 7, 5, 3.')

            time.sleep(10)

            print('\n2. Os valores inseridos não podem ser repetidos.')

            time.sleep(5)

            print('\n3. O jogo apresenta 2 modos: Modo Clássico e Modo Especial')

            time.sleep(5)

            print('\nO modo Clássico é o modo sem nenhuma funcionalidade extra e envolve apenas montar as sequências definidas, sem qualquer auxílio além da sua própria habilidade!')

            time.sleep(7)

            print('\nO modo Especial envolve o mesmo objetivo, porém você pode contar com uma jogada coringa que tem o poder de limpar uma linha ou coluna de sua preferência.')

            time.sleep(7)

            print('\n !!! AVISO ESTRITAMENTE IMPORTANTE !!!')

            time.sleep(3)

            print('\nO jogo proporciona altas doses de diversão. Contenha-se!')

            time.sleep(5)

            input('\nPressione Enter para voltar')
            os.system('cls || clear')
            breakpoint

        case 5:

            break