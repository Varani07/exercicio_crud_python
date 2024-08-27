class PessoaVO:
    def __init__(self, nome, cpf, data):
        self.nome = nome
        self.cpf = cpf
        self.data = data

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "data": self.data
        }