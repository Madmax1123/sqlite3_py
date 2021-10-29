import sqlite3
# CONECTA-SE AO BANCO DE DADOS
path_db = sqlite3.connect("local.db")
cursor = path_db.cursor()

# CRIA A TABELA SE NÃO EXISTIR
cursor.execute("""CREATE TABLE IF NOT EXISTS names(
	
	name TEXT
	
	);""")

N_name = input('Insert a name:')
# INSERI VALORES NO DATA
cursor.execute("INSERT INTO names(name) VALUES(?)", (N_name))
path_db.commit()

# SELECIONA VALORES DO DATA E COLOCA SEUS ID"NÚMERAÇÃO"
cursor.execute("SELECT rowid, * FROM names")
names = cursor.fetchall() 
