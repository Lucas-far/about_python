

# Instalação do SqlAlchemy
def parte_1():
    """
    pip install SQLAlchemy
    """


# Importar dependências, criar base de herança para um modelo, configurar var da tabela e campos
def parte_2():
    """
    from sqlalchemy.orm import declarative_base
    from sqlalchemy import Column, Integer
    # Outros: String, Float...

    Base = declarative_base()


    class Modelo(Base):
        __tablename__ = 'nome_da_tabela'

        id_ = Column(Integer, primary_key=True, autoincrement=True)
        atributo = Column(String(100))
    """


# Função da classe para configurar um banco
def parte_3():
    """
    @staticmethod
    def database_config(name):
        import sqlalchemy
        engine = sqlalchemy.create_engine(f"sqlite:///{name}")
        return engine
    """


# Função da classe para configurar um cursor, que executa ações no banco
def parte_4():
    """
    @staticmethod
    def database_cursor(engine_var):
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=engine_var)
        cursor = Session()
        return cursor
    """


# Função da classe para configurar a criação do banco
def parte_5():
    """
    @staticmethod
    def database_init(engine_var):
        Base.metadata.create_all(engine_var)
    """


# Função da classe para converter um objeto da classe para formato json (chave pk não deve ser inclusa)
def parte_6():
    """
    @staticmethod
    def json(the_object):
        return {
            "atributo": the_object.atributo
        }
    """


# Função da classe para armazenar os dados do banco em uma "var", com intuito de consulta ou verificação
# Parâmetro referente ao cursor
def parte_7():
    """
    @staticmethod
    def database_as_var(exec_):
        box = []
        for content in exec_.query(Modelo).order_by(Modelo.pk):
            box.append(Modelo.json(the_object=content))
        return box
    """


# Exemplo de código que mostra: criação do banco e adição de dados
# Importação, vars de criação, ver banco, input de dados, conversão do input em objeto, inserção, ver banco
def parte_8():
    """
    importar local do Modelo

    engine = Modelo.database_config(name='nome_do_banco.db')
    cursor = Modelo.database_cursor(engine_var=engine)
    Modelo.database_init(engine_var=engine)

    database = Games.database_as_var(exec_=cursor)
    print(database)

    an_object = input('Insira um jogo -> ')
    an_object_of_class = Games(game=an_object)

    Games.database_insert(exec_=cursor, game_object=an_object_of_class)

    database = Games.database_as_var(exec_=cursor)
    print(database)
    """
