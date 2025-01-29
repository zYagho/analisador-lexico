from automata.fa.Moore import Moore
#from moore import Moore
import sys, os

from myerror import MyError

from elementos_moore import estados, alfabeto_entrada, alfabeto_saida, transicoes, tabela_saida, transicoes_iniciais, estado_inicial
error_handler = MyError('LexerErrors')

global check_cm
global check_key

# moore = Moore(  estados,
#                 alfabeto_entrada,
#                 alfabeto_saida,
#                 transicoes,
#                 estado_inicial,
#                 tabela_saida
#                )

moore = Moore(
        estados,
        alfabeto_entrada,
        alfabeto_saida,
        transicoes,
        estado_inicial,
        tabela_saida
              )

def main():
    check_cm = False
    check_key = False
    
    for idx, arg in enumerate(sys.argv):
        aux = arg.split('.')
        if aux[-1] == 'cm':
            check_cm = True
            idx_cm = idx

        if(arg == "-k"):
            check_key = True

    # print ("No. of arguments passed is ", len(sys.argv))
    #print(transicoes_iniciais)
    #print(transicoes)
    if(len(sys.argv) < 3):
        raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

    if not check_cm:
      raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
    elif not os.path.exists(sys.argv[idx_cm]):
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
    else:
        data = open(sys.argv[idx_cm])
        source_file = data.read()
        
        if(set(source_file) - set(alfabeto_entrada)):
            raise IOError(error_handler.newError(check_key, 'ERR-LEX-CARACTER-NOT-ALLOWED'))
        
        if check_cm:
            print("Definição da Máquina")
            #print(moore)
            print("Entrada:")
            print(source_file)
            print("Lista de Tokens:")

            print(moore.get_output_from_string(source_file))
            #resultado = moore.get_output_from_string(source_file)

if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e)
    except (ValueError, TypeError) as e:
        print(e)