from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum as SQLEnum, ForeignKey
from database import Base
from datetime import datetime
from enum import Enum

#lista fechada com todas as opções de atendimento válidas
class TipoAtendimento(str, Enum):
    ambulatório = "ambulatório"
    cirurgia = "cirurgia"
    exame = "exame"  
    regulacao = "regulação"
    diagnostico = "diagnóstico"
    internacao = "internação"  # adicionar mais se necessário



class Paciente(Base): 
    __tablename__ = "pacientes"

    prontuario_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    data_nascimento = Column(String) # poderia ser Date, mas para simplificar usei String
    sexo = Column(String, nullable=True)
    telefone = Column(String)

class Atendimento(Base):
    __tablename__ = "atendimentos"

    atendimento_id = Column(Integer, primary_key=True, index=True)
    prontuario_id = Column(Integer, ForeignKey("pacientes.prontuario_id")) 
    especialidade = Column(String)
    is_reguled = Column(Boolean) 
    tipo_atendimento = Column(SQLEnum(TipoAtendimento))

class Evento(Base):
    __tablename__ = "eventos"

    evento_id = Column(Integer, primary_key=True, index=True)
    atendimento_id = Column(Integer, ForeignKey("atendimentos.atendimento_id", nulltable=True))
    tipo_evento = Column(String)
    timestamps_evento = Column(DateTime)