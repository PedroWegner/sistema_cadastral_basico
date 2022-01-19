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
          '\n\t50 - mostrar alunos'
          '\n\t100 - sair')
    op = input('digite uma operação: ')
    menu(op)


def menu(op):
    if op == '1':
        cadastrar_aluno()
    elif op == '2':
        pass
    elif op == '50':
        show_alunos()
    elif op == '100':
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


def show_alunos():
    for aluno in lista_aluno:
        aluno.get_informacao()


while True:
    show_menu()
