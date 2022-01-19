class Endereco:
    def __init__(self, rua, numero, bairro, cidade, cep):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._cep = cep

    @property
    def rua(self):
        return self._rua

    @property
    def numero(self):
        return self._numero

    @property
    def bairro(self):
        return self._bairro

    @property
    def cidade(self):
        return self._cidade

    @property
    def cep(self):
        return self._cep

    def update_endereco(self, rua, numero, bairro, cidade, cep):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._cep = cep
