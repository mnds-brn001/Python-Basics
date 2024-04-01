import psycopg2

class AppBD:
    def __init__(self):
        print("Método construtor")

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user= "postgres",
                                               password= "123",
                                               host= "localhost",
                                               port="5433",
                                               database= "postgres")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)

    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = '''SELECT * FROM public. "PRODUTO" '''

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Erro na Operação de Seleção", error)

        finally:
            if(self.connection):
                cursor.close()
                self.connection.close( )
                print("A conexao com o PostGreSQL foi fechada!")
            return registros
    
    def InserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query= '''INSERT INTO public. "PRODUTO"
                                        ("CODIGO","NAME","PRECO")
                                        VALUES  (%s,%s,%s)'''
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print (count, "Registro inserido com Sucesso na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if (self.conncetion):
                print("Falha ao inserir registro na Tabela PRODUTO", error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostGreSQL foi fechada com Sucesso!")

    def atualizarDados( self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro antes da Atualização")
            sql_select_query =  '''SELECT * FROM public. "PRODUTO"
                                    WHERE "CODIGO" = %s'''
            cursor.execute(sql_select_query,  (codigo,))
            record = cursor.fetchone()
            print(record)

            # ATUALIZAR REGISTRO
            sql_update_query = '''UPDATE public. "PRODUTO" set "NOME" = %s,
                                    "PRECO" = %s WHERE  "CODIGO" = %s'''
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro Depois de Atualizado")
            sql_select_query = '''SELECT * FROM public. "PRODUTO"
                                WHERE "CODIGO" = %s'''
            cursor.execute(sql_select_query, (codigo))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada com Sucesso!")

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
        # Atualizar registro
            sql_delete_query = '''DELETE FROM public. "PRODUTO"
                            WHERE "CODIGO" = %s'''
            cursor.execute(sql_delete_query, (codigo, ))

            self.connection.commit()
            count = cursor.rowcount
            print( count, "Registro excluído com Sucesso!")
        except ( Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            if(self.connection):
                cursor.close() 
                self.connection.close()
                print(" A conexão foi fechada com Sucesos!")



