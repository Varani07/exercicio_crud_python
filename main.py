import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pessoaDAO import PessoaDAO
from pessoaVO import PessoaVO
from enderecoVO import EnderecoVO
from enderecoDAO import EnderecoDAO

def iniciar():
    os.system("cls")
    answer = 1
    while 0 < answer < 4:
        print()
        print("-------- EXERCÍCIO CRUD --------")
        print()
        print()
        print("[1] Cadastrar")
        print("[2] Visualizar Dados Cadastrados")
        print("[3] Sair")
        print()
        try:
            answer = int(input("Escolha uma opção: "))
            os.system("cls")
        except ValueError as e:
            os.system("cls")
            print("-----------------------------")
            print("| DIGITE UM CARACTER VÁLIDO |")
            print("-----------------------------")
            print()
            continue
        if answer == 1:
            if cadastrar() == 4:
                break
        elif answer == 2:
            if visualisar() == 4:
                break
        elif answer == 3:
            break
        else:
            os.system("cls")
            print("---------------------------")
            print("| DIGITE UM NUMERO VÁLIDO |")
            print("---------------------------")
            print()
            answer = 1
            continue


def cadastrar():
    tela = "Cadastro de Pessoas"

    answer = 1
    nome = ""
    data_nascimento = ""
    cpf = ""
    id_pessoa = 0
    idade = ""

    numero = ""
    rua = ""
    bairro = ""
    cidade = ""
    estado = ""
    cep = ""
    endereco_principal = True

    while 0 < answer < 13:
        pre_requesito_nome = " "
        if nome == "":
            pre_requesito_nome = "*"

        pre_requesito_cpf = " "
        if cpf == "":
            pre_requesito_cpf = "*"

        pre_requesito_rua = " "
        if rua == "":
            pre_requesito_rua = "*"

        pre_requesito_numero = " "
        if numero == "":
            pre_requesito_numero = "*"

        pre_requesito_bairro = " "
        if bairro == "":
            pre_requesito_bairro = "*"

        pre_requesito_cidade = " "
        if cidade == "":
            pre_requesito_cidade = "*"

        pre_requesito_estado = " "
        if estado == "":
            pre_requesito_estado = "*"

        pre_requesito_cep = " "
        if cep == "":
            pre_requesito_cep = "*"

        print()
        print("-------- Cadastro de Pessoas --------")
        print()
        print()
        print(f"[1] {pre_requesito_nome}Nome: {nome}")
        print(f"[2]  Data de Nascimento: {data_nascimento}  | Idade: {idade}")
        print(f"[3] {pre_requesito_cpf}CPF: {cpf}")
        print()
        print(f"[4] {pre_requesito_rua}Rua: {rua}")
        print(f"[5] {pre_requesito_numero}Numero: {numero}")
        print(f"[6] {pre_requesito_bairro}Bairro: {bairro}")
        print(f"[7] {pre_requesito_cidade}Cidade: {cidade}")
        print(f"[8] {pre_requesito_estado}Estado: {estado}")
        print(f"[9] {pre_requesito_cep}CEP: {cep}")
        print()
        print()
        print("[10] Cadastrar Pessoa")
        print("[11] Voltar")
        print("[12] Sair")
        print()

        try:
            answer = int(input("Escolha uma opção: "))
            os.system("cls")

        except ValueError as e:
            os.system("cls")
            print("-----------------------------")
            print("| DIGITE UM CARACTER VÁLIDO |")
            print("-----------------------------")
            print()
            continue

        if answer == 1:
            nome = cadastrar_nome(tela)
            if nome == 4:
                return 4
            
        elif answer == 2:
            data_nascimento, idade = cadastrar_data_nascimento(tela)
            if data_nascimento == 4:
                return 4
            
        elif answer == 3:
            cpf = cadastrar_cpf(tela)
            if cpf == 4:
                return 4
            
        elif answer == 4:
            rua = cadastrar_rua(tela)
            if rua == 4:
                return 4
            
        elif answer == 5:
            numero = cadastrar_numero(tela)
            if numero == "sair":
                return 4

        elif answer == 6:
            bairro = cadastrar_bairro(tela)
            if bairro == 4:
                return 4

        elif answer == 7:
            cidade = cadastrar_cidade(tela)
            if cidade == 4:
                return 4

        elif answer == 8:
            estado = cadastrar_estado(tela)
            if estado == 4:
                return 4

        elif answer == 9:
            cep = cadastrar_cep(tela)
            if cep == 4:
                return 4

        elif answer == 10:
            if nome == "" or cpf == "" or numero == "" or bairro == "" or cidade == "" or estado == "" or estado == "" or cep == "":
                os.system("cls")
                print("-----------------------------------------")
                print("| PREENCHA TODOS OS CAMPOS QUE CONTÉM * |")
                print("-----------------------------------------")
                print()
                continue

            else:
                date = None
                if data_nascimento != "":
                    date = datetime.strptime(data_nascimento, "%d/%m/%Y")

                pVO = PessoaVO(nome, cpf, date)
                dao = PessoaDAO()
                dao.cadastrar_pessoas(pVO.to_dict())

                id_pessoa_dao = PessoaDAO()
                result = id_pessoa_dao.get_id_pessoas(cpf)
                for item in result:
                    id_pessoa = int(item)
                eVO = EnderecoVO(rua, numero, bairro, cidade, estado, cep, id_pessoa, endereco_principal)
                end_dao = EnderecoDAO()
                end_dao.cadastrar_enderecos(eVO.to_dict())

                answer = 1
                nome = ""
                data_nascimento = ""
                cpf = ""
                id_pessoa = 0
                idade = ""

                numero = ""
                rua = ""
                bairro = ""
                cidade = ""
                estado = ""
                cep = ""

        elif answer == 11:
            break

        elif answer == 12:
            return 4
        
        else:
            os.system("cls")
            print("---------------------------")
            print("| DIGITE UM NUMERO VÁLIDO |")
            print("---------------------------")
            print()
            answer = 1
            continue

