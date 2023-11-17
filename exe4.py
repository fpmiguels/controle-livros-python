# Criando uma lista e variáveis globais
lista_livros = []           # lista de livros vazia
id_global = 0
# Função de cadastro do livro
def cadastrar_livros(id):             
    print('Bem-vindo ao menu de cadastrar livros')
    print('ID do livro : {}'.format(id))    
    nome = input ('Digite o nome do livro: ')
    autor = input ('Digite o nome do autor: ')
    editora = input ('Digite o nome da editora: ')    
    dicionario_livro = {'id': id , 'nome': nome, 'autor': autor, 'editora': editora} # adicionando um dicionario a lista    
    lista_livros.append(dicionario_livro.copy())    
# Função para consultar livros 
def consultar_livros():                         
    print('Bem-vindo ao menu para consultar livros')
    print('1 - Consultar todos os livros')
    print('2 - Consultar livro por id')
    print('3 - Consultar livro(s) por autor')
    print('4 - Retornar ')    
    while True:        
        resposta_consulta = input ('>> ')        
        if resposta_consulta == '1':
            print('Você escolheu consultar todos os livros')
            for livro in lista_livros:
                for key, value in livro.items():           # Retorna os livros cadastrados na lista
                    print('{} : {}' .format(key, value))
            print('----------------------------------------')
            return consultar_livros() #adicionando return para voltar ao menu consulta ao livro  
        elif resposta_consulta == '2':
            print('Você escolheu consultar livro por id')
            opção_desejada = int(input('Digite o id:  '))       
            for livro in lista_livros:
                if livro['id'] == opção_desejada:
                    for key, value in livro.items():           # retorna o livro consultado por id
                        print('{} : {}' .format(key, value))
            print('----------------------------------------')
            return consultar_livros()        # retorna para o menu consulta livro
        elif resposta_consulta == '3':
            print('Você escolheu consultar livro por autor')
            opção_desejada = input('Digite o autor:  ')
            for livro in lista_livros:
                if livro['autor'] == opção_desejada:
                    for key, value in livro.items():         # retorna o(s) livro(s) consultado por autor
                        print('{} : {}' .format(key, value))
            print('----------------------------------------')
            return consultar_livros()       # retorna para o menu consulta livro 
        elif resposta_consulta == '4':
            return        # retorna ao menu principal
        else:
            print('Opção inválida, tente novamente')
            continue        
# Função remover livros
def remover_livros():                                  
    print('Bem-vindo ao menu para remover livros')    
    opção_desejada = int (input('Digite o id do livro: '))    
    for livro in lista_livros:        
        if livro ['id'] == opção_desejada:
            lista_livros.remove(livro)     #remover livro da lista
# Inicio do main
print('Bem vindo ao controle de livros do Felipe Miguel da Silva')     
while True:
    print ('         Escolha uma opção desejada          ')            
    print('1 - Cadastrar livro')
    print('2 - Consultar livro')
    print('3 - Remover livro')
    print('4 - Encerrar programa')
    menu_cadastro = input('>> ')    
    if menu_cadastro == '1':
        id_global = id_global + 1
        cadastrar_livros(id_global)    
    elif menu_cadastro == '2':
        consultar_livros()
    elif menu_cadastro == '3':
        remover_livros()
    elif menu_cadastro == '4':
        print('Programa encerrado')
        break # encerra o programa
    else:
        print('Opção inválida. Tente novamente')
        continue