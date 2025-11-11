from sqlalchemy import Column,Integer, Enum, Text, ForeignKey, Date #import columns necessary
from sqlalchemy.orm import relationship #import relationship table
from .enum import StatusEmprestimo #import file enum statusEmprestimo
from app import db #import instance db

# Tabela Emprestimo
class Emprestimo(db.Model):
    __tablename__ = 'emprestimo'
    
    id_emprestimo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    id_material = Column(Integer, ForeignKey('material.id_material'), nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_prevista_devolucao = Column(Date, nullable=False)
    data_devolucao = Column(Date)
    status = Column(Enum(StatusEmprestimo), default=StatusEmprestimo.ativo)
    observacoes = Column(Text)
    
    # Relacionamentos
    usuario = relationship('usuario', back_populates='emprestimo')
    material = relationship('material', back_populates='emprestimo')