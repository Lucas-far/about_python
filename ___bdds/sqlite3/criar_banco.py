

""" Para criar o banco, o arquivo deve ser executado """
import sqlite3

instance_ = sqlite3.connect('nome_banco.db')
command = instance_.cursor()

# EXEMPLO DE CRIAÇÃO DE UMA TABELA
sintaxe_criar = 'CREATE TABLE IF NOT EXISTS hoteis('
campo_pk = 'hotel_id text PRIMARY KEY, '
campo_2, campo_3, campo_4, campo_5 = 'nome text, ', 'estrelas real, ', 'diaria real, ', 'cidade text)'
tabela_criar = sintaxe_criar + campo_pk + campo_2 + campo_3 + campo_4 + campo_5

# COMANDOS PARA VALIDAÇÃO
command.execute(tabela_criar)
instance_.commit()
instance_.close()