def cadastrar_nome(tela):
    nome = ""
    while nome == "":
        print()
        print(f"-------- {tela} --------")
        print()
        print("[1] Voltar")
        print("[2] Sair")
        print()
        nome = input("Nome: ")

        try:
            num = int(nome)
            os.system("cls")
            if num == 1:
                nome = ""
                return nome
            elif num == 2:
                nome = ""
                return 4
            else:
                nome = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue
        except ValueError as e:
            os.system("cls")
            if len(nome) > 100:
                nome = ""
                print("----------------------------------")
                print("| NOME COM EXCESSO DE CARACTERES |")
                print("----------------------------------")
                print()
                continue
            else:
                return nome
            
def cadastrar_data_nascimento(tela):
    data= ""
    while data == "":
        difference_in_years = ""
        data_formato_certo = True
        print()
        print(f"-------- {tela} --------")
        print()
        print("[1] Voltar")
        print("[2] Sair")
        print()
        data = input("Data de Nascimento (dd/mm/yyyy): ")

        try:
            num = int(data)
            os.system("cls")
            if num == 1:
                data = ""
                return data, difference_in_years  
            
            elif num == 2:
                data = ""
                return 4, ""
            
            else:
                data = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue

        except ValueError as e:
            os.system("cls")

            if len(data) > 10:
                data = ""
                print("---------------------------------")
                print("| DATA COM EXCESSO DE CARACTERES |")
                print("---------------------------------")
                print()
                continue

            elif len(data) < 10:
                data = ""
                print("------------------------------------")
                print("| PREENCHA O CAMPO CONFORME MODELO |")
                print("------------------------------------")
                print()
                continue

            else:
                i = 0
                for char in data:
                    if 0 <= i < 2 or 2 < i < 5 or 5 < i < 10:
                        try:
                            int(char)
                        except ValueError as e:
                            data = ""
                            print("------------------------------------")
                            print("| PREENCHA O CAMPO CONFORME MODELO |")
                            print("------------------------------------")
                            print()
                            data_formato_certo = False
                            break
                    elif i == 2 and char != "/" or i == 5 and char != "/":
                        data = ""
                        print("------------------------------------")
                        print("| PREENCHA O CAMPO CONFORME MODELO |")
                        print("------------------------------------")
                        print()
                        data_formato_certo = False
                        break
                    i += 1
                if data_formato_certo:
                    aniversario = datetime.strptime(data, "%d/%m/%Y")
                    hoje = datetime.now()
                    difference_in_years = int(relativedelta(hoje, aniversario).years)
                    if difference_in_years < 1 or difference_in_years > 159:
                        data = ""
                        print("-----------------------------")
                        print("| DATA FORNECIDA É INVÁLIDA |")
                        print("-----------------------------")
                        print()
                        continue
                    else:
                        return data, difference_in_years
                else:
                    continue
            
