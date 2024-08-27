from conexao_banco import ConexaoBanco
from mysql.connector import Error
import os

class PessoaDAO:
    def __init__(self):
        self.connection = ConexaoBanco().get_connection()
        self.cursor = self.connection.cursor()

    def cadastrar_pessoas(self, pessoas_dict):
        try:
            sql = "INSERT INTO pessoas (nome, data_nasc, cpf) VALUES (%s, %s, %s)"
            valores = (pessoas_dict['nome'], pessoas_dict['data'], pessoas_dict['cpf'])
            self.cursor.execute(sql, valores)
            self.connection.commit()
            self.cursor.close()
            os.system("cls")
            print("----------------------------------")
            print("| PESSOA CADASTRADA COM SUCESSO! |")
            print("----------------------------------")
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

    def get_id_pessoas(self, cpf):
        try:
            sql = "SELECT id FROM pessoas WHERE cpf = %s"
            self.cursor.execute(sql, (cpf, ))
            result = self.cursor.fetchone()
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

    def get_pessoas(self):
        try:
            sql = "SELECT id, nome, cpf FROM pessoas"
            self.cursor.execute(sql)
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

    def get_info_pessoa(self, id):
        try:
            sql = "SELECT nome, data_nasc, cpf FROM pessoas WHERE id = %s"
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

    def delete_pessoa(self, id):
        try:
            sql = "DELETE FROM pessoas WHERE id = %s"
            sc0 = "SET FOREIGN_KEY_CHECKS=0 "
            sc1 = "SET FOREIGN_KEY_CHECKS=1 "

            self.cursor.execute(sc0)
            self.cursor.execute(sql, (id, ))
            self.cursor.execute(sc1)

            self.connection.commit()
            self.cursor.close()
            os.system("cls")
            print("--------------------------------")
            print("| PESSOA DELETADA COM SUCESSO! |")
            print("--------------------------------")
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

    def atualizar_pessoas(self, nome, cpf, date, id):
        try:
            sql = "UPDATE pessoas SET nome = %s, data_nasc = %s, cpf = %s WHERE id = %s"
            self.cursor.execute(sql, (nome, date, cpf, id))
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