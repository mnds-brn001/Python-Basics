import psycopg2
conn = psycopg2.connect(database = "PRODUTO", user = "postgres", password = "123", host = "localhost", port = "5433")
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""Delete from public."AGENDA" where "id"=1""") 
conn.commit() 
cont=cur.rowcount 
print(cont, "Registro excluído com sucesso!") 
print("Exclusão realizada com sucesso!"); 
conn.close()