def cadastrar_cpf(tela):
    cpf= ""
    while cpf == "":
        cpf_formato_certo = True
        print()
        print(f"-------- {tela} --------")
        print()
        print("[1] Voltar")
        print("[2] Sair")
        print()
        cpf = input("CPF (000.000.000-00): ")

        try:
            num = int(cpf)
            os.system("cls")
            if num == 1:
                cpf = ""
                return cpf  
            
            elif num == 2:
                cpf = ""
                return 4
            
            else:
                cpf = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue

        except ValueError as e:
            os.system("cls")

            if len(cpf) > 14:
                cpf = ""
                print("---------------------------------")
                print("| CPF COM EXCESSO DE CARACTERES |")
                print("---------------------------------")
                print()
                continue

            elif len(cpf) < 14:
                cpf = ""
                print("------------------------------------")
                print("| PREENCHA O CAMPO CONFORME MODELO |")
                print("------------------------------------")
                print()
                continue

            else:
                i = 0
                for char in cpf:
                    if 0 <= i < 3 or 3 < i < 7 or 7 < i < 11 or 11 < i < 14:
                        try:
                            int(char)
                        except ValueError as e:
                            cpf = ""
                            print("------------------------------------")
                            print("| PREENCHA O CAMPO CONFORME MODELO |")
                            print("------------------------------------")
                            print()
                            cpf_formato_certo = False
                            break
                    elif i == 3 and char != "." or i == 7 and char != ".":
                        cpf = ""
                        print("------------------------------------")
                        print("| PREENCHA O CAMPO CONFORME MODELO |")
                        print("------------------------------------")
                        print()
                        cpf_formato_certo = False
                        break
                    elif i == 11 and char != "-":
                        cpf = ""
                        print("------------------------------------")
                        print("| PREENCHA O CAMPO CONFORME MODELO |")
                        print("------------------------------------")
                        print()
                        cpf_formato_certo = False
                        break
                    i += 1
                if cpf_formato_certo:
                    return cpf
                else:
                    continue

def cadastrar_rua(tela):
    rua = ""
    while rua == "":
        print()
        print(f"-------- {tela} --------")
        print()
        print("[1] Voltar")
        print("[2] Sair")
        print()
        rua = input("Rua: ")
        try:
            num = int(rua)
            os.system("cls")
            if num == 1:
                rua = ""
                return rua
            elif num == 2:
                rua = ""
                return 4
            else:
                rua = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue
        except ValueError as e:
            os.system("cls")
            if len(rua) > 50:
                rua = ""
                print("---------------------------------")
                print("| RUA COM EXCESSO DE CARACTERES |")
                print("---------------------------------")
                print()
                continue
            else:
                return rua
            
def cadastrar_numero(tela):
    numero = ""
    while numero == "":
        print()
        print(f"-------- {tela} --------")
        print()
        print("Digite \"Voltar\" para voltar a página anterior")
        print("Digite \"Sair\" para sair da aplicação")
        print()
        numero = input("Número Residencial: ")
        try:
            num = int(numero)
            os.system("cls")
            if num == 0 or len(numero) > 5:
                numero = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue
            else:
                return num
                
        except ValueError as e:
            os.system("cls")
            if numero.lower() == "voltar":
                numero = ""
                return numero
            elif numero.lower() == "sair":
                numero = ""
                return "sair"
            else:
                numero = ""
                print("-------------------------")
                print("| DIGITE APENAS NÚMEROS |")
                print("-------------------------")
                print()
                continue

def cadastrar_bairro(tela):
    bairro = ""
    while bairro == "":
        print()
        print(f"-------- {tela} --------")
        print()
        print("[1] Voltar")
        print("[2] Sair")
        print()
        bairro = input("Bairro: ")
        try:
            num = int(bairro)
            os.system("cls")
            if num == 1:
                bairro = ""
                return bairro
            elif num == 2:
                bairro = ""
                return 4
            else:
                bairro = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue
        except ValueError as e:
            os.system("cls")
            if len(bairro) > 30:
                bairro = ""
                print("------------------------------------")
                print("| BAIRRO COM EXCESSO DE CARACTERES |")
                print("------------------------------------")
                print()
                continue
            else:
                return bairro

def cadastrar_cidade(tela):
    cidade = ""
    while cidade == "":
        print()
        print(f"-------- {tela} --------")
        print()
        print("[1] Voltar")
        print("[2] Sair")
        print()
        cidade = input("Cidade: ")
        try:
            num = int(cidade)
            os.system("cls")
            if num == 1:
                cidade = ""
                return cidade
            elif num == 2:
                cidade = ""
                return 4
            else:
                cidade = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue
        except ValueError as e:
            os.system("cls")
            if len(cidade) > 50:
                cidade = ""
                print("------------------------------------")
                print("| CIDADE COM EXCESSO DE CARACTERES |")
                print("------------------------------------")
                print()
                continue
            else:
                return cidade

def cadastrar_estado(tela):
    estado = ""
    while estado == "":
        print()
        print(f"-------- {tela} --------")
        print()
        print("[1] Voltar")
        print("[2] Sair")
        print()
        estado = input("Estado: ")
        try:
            num = int(estado)
            os.system("cls")
            if num == 1:
                estado = ""
                return estado
            elif num == 2:
                estado = ""
                return 4
            else:
                estado = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue
        except ValueError as e:
            os.system("cls")
            if len(estado) > 50:
                estado = ""
                print("------------------------------------")
                print("| CIDADE COM EXCESSO DE CARACTERES |")
                print("------------------------------------")
                print()
                continue
            else:
                return estado

