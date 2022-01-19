from datetime import date

class Aluno:
    def __init__(self, id_aluno, nome_aluno, curso_aluno, periodo_aluno, nasc_aluno, endereco_aluno):
        self._id_aluno = id_aluno
        self._nome_aluno = nome_aluno
        self._curso_aluno = curso_aluno
        self._periodo_aluno = periodo_aluno
        self._nasc_aluno = nasc_aluno
        self._endereco_aluno = endereco_aluno
        self.lista_disciplinas = []

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
        self.lista_disciplinas.append(disciplina)

    def remove_disciplina(self, disciplina):
        self.lista_disciplinas.remove(disciplina)

    def get_idade(self):
        ano_atual = date.today()
        return ano_atual.year - self._nasc_aluno - ((ano_atual.month, ano_atual.day) <(self._nasc_aluno.month, self._nasc_aluno.day))
    