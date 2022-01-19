class Disciplina:
    def __init__(self, nome_disc, horario_disc, credito_disc):
        self._nome_disc = nome_disc
        self._horario_disc = horario_disc
        self._credito_disc = credito_disc

    @property
    def nome_disc(self):
        return self._nome_disc

    @property
    def horario_disc(self):
        return self._horario_disc

    @property
    def credito_disc(self):
        return self._credito_disc