def cadastrar_cep(tela):
    cep= ""
    while cep == "":
        cep_formato_certo = True
        print()
        print(f"-------- {tela} --------")
        print()
        print("[1] Voltar")
        print("[2] Sair")
        print()
        cep = input("CEP (13165-000): ")

        try:
            num = int(cep)
            os.system("cls")
            if num == 1:
                cep = ""
                return cep  
            
            elif num == 2:
                cep = ""
                return 4
            
            else:
                cep = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue

        except ValueError as e:
            os.system("cls")

            if len(cep) > 9:
                cep = ""
                print("---------------------------------")
                print("| CEP COM EXCESSO DE CARACTERES |")
                print("---------------------------------")
                print()
                continue

            elif len(cep) < 9:
                cep = ""
                print("------------------------------------")
                print("| PREENCHA O CAMPO CONFORME MODELO |")
                print("------------------------------------")
                print()
                continue

            else:
                i = 0
                for char in cep:
                    if 0 <= i < 5 or 5 < i < 9:
                        try:
                            int(char)
                        except ValueError as e:
                            cep = ""
                            print("------------------------------------")
                            print("| PREENCHA O CAMPO CONFORME MODELO |")
                            print("------------------------------------")
                            print()
                            cep_formato_certo = False
                            break
                    elif i == 5 and char != "-":
                        cep = ""
                        print("------------------------------------")
                        print("| PREENCHA O CAMPO CONFORME MODELO |")
                        print("------------------------------------")
                        print()
                        cep_formato_certo = False
                        break
                    i += 1
                if cep_formato_certo:
                    return cep
                else:
                    continue

def visualisar():
    answer = 1
    while 0 < answer < 4:
        print()
        print("-------- Pessoas Cadastradas --------")
        print()
        print()
        print("[1] Ver Todas Pessoas Cadastradas")
        print("[2] Filtrar Pessoas")
        print("[3] Voltar")
        print("[4] Sair")
        print()
        try:
            answer = int(input("Escolha uma opção: "))
            os.system("cls")
        except ValueError as e:
            os.system("cls")
            print("-----------------------------")
            print("| DIGITE UM CARACTER VÁLIDO |")
            print("-----------------------------")
            print()
            continue
        if answer == 1:
            if pessoas("") == 4:
                return 4
        elif answer == 2:
            if tipo_pesquisa() == 4:
                return 4
        elif answer == 3:
            break
        elif answer == 4:
            return 4
        else:
            os.system("cls")
            print("---------------------------")
            print("| DIGITE UM NUMERO VÁLIDO |")
            print("---------------------------")
            print()
            answer = 1
            continue

def pessoas(arg):
    id = ""
    while id == "":
        lista_numero_id = []
        print()
        print("-------- Pessoas Cadastradas --------")
        print()
        print()
        print("Digite \"Voltar\" para voltar a página anterior")
        print("Digite \"Sair\" para sair da aplicação")
        print()
        info_pessoas_dao = PessoaDAO()
        result = info_pessoas_dao.get_pessoas(arg)
        for item in result:
            id_pessoa = int(item[0])
            nome = str(item[1])
            cpf = str(item[2])
            lista_numero_id.append(id_pessoa)

            print(f"ID: {id_pessoa} | NOME: {nome} | CPF: {cpf}")

        print()
        if len(lista_numero_id) == 0:
            input("Nenhuma pessoa foi encontrada...")
            os.system("cls")
            break
        id = input("Digite o ID: ")
        try:
            num = int(id)
            os.system("cls")
            if num not in lista_numero_id:
                id = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue
            else:
                ref_id = id
                id = ""
                if dados_cadastrados(ref_id) == 4:
                    return 4
                
        except ValueError as e:
            os.system("cls")
            if id.lower() == "voltar":
                id = ""
                return id
            elif id.lower() == "sair":
                id = ""
                return 4
            else:
                id = ""
                print("-------------------------")
                print("| DIGITE APENAS NÚMEROS |")
                print("-------------------------")
                print()
                continue

