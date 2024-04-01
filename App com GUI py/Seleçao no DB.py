import psycopg2
conn = psycopg2.connect(database = "PRODUTO", user = "postgres", password = "123", host = "localhost", port = "5433")
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro)
conn.commit()
print("Seleção realizada com sucesso!"); 
conn.close()