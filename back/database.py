# arquivo de conexao com o banco de dados e definição dos modelos
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sql_alchemy_database_url = "sqlite:///./banco.db" # pode ser outro banco

engine = create_engine(sql_alchemy_database_url, connect_args={"check_same_thread": False}) #
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()