def dados_cadastrados(id):
    answer = 1
    pessoa_info_dao = PessoaDAO()
    result = pessoa_info_dao.get_info_pessoa(id)
    for info in result:
        nome = info[0]
        data_nasc = info[1]
        cpf = info[2]
    if data_nasc == None:
        data_nasc = ""
        difference_in_years = ""
    else:
        hoje = datetime.now()
        difference_in_years = int(relativedelta(hoje, data_nasc).years)
        data_nasc = data_nasc.strftime("%d/%m/%Y")

    while 0 < answer < 6:
        print()
        print("-------- Dados Cadastrados --------")
        print()
        print(f"Nome: {nome}")
        print(f"Data de Nascimento: {data_nasc}  |  Idade: {difference_in_years}")
        print(f"CPF: {cpf}")
        print()
        print("[1] Ver Endereços")
        print("[2] Alterar Dados")
        print("[3] Deletar Pessoa")
        print("[4] Voltar")
        print("[5] Sair")
        print()
        try:
            answer = int(input("Escolha uma opção: "))
            os.system("cls")
        except ValueError as e:
            os.system("cls")
            print("-----------------------------")
            print("| DIGITE UM CARACTER VÁLIDO |")
            print("-----------------------------")
            print()
            continue
        if answer == 1:
            if enderecos(id) == 4:
                return 4
        elif answer == 2:
            if tipo_info_pessoas(id) == 4:
                return 4
            pessoa_info_dao = PessoaDAO()
            result = pessoa_info_dao.get_info_pessoa(id)
            for info in result:
                nome = info[0]
                data_nasc = info[1]
                cpf = info[2]
            if data_nasc == None:
                data_nasc = ""
                difference_in_years = ""
            else:
                hoje = datetime.now()
                difference_in_years = int(relativedelta(hoje, data_nasc).years)
                data_nasc = data_nasc.strftime("%d/%m/%Y")
        elif answer == 3:
            print()
            confirm = input("Digite 'DELETAR' para excluir a Pessoa e seus endereços cadastrados: ")
            if confirm.lower() == "deletar":
                deletar_pessoa_dao = PessoaDAO()
                deletar_pessoa_dao.delete_pessoa(id)

                deletar_endereco_dao = EnderecoDAO()
                deletar_endereco_dao.delete_endereco(id)

                input("Pressione ENTER para continuar...")
                break
            else:
                os.system("cls")
                print("----------------------")
                print("| OPERAÇÃO CANCELADA |")
                print("----------------------")
                print()
                answer = 1
                continue
        elif answer == 4:
            break
        elif answer == 5:
            return 4
        else:
            os.system("cls")
            print("---------------------------")
            print("| DIGITE UM NUMERO VÁLIDO |")
            print("---------------------------")
            print()
            answer = 1
            continue

def tipo_info_pessoas(id):
    tela = "Alterar Dados Cadastrados"
    answer = 1
    pessoa_info_dao = PessoaDAO()
    result = pessoa_info_dao.get_info_pessoa(id)
    for info in result:
        nome = info[0]
        data_nasc = info[1]
        cpf = info[2]
    if data_nasc == None:
        data_nasc = ""
        difference_in_years = ""
    else:
        hoje = datetime.now()
        difference_in_years = int(relativedelta(hoje, data_nasc).years)
        data_nasc = data_nasc.strftime("%d/%m/%Y")
        
    nome_alterado = nome
    data_alterada = data_nasc
    cpf_alterado = cpf
    while 0 < answer < 7:
        print()
        print(f"-------- {tela} --------")
        print()
        print(f"Nome: {nome_alterado}")
        print(f"Data de Nascimento: {data_alterada}  |  Idade: {difference_in_years}")
        print(f"CPF: {cpf_alterado}")
        print()
        print("[1] Alterar Nome")
        print("[2] Alterar Data de Nascimento")
        print("[3] Alterar CPF")
        print()
        print("[4] Confirmar Alterações")
        print("[5] Voltar")
        print("[6] Sair")
        print()
        try:
            answer = int(input("Escolha uma opção: "))
            os.system("cls")
        except ValueError as e:
            os.system("cls")
            print("-----------------------------")
            print("| DIGITE UM CARACTER VÁLIDO |")
            print("-----------------------------")
            print()
            continue

        if answer == 1:
            nome_alterado = cadastrar_nome(tela)
            if nome_alterado == 4:
                return 4
        elif answer == 2:
            data_alterada, difference_in_years = cadastrar_data_nascimento(tela)
            if data_alterada == 4:
                return 4
        elif answer == 3:
            cpf_alterado = cadastrar_cpf(tela)
            if cpf_alterado == 4:
                return 4
            
        elif answer == 4:
            if nome == nome_alterado and cpf == cpf_alterado and data_nasc == data_alterada:
                os.system("cls")
                print("----------------------------------------")
                print("| NENHUMA INFORMAÇÃO PARA SER ALTERADA |")
                print("----------------------------------------")
                print()
                continue
            else:
                date = None
                if data_alterada != "":
                    date = datetime.strptime(data_alterada, "%d/%m/%Y")

                dao_att_pessoa = PessoaDAO()
                dao_att_pessoa.atualizar_pessoas(nome_alterado, cpf_alterado, date, id)

                nome = nome_alterado
                data_nasc = data_alterada
                cpf = cpf_alterado

        elif answer == 5:
            break
        elif answer == 6:
            return 4
        else:
            os.system("cls")
            print("---------------------------")
            print("| DIGITE UM NUMERO VÁLIDO |")
            print("---------------------------")
            print()
            answer = 1
            continue

