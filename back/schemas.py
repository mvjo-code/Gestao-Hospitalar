from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum

#lista fechada com todas as opções de atendimento válidas
class TipoAtendimento(str, Enum):
    ambulatório = "ambulatório"
    cirurgia = "cirurgia"
    exame = "exame"  
    regulacao = "regulação"
    diagnostico = "diagnóstico"
    internacao = "internação"  # adicionar mais se necessário


# paciente
class Paciente(BaseModel):
    prontuario_id: int
    nome: str
    data_nasimento: datetime
    sexo: Optional[str] = None
    telefone: str

# atendimento
class Atendimento(BaseModel):
    Atendimento_id: int
    pronturio_id: int
    especialidade: str
    is_reguled: bool
    tipo_atendimento: TipoAtendimento

# evento
class Evento(BaseModel):
    evento_id: int
    atendimento_id: Optional[int] = None # acredito que nem todo evento esteja relacionado a um atendimento
    tipo_evento: str # entrada, saída
    timestamps_evento: datetime
