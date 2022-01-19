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
          '\n\t60 - exibir alunos e disciplinas'
          '\n\t50 - mostrar alunos'
          '\n\t100 - sair')
    op = input('digite uma operação: ')
    menu(op)


def menu(op):
    if op == '1':
        cadastrar_aluno()
    elif op == '2':
        cadastra_disciplina()
    elif op == '60':
        show_aluno_disciplina()
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
    if not lista_aluno:
        print("Não há alunos cadastrados")
        return
    for aluno in lista_aluno:
        aluno.get_informacao()


def cadastra_disciplina():
    if not lista_aluno:
        print("Não há alunos cadastrados")
        return
    for aluno in lista_aluno:
        aluno.get_nome_id()
    id_aux = input('escolha um aluno: ')
    aluno_aux = get_aluno_by_id(int(id_aux))
    if not aluno_aux:
        print(f'Não há aluno cadastrado com o id {id_aux}')
    else:
        nome_disc = input('disciplina: ')
        hora_disc = input('horario: ')
        cred_disc = input('creditos: ')
        aluno_aux.add_disciplina(Disciplina(nome_disc, hora_disc, cred_disc))


def get_aluno_by_id(id):
    for aluno in lista_aluno:
        if aluno.id_aluno == id:
            return aluno
    return False

def show_aluno_disciplina():
    if not lista_aluno:
        print("Não há alunos cadastrados")
        return
    for aluno in lista_aluno:
        aluno.get_disciplinas()

while True:
    show_menu()
