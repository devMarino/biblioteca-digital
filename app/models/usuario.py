from sqlalchemy import Column,Integer, String, Enum, Boolean, Date #import columns necessary
from sqlalchemy.orm import relationship #import relationship table
from .enum import TipoUsuario #import file enum typeUsuario
from app import db #import instance db
#Tabela Usuario
class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    matricula = Column(String(50), unique=True, nullable=False)
    tipo_usuario = Column(Enum(TipoUsuario), nullable=False)
    turma = Column(String(50))
    senha = Column(String(255), nullable=False)
    email = Column(String(120), nullable=False)
    telefone = Column(String(20))
    data_cadastro = Column(Date, nullable=False)
    ativo = Column(Boolean, default=True)
    
    # Relacionamentos
    emprestimos = relationship('Emprestimo', back_populates='usuario')
    reservas = relationship('Reserva', back_populates='usuario')
    notificacoes = relationship('Notificacao', back_populates='usuario')
    logs_acesso = relationship('LogAcesso', back_populates='usuario')