def enderecos(id_pessoa):
    id = ""
    while id == "":
        lista_numero_id = []
        print()
        print("-------- Endereços Cadastrados --------")
        print()
        print()
        print("Digite \"+\" para adicionar mais um endereço")
        print("Digite \"Voltar\" para voltar a página anterior")
        print("Digite \"Sair\" para sair da aplicação")
        print()
        info_endereco_dao = EnderecoDAO()
        result = info_endereco_dao.get_enderecos(id_pessoa)
        for item in result:

            id_endereco = int(item[0])
            rua = str(item[1])
            numero = int(item[2])
            bairro = str(item[3])
            cidade = str(item[4])
            estado = str(item[5])
            cep = str(item[6])
            endereco_principal = bool(item[7])
            tipo = ""

            if endereco_principal:
                tipo = "Endereço Principal"
            else:
                tipo = "Endereço Secundário"

            lista_numero_id.append(id_endereco)

            print(f"ID: {id_endereco}")
            print(f"Tipo: {tipo}")
            print(f"Endereço: {rua}, {numero} - {bairro} - {cep}")
            print(f"Cidade/Estado: {cidade} / {estado}")
            print()


        
        id = input("Digite o ID: ")
        try:
            num = int(id)
            os.system("cls")
            if num not in lista_numero_id:
                id = ""
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
                print()
                continue
            else:
                ref_id = id
                id = ""
                if dados_cadastrados_enderecos(ref_id, id_pessoa) == 4:
                    return 4
                
        except ValueError as e:
            os.system("cls")
            if id.lower() == "voltar":
                id = ""
                return id
            elif id.lower() == "sair":
                id = ""
                return 4
            elif id == "+":
                id = ""
                if adicionar_endereco(id_pessoa) == 4:
                    return 4
            else:
                id = ""
                print("-------------------------")
                print("| DIGITE APENAS NÚMEROS |")
                print("-------------------------")
                print()
                continue

