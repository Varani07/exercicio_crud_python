from conexao_banco import ConexaoBanco
from mysql.connector import Error
import os

class EnderecoDAO:
    def __init__(self):
        self.connection = ConexaoBanco().get_connection()
        self.cursor = self.connection.cursor()

    def cadastrar_enderecos(self, enderecos_dict):
        try:
            sql = "INSERT INTO enderecos (rua, numero, bairro, cidade, estado, cep, pessoa_id, endereco_principal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (enderecos_dict['rua'], enderecos_dict['numero'], enderecos_dict['bairro'], 
                       enderecos_dict['cidade'], enderecos_dict['estado'], enderecos_dict['cep'], 
                       enderecos_dict['pessoa_id'], enderecos_dict['endereco_principal'])
            
            self.cursor.execute(sql, valores)
            self.connection.commit()
            self.cursor.close()
        except Error as e:
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def delete_endereco(self, id):
        try:
            sql = "DELETE FROM enderecos WHERE pessoa_id = %s"
            self.cursor.execute(sql, (id, ))

            self.connection.commit()
            self.cursor.close()
        except Error as e:
            os.system("cls")
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def get_enderecos(self, id):
        try:
            sql = "SELECT id, rua, numero, bairro, cidade, estado, cep, endereco_principal FROM enderecos WHERE pessoa_id = %s"
            self.cursor.execute(sql, (id, ))
            result = self.cursor.fetchall()
            self.cursor.close()
            return result
        except Error as e:
            os.system("cls")
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def get_one_endereco(self, id):
        try:
            sql = "SELECT rua, numero, bairro, cidade, estado, cep, endereco_principal FROM enderecos WHERE id = %s"
            self.cursor.execute(sql, (id, ))
            result = self.cursor.fetchall()
            self.cursor.close()
            return result
        except Error as e:
            os.system("cls")
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def atualizar_endereco(self, rua, numero, bairro, cep, cidade, estado, id):
        try:
            sql = "UPDATE enderecos SET rua = %s, numero = %s, bairro = %s, cep = %s, cidade = %s, estado = %s WHERE id = %s"
            self.cursor.execute(sql, (rua, numero, bairro, cep, cidade, estado, id))
            self.connection.commit()
            self.cursor.close()
            os.system("cls")
            print("----------------------------------------")
            print("| INFORMAÇÕES ATUALIZADAS COM SUCESSO! |")
            print("----------------------------------------")
            print()
        except Error as e:
            os.system("cls")
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def delete_endereco_id(self, id):
        try:
            sql = "DELETE FROM enderecos WHERE id = %s"
            self.cursor.execute(sql, (id, ))

            self.connection.commit()
            self.cursor.close()
        except Error as e:
            os.system("cls")
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def set_endereco_pricipal(self, id):
        try:
            sql = "UPDATE enderecos SET endereco_principal = %s WHERE id = %s"
            self.cursor.execute(sql, (True, id))
            self.connection.commit()
            self.cursor.close()
            os.system("cls")
            print("----------------------------------------")
            print("| INFORMAÇÕES ATUALIZADAS COM SUCESSO! |")
            print("----------------------------------------")
            print()
        except Error as e:
            os.system("cls")
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def set_endereco_secundario(self, id):
        try:
            sql = "UPDATE enderecos SET endereco_principal = %s WHERE endereco_principal = %s AND pessoa_id = %s"
            self.cursor.execute(sql, (False, True, id))
            self.connection.commit()
            self.cursor.close()
        except Error as e:
            os.system("cls")
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected():
                self.connection.close()