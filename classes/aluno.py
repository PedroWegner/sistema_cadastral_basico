from datetime import date


class Aluno:
    def __init__(self, id_aluno, nome_aluno, nasc_aluno, periodo_aluno, curso_aluno, endereco_aluno):
        self._id_aluno = id_aluno
        self._nome_aluno = nome_aluno
        self._nasc_aluno = nasc_aluno
        self._curso_aluno = curso_aluno
        self._periodo_aluno = periodo_aluno
        self._endereco_aluno = endereco_aluno
        self._lista_disciplinas = []

    @property
    def id_aluno(self):
        return self._id_aluno

    @property
    def nome_aluno(self):
        return self._nome_aluno

    @property
    def curso_aluno(self):
        return self._curso_aluno

    @property
    def periodo_aluno(self):
        return self._periodo_aluno

    @property
    def nasc_aluno(self):
        return self._nasc_aluno

    @property
    def endereco_aluno(self):
        return self._endereco_aluno

    def add_disciplina(self, disciplina):
        self._lista_disciplinas.append(disciplina)

    def remove_disciplina(self, disciplina):
        self._lista_disciplinas.remove(disciplina)

    def separa_data(self):
        separado = self._nasc_aluno.split('/')
        return separado

    def get_idade(self):
        ano_atual = date.today()
        ano_separado = self.separa_data()
        ano = ano_separado[2]
        mes = ano_separado[1]
        dia = ano_separado[0]
        ano_nascimento = date(int(ano), int(mes), int(dia))
        idade = ano_atual.year - ano_nascimento.year - (
                (ano_atual.month, ano_atual.day) < (ano_nascimento.month, ano_nascimento.day))
        return idade

    def get_nome_id(self):
        print(f'\tid_aluno: {self._id_aluno} - nome: {self._nome_aluno}')

    def get_disciplinas(self):
        self.get_nome_id()
        if not self._lista_disciplinas:
            print("\tNão há disciplinas cadastradas")
            return
        for disciplina in self._lista_disciplinas:
            print(f'\t{disciplina}')

    def get_informacao(self):
        print(f'\tid_aluno: {self._id_aluno}'
              f'\n\tnome: {self._nome_aluno}'
              f'\n\tidade: {self.get_idade()}'
              f'\n\tcurso: {self._curso_aluno}'
              f'\n\tperiodo: {self._periodo_aluno}'
              f'\n\tENDERECO:'
              f'\n\t{self._endereco_aluno}')