def dados_cadastrados_enderecos(id, id_pessoa):
    tela = "Alterar Dados Cadastrados"
    answer = 1
    endereco_info_dao = EnderecoDAO()
    result = endereco_info_dao.get_one_endereco(id)
    for item in result:
        rua = str(item[0])
        numero = int(item[1])
        bairro = str(item[2])
        cidade = str(item[3])
        estado = str(item[4])
        cep = str(item[5])
        endereco_principal = bool(item[6])
        tipo = ""

    if endereco_principal:
        tipo = "Endereço Principal"
        num_max = 10
    else:
        tipo = "Endereço Secundário"
        num_max = 12

    rua_alterada = rua
    numero_alterado = numero
    bairro_alterado = bairro
    cep_alterado = cep
    cidade_alterada = cidade
    estado_alterado = estado

    while 0 < answer < num_max:
        if endereco_principal:
            tipo = "Endereço Principal"
            num_max = 10
        else:
            tipo = "Endereço Secundário"
            num_max = 12
        print()
        print("-------- Dados Cadastrados --------")
        print()
        print(f"Tipo: {tipo}")
        print(f"Endereço: {rua_alterada}, {numero_alterado} - {bairro_alterado} - {cep_alterado}")
        print(f"Cidade/Estado: {cidade_alterada} / {estado_alterado}")
        print()
        print("[1] Alterar Rua")
        print("[2] Alterar Número Residencial")
        print("[3] Alterar Bairro")
        print("[4] Alterar CEP")
        print("[5] Alterar Cidade")
        print("[6] Alterar Estado")
        print()
        if endereco_principal:
            num1 = 7
            num2 = 8
            num3 = 9
        else:
            num1 = 9
            num2 = 10
            num3 = 11
            print("[7] Tornar Em Endereço Principal")
            print("[8] Deletar Endereço")
        print(f"[{num1}] Confirmar Alterações")
        print(f"[{num2}] Voltar")
        print(f"[{num3}] Sair")
        print()

        try:
            answer = int(input("Escolha uma opção: "))
            os.system("cls")
        except ValueError as e:
            os.system("cls")
            print("-----------------------------")
            print("| DIGITE UM CARACTER VÁLIDO |")
            print("-----------------------------")
            print()
            continue

        if answer == 1:
            rua_alterada = cadastrar_rua(tela)
            if rua_alterada == 4:
                return 4

        elif answer == 2:
            numero_alterado = cadastrar_numero(tela)
            if numero_alterado == "sair":
                return 4

        elif answer == 3:
            bairro_alterado = cadastrar_bairro(tela)
            if bairro_alterado == 4:
                return 4

        elif answer == 4:
            cep_alterado = cadastrar_cep(tela)
            if cep_alterado == 4:
                return 4

        elif answer == 5:
            cidade_alterada = cadastrar_cidade(tela)
            if cidade_alterada == 4:
                return 4

        elif answer == 6:
            estado_alterado = cadastrar_estado(tela)
            if estado_alterado == 4:
                return 4

        elif endereco_principal:
            if answer == 7:
                if rua == rua_alterada and numero == numero_alterado and bairro == bairro_alterado and cep == cep_alterado and cidade == cidade_alterada and estado == estado_alterado:
                    os.system("cls")
                    print("----------------------------------------")
                    print("| NENHUMA INFORMAÇÃO PARA SER ALTERADA |")
                    print("----------------------------------------")
                    print()
                    continue
                else:
                    endereco_att_dao = EnderecoDAO()
                    endereco_att_dao.atualizar_endereco(rua_alterada, numero_alterado, bairro_alterado, cep_alterado, cidade_alterada, estado_alterado, id)
                    
                    rua = rua_alterada
                    numero = numero_alterado
                    bairro = bairro_alterado
                    cep = cep_alterado
                    cidade = cidade_alterada
                    estado = estado_alterado

            elif answer == 8:
                break
            
            elif answer == 9:
                return 4
        
        elif not endereco_principal:
            if answer == 7:
                setar_endereco_secundario_dao = EnderecoDAO()
                setar_endereco_secundario_dao.set_endereco_secundario(id_pessoa)

                setar_endereco_principal_dao = EnderecoDAO()
                setar_endereco_principal_dao.set_endereco_pricipal(id)

                endereco_principal = True

            elif answer == 8:
                print()
                confirm = input("Digite 'DELETAR' para excluir o endereço selecionado: ")
                if confirm.lower() == "deletar":
                    deletar_endereco_dao = EnderecoDAO()
                    deletar_endereco_dao.delete_endereco_id(id)

                    input("Pressione ENTER para continuar...")
                    break
                else:
                    os.system("cls")
                    print("----------------------")
                    print("| OPERAÇÃO CANCELADA |")
                    print("----------------------")
                    print()
                    answer = 1
                    continue
            
            elif answer == 9:
                if rua == rua_alterada and numero == numero_alterado and bairro == bairro_alterado and cep == cep_alterado and cidade == cidade_alterada and estado == estado_alterado:
                    os.system("cls")
                    print("----------------------------------------")
                    print("| NENHUMA INFORMAÇÃO PARA SER ALTERADA |")
                    print("----------------------------------------")
                    print()
                    continue
                else:
                    endereco_att_dao = EnderecoDAO()
                    endereco_att_dao.atualizar_endereco(rua_alterada, numero_alterado, bairro_alterado, cep_alterado, cidade_alterada, estado_alterado, id)
                    
                    rua = rua_alterada
                    numero = numero_alterado
                    bairro = bairro_alterado
                    cep = cep_alterado
                    cidade = cidade_alterada
                    estado = estado_alterado

            elif answer == 10:
                break

            elif answer == 11:
                return 4

        else:
            os.system("cls")
            print("---------------------------")
            print("| DIGITE UM NUMERO VÁLIDO |")
            print("---------------------------")
            print()
            answer = 1
            continue

def adicionar_endereco(id_pessoa):
    tela = "Cadastrar Novo Endereço"
    answer = 1

    numero = ""
    rua = ""
    bairro = ""
    cidade = ""
    estado = ""
    cep = ""
    endereco_principal = ""

    while 0 < answer < 11:
        pre_requesito_rua = " "
        if rua == "":
            pre_requesito_rua = "*"

        pre_requesito_numero = " "
        if numero == "":
            pre_requesito_numero = "*"

        pre_requesito_bairro = " "
        if bairro == "":
            pre_requesito_bairro = "*"

        pre_requesito_cidade = " "
        if cidade == "":
            pre_requesito_cidade = "*"

        pre_requesito_estado = " "
        if estado == "":
            pre_requesito_estado = "*"

        pre_requesito_cep = " "
        if cep == "":
            pre_requesito_cep = "*"

        pre_requesito_endereco_principal = " "
        if endereco_principal == "":
            pre_requesito_endereco_principal = "*"

        print()
        print(f"-------- {tela} --------")
        print()
        print(f"Tipo: {endereco_principal}")
        print(f"Endereço: {rua}, {numero} - {bairro} - {cep}")
        print(f"Cidade/Estado: {cidade} / {estado}")
        print()
        print(f"[1] {pre_requesito_rua}Rua")
        print(f"[2] {pre_requesito_numero}Número Residencial")
        print(f"[3] {pre_requesito_bairro}Bairro")
        print(f"[4] {pre_requesito_cep}CEP")
        print(f"[5] {pre_requesito_cidade}Cidade")
        print(f"[6] {pre_requesito_estado}Estado")
        print(f"[7] {pre_requesito_endereco_principal}Tipo")
        print()
        print("[8] Confirmar Alterações")
        print("[9] Voltar")
        print("[10] Sair")
        print()

        try:
            answer = int(input("Escolha uma opção: "))
            os.system("cls")
        except ValueError as e:
            os.system("cls")
            print("-----------------------------")
            print("| DIGITE UM CARACTER VÁLIDO |")
            print("-----------------------------")
            print()
            continue

        if answer == 1:
            rua = cadastrar_rua(tela)
            if rua == 4:
                return 4

        elif answer == 2:
            numero = cadastrar_numero(tela)
            if numero == "sair":
                return 4

        elif answer == 3:
            bairro = cadastrar_bairro(tela)
            if bairro == 4:
                return 4

        elif answer == 4:
            cep = cadastrar_cep(tela)
            if cep == 4:
                return 4

        elif answer == 5:
            cidade = cadastrar_cidade(tela)
            if cidade == 4:
                return 4

        elif answer == 6:
            estado = cadastrar_estado(tela)
            if estado == 4:
                return 4

        elif answer == 7:
            print()
            resposta = ""
            while resposta.lower() != "s" and resposta.lower() != "n":
                resposta = input("Cadastrar Endereço como principal (digite 'sair' para voltar a etapa anterior)? [S/N] ")
                os.system("cls")
                if resposta.lower() == "sair":
                    break
                elif resposta.lower() == "s":
                    endereco_principal = "Endereço Principal"
                elif resposta.lower() == "n":
                    endereco_principal = "Endereço Secundário"

        elif answer == 8:
            if rua == "" or numero == "" or bairro == "" or cep == "" or cidade == "" or estado == "" or endereco_principal == "":
                os.system("cls")
                print("----------------------------")
                print("| PREENCHA TODOS OS CAMPOS |")
                print("----------------------------")
                print()
                continue
            else:
                if endereco_principal == "Endereço Principal":
                    endereco_principal = True
                    setar_endereco_secundario_dao = EnderecoDAO()
                    setar_endereco_secundario_dao.set_endereco_secundario(id_pessoa)
                else:
                    endereco_principal = False

                eVO = EnderecoVO(rua, numero, bairro, cidade, estado, cep, id_pessoa, endereco_principal)
                end_dao = EnderecoDAO()
                end_dao.cadastrar_enderecos(eVO.to_dict())

                os.system("cls")
                print("------------------------------------")
                print("| ENDEREÇO CADASTRADO COM SUCESSO! |")
                print("------------------------------------")
                print()

                numero = ""
                rua = ""
                bairro = ""
                cidade = ""
                estado = ""
                cep = ""
                endereco_principal = ""

        elif answer == 9:
            break

        elif answer == 10:
            return 4
        
        else:
            os.system("cls")
            print("---------------------------")
            print("| DIGITE UM NUMERO VÁLIDO |")
            print("---------------------------")
            print()
            answer = 1
            continue

def tipo_pesquisa():
    answer = 1
    while 0 < answer < 5:
        escolha = ""
        print()
        print("-------- Pessoas Cadastradas --------")
        print()
        print()
        print("[1] Pesquisar por Nome")
        print("[2] Pesquisar por CPF")
        print("[3] Voltar")
        print("[4] Sair")
        print()
        try:
            answer = int(input("Escolha uma opção: "))
            os.system("cls")
        except ValueError as e:
            os.system("cls")
            print("-----------------------------")
            print("| DIGITE UM CARACTER VÁLIDO |")
            print("-----------------------------")
            print()
            continue
        if answer == 1:
            escolha = "nome"
            nome = pesquisa(escolha)
            if nome == "sair":
                return 4
        elif answer == 2:
            escolha = "cpf"
            cpf = pesquisa(escolha)
            if cpf == "sair":
                return 4
            
        elif answer == 3:
            break
        elif answer == 4:
            return 4
        else:
            os.system("cls")
            print("---------------------------")
            print("| DIGITE UM NUMERO VÁLIDO |")
            print("---------------------------")
            print()
            answer = 1
            continue

def pesquisa(escolha: str):
    answer = ""
    while answer == "":
        if escolha == "nome":
            look_escolha = escolha.title()
            cpf = ""
        else:
            look_escolha = escolha.upper()
            cpf = " (000.000.000-00)"
        print()
        print(f"-------- Pesquisar {look_escolha} --------")
        print()
        print()
        print("Digite \"Voltar\" para voltar a página anterior")
        print("Digite \"Sair\" para sair da aplicação")
        print()
        print()
        answer = input(f"Digite o {look_escolha}{cpf}: ")
        os.system("cls")
        if answer.lower() == "voltar":
            break
        elif answer.lower() == "sair":
            return "sair"
        else:
            if pessoas(f" WHERE {escolha} LIKE '%{answer}%'") == 4:
                return "sair"
            

iniciar()