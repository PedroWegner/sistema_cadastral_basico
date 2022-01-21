from classes.disciplina import Disciplina
from classes.aluno import Aluno
from classes.endereco import Endereco
from itertools import count
from sys import exit

lista_aluno = []
id_aluno = count(1)


def show_menu():
    print('---MENU---'
          '\n\t1 - cadastrar aluno'
          '\n\t2 - cadastrar disciplina em aluno'
          '\n\t3 - descadastrar um aluno'
          '\n\t4 - descadastrar disciplina de um aluno'
          '\n\t5 - atualizar cadastro de aluno'
          '\n\t6 - exibir alunos e disciplinas'
          '\n\t7 - mostrar alunos'
          '\n\t00 - sair')
    op = input('digite uma operação: ')
    menu(op)


def menu(op):
    if op == '1':
        cadastrar_aluno()
    elif op == '2':
        cadastra_disciplina()
    elif op == '3':
        descadastrar_aluno()
    elif op == '4':
        descadastrar_disciplina()
    elif op == '5':
        update_aluno()
    elif op == '6':
        show_aluno_disciplina()
    elif op == '7':
        show_alunos()
    elif op == '00':
        print('saindo...')
        exit()
    else:
        print('Operação desconhecida')


def cadastrar_aluno():
    print('---DADOS DO ALUNO---')
    nome = input('\tnome: ')
    nascimento = input('\tdata de nascimento: ')
    curso = input('\tcurso: ')
    periodo = input('\tperiodo: ')
    print('---ENDERECO DO ALUNO---')
    rua = input('\trua: ')
    numero = input('\tnumero: ')
    bairro = input('\tbairro: ')
    cidade = input('\tcidade: ')
    cep = input('\tcep: ')
    aluno = Aluno(next(id_aluno), nome, nascimento, curso, periodo, Endereco(rua, numero, bairro, cidade, cep))
    lista_aluno.append(aluno)

def descadastrar_aluno():
    aluno_aux = get_aluno()
    lista_aluno.remove(aluno_aux)

def show_alunos():
    if not lista_aluno:
        print("Não há alunos cadastrados")
        return
    for aluno in lista_aluno:
        aluno.get_informacao()


def cadastra_disciplina():
    aluno_aux = get_aluno()
    if not aluno_aux:
        print('Não há aluno cadastrado com o id digitado')
        return
    cod_disc = input('código da disciplina: ')
    nome_disc = input('disciplina: ')
    hora_disc = input('horario: ')
    cred_disc = input('creditos: ')
    aluno_aux.add_disciplina(Disciplina(cod_disc, nome_disc, hora_disc, cred_disc))

def descadastrar_disciplina():
    aluno_aux = get_aluno()
    print(f'Disciplinas do aluno {aluno_aux.nome_aluno}')
    aluno_aux.get_disciplinas()
    cod_disc = input('código da disciplina: ')
    aluno_aux.remove_disciplina(cod_disc)
    print('disciplina descadastrada')


def update_aluno():
    aluno_aux = get_aluno()
    if not aluno_aux:
        print('Não há aluno cadastrado com o id digitado')
        return
    print('\t1 - alterar dados pessoais'
          '\n\t2 - alterar curso'
          '\n\t3 - alterar endereço')
    ope = input('digite uma operação: ')
    if ope == '1':
        update_aluno_pessoal(aluno_aux)
    elif ope == '2':
        update_aluno_curso(aluno_aux)
    elif ope == '3':
        update_aluno_endereco(aluno_aux)
    else:
        print('Operação não definida')
        return
    print('---ATUALIZAÇÃO COMPLETA---')


def update_aluno_pessoal(aluno):
    print('---ATUALIZAR INFORMAÇÕES PESSOAIS---')
    nome = input('\tnome :')
    data_nasc = input('\tdata de nascimento: ')
    aluno.update_pessoal(nome, data_nasc)


def update_aluno_curso(aluno):
    print('---ATUALIZAR CURSO---')
    curso = input('\tcurso: ')
    periodo = input('\tperiodo: ')
    aluno.update_curso(curso, periodo)

def update_aluno_endereco(aluno):
    print('---ATUALIZAR ENDEREÇO---')
    rua = input('\trua: ')
    numero = input('\tnumero: ')
    bairro = input('\tbairro: ')
    cidade = input('\tcidade: ')
    cep = input('\tcep: ')
    aluno.update_endereco_alu(rua, numero, bairro, cidade, cep)

def get_aluno_by_id(id):
    for aluno in lista_aluno:
        if aluno.id_aluno == id:
            return aluno
    return False


def get_aluno():
    if not lista_aluno:
        print("Não há alunos cadastrados")
        return
    for aluno in lista_aluno:
        aluno.get_nome_id()
    id_aux = input('escolha um aluno: ')
    return get_aluno_by_id(int(id_aux))


def show_aluno_disciplina():
    if not lista_aluno:
        print("Não há alunos cadastrados")
        return
    for aluno in lista_aluno:
        aluno.get_disciplinas()


while True:
    show_menu()
