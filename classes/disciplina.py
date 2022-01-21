class Disciplina:
    def __init__(self, cod_disc, nome_disc, horario_disc, credito_disc):
        self._cod_disc = cod_disc.upper()
        self._nome_disc = nome_disc
        self._horario_disc = horario_disc
        self._credito_disc = credito_disc

    @property
    def cod_disc(self):
        return self._cod_disc

    @property
    def nome_disc(self):
        return self._nome_disc

    @property
    def horario_disc(self):
        return self._horario_disc

    @property
    def credito_disc(self):
        return self._credito_disc

    def __repr__(self):
        return f'código: {self._cod_disc} | {self._nome_disc}, {self.horario_disc} - total de créditos: {self._credito_disc}'
