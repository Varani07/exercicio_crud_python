class EnderecoVO:
    def __init__(self, rua, numero, bairro, cidade, estado, cep, pessoa_id, endereco_principal):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.pessoa_id = pessoa_id
        self.endereco_principal = endereco_principal

    def to_dict(self):
        return {
            "rua": self.rua,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "cep": self.cep,
            "pessoa_id": self.pessoa_id,
            "endereco_principal": self.endereco_principal